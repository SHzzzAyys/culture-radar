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


def fmt_currency(n):
    if n is None:
        return DASH
    try:
        n = float(n)
    except (TypeError, ValueError):
        return DASH
    if n >= 1e12:
        return f"${n / 1e12:.2f}T"
    if n >= 1e9:
        return f"${n / 1e9:.1f}B"
    if n >= 1e6:
        return f"${n / 1e6:.0f}M"
    return f"${n:,.0f}"


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


def fetch_one(ticker: str) -> dict:
    try:
        info = yf.Ticker(ticker).info
    except Exception as exc:
        return {"error": f"yfinance fetch failed: {exc}"}
    return {
        "marketCap": fmt_currency(info.get("marketCap")),
        "revenue": fmt_currency(info.get("totalRevenue")),
        "pe": fmt_ratio(info.get("trailingPE")),
        "revGrowth": fmt_pct(info.get("revenueGrowth")),
        "employees": fmt_int(info.get("fullTimeEmployees")),
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
