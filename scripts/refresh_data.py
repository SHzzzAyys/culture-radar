"""
Refresh live company fundamentals from yfinance.

Reads the ticker list from scripts/generate_assets.py (single source of truth),
fetches market cap / revenue / P/E / revenue growth / employee count, and
writes data/live_companies.json.

The HTML dashboard fetches this JSON at page load and merges it with
data/curated_companies.json (manually curated culture narrative).
"""
from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import yfinance as yf

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from generate_assets import COMPANIES

OUT = ROOT / "data" / "live_companies.json"

DASH = "—"


def fmt_currency(n, currency="USD"):
    if n is None:
        return DASH
    try:
        n = float(n)
    except (TypeError, ValueError):
        return DASH
    prefix = "$" if currency == "USD" else f"{currency} "
    if n >= 1e12:
        return f"{prefix}{n / 1e12:.2f}T"
    if n >= 1e9:
        return f"{prefix}{n / 1e9:.1f}B"
    if n >= 1e6:
        return f"{prefix}{n / 1e6:.0f}M"
    return f"{prefix}{n:,.0f}"


def fmt_pct(n):
    if n is None:
        return DASH
    try:
        n = float(n)
    except (TypeError, ValueError):
        return DASH
    sign = "+" if n >= 0 else ""
    return f"{sign}{n * 100:.0f}%"


def fmt_int(n):
    if n is None:
        return DASH
    try:
        n = float(n)
    except (TypeError, ValueError):
        return DASH
    if n >= 1e6:
        return f"{n / 1e6:.1f}M"
    if n >= 1e3:
        return f"{n / 1e3:.0f}K"
    return f"{n:,.0f}"


def fmt_ratio(n):
    if n is None:
        return DASH
    try:
        n = float(n)
    except (TypeError, ValueError):
        return DASH
    if n <= 0:
        return DASH
    return f"{n:.0f}"


def fmt_price(n, currency="USD"):
    if n is None:
        return DASH
    try:
        n = float(n)
    except (TypeError, ValueError):
        return DASH
    prefix = "$" if currency == "USD" else f"{currency} "
    if n >= 1000:
        return f"{prefix}{n:,.0f}"
    if n >= 10:
        return f"{prefix}{n:.2f}"
    return f"{prefix}{n:.3f}"


def fmt_pct_signed(n):
    """Format a raw percent value (e.g. 12.5 -> '+12.5%'). Used for daily/monthly changes."""
    if n is None:
        return DASH
    try:
        n = float(n)
    except (TypeError, ValueError):
        return DASH
    sign = "+" if n >= 0 else ""
    return f"{sign}{n:.1f}%"


def safe_pct_change(series, days_back):
    """Calculate % change comparing latest close to N trading days back. None if insufficient data."""
    if series is None or len(series) <= days_back:
        return None
    try:
        latest = float(series[-1])
        prior = float(series[-days_back - 1])
        if prior == 0:
            return None
        return (latest / prior - 1) * 100
    except (TypeError, ValueError, IndexError):
        return None


def fetch_one(ticker: str) -> dict:
    try:
        t = yf.Ticker(ticker)
        info = t.info
        hist_df = t.history(period="6mo", interval="1d", auto_adjust=False)
        closes = hist_df["Close"].dropna().tolist() if not hist_df.empty else []
    except Exception as exc:
        return {"error": f"yfinance fetch failed: {exc}"}

    currency = info.get("financialCurrency", "USD") or "USD"
    current_price = info.get("currentPrice")
    if current_price is None and closes:
        current_price = closes[-1]

    return {
        "marketCap": fmt_currency(info.get("marketCap"), currency),
        "revenue": fmt_currency(info.get("totalRevenue"), currency),
        "pe": fmt_ratio(info.get("trailingPE")),
        "revGrowth": fmt_pct(info.get("revenueGrowth")),
        "employees": fmt_int(info.get("fullTimeEmployees")),
        "price": fmt_price(current_price, currency),
        "change30dPct": fmt_pct_signed(safe_pct_change(closes, 21)),
        "change90dPct": fmt_pct_signed(safe_pct_change(closes, 63)),
        "change30dRaw": safe_pct_change(closes, 21),
        "priceHistory": [round(float(c), 2) for c in closes] if closes else [],
        "priceCurrency": "USD" if currency == "USD" else currency,
    }


def main() -> None:
    tickers = [c["ticker"] for c in COMPANIES]
    print(f"Refreshing {len(tickers)} tickers via yfinance...")
    results = {}
    for ticker in tickers:
        print(f"  {ticker}...", end=" ", flush=True)
        results[ticker] = fetch_one(ticker)
        print("ok" if "error" not in results[ticker] else f"FAIL ({results[ticker]['error']})")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "updatedAt": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "tickers": tickers,
        "companies": results,
    }
    OUT.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nWrote {OUT} ({len(results)} tickers).")


if __name__ == "__main__":
    main()
