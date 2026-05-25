# CultureRadar MVP

CultureRadar is a manual-first MVP for a bilingual public research newsletter that tracks culture inflection signals in US-listed companies before those signals are obvious in financial results.

This folder implements the three-month launch plan as an operating kit. It does not claim that any company is improving or deteriorating yet; those judgments must be produced only after the manual research workflow is completed and logged.

## What Is Included

- `data/CultureRadar_MVP_Workbook.xlsx`: the master workbook and single source of truth.
- `data/company_universe.csv`: selected company universe plus alternates.
- `data/judgment_tracker.csv`: importable public judgment tracker header.
- `data/source_library.csv`: manual source shortcuts for each selected company.
- `data/google_alert_queries.csv`: Google Alerts setup queue.
- `data/weekly_cadence.csv`: 12-week operating cadence.
- `templates/`: reusable card, newsletter, X thread, and reader-interview templates.
- `content/`: first public about page, methodology article draft, and launch note draft.
- `docs/`: research SOP, compliance guardrails, and launch checklist.
- `scripts/generate_assets.py`: regenerates the workbook and CSVs from the canonical company list.

## First Run

Run the asset generator whenever you want to rebuild the workbook or CSVs:

```powershell
python .\CultureRadar\scripts\generate_assets.py
```

The script creates:

- `CultureRadar\data\CultureRadar_MVP_Workbook.xlsx`
- `CultureRadar\data\company_universe.csv`
- `CultureRadar\data\judgment_tracker.csv`
- `CultureRadar\data\source_library.csv`
- `CultureRadar\data\google_alert_queries.csv`
- `CultureRadar\data\weekly_cadence.csv`

## Operating Rules

- Use one research system and one judgment tracker for both English and Chinese output.
- Do not publish a judgment without one primary validation metric, a threshold, a deadline, source links, and a timestamp.
- Do not publish hit-rate percentages before at least 10 judgments are closed.
- Do not use buy, sell, hold, target price, position sizing, or personalized investment advice language.
- Treat every company direction as `TBD` until the evidence log is complete.

See also: [`docs/first_judgment_runbook.md`](docs/first_judgment_runbook.md) — the single-day execution checklist used to produce the first real, pre-registered judgment. Re-read its "no optimizing templates today" rule whenever you feel the urge to extend scaffolding instead of running research.

## Default Company Universe

The first 15 selected names are split between enterprise SaaS and semiconductors:

- SaaS: Salesforce, ServiceNow, Workday, Snowflake, Datadog, HubSpot, Atlassian, MongoDB.
- Semiconductor: NVIDIA, AMD, Intel, Micron, Qualcomm, Applied Materials, Lam Research.

Alternates:

- Okta, Twilio, KLA, Tesla (cross-sector — auto / EV / energy).

## Three-Month Output Target

- 12-15 baseline company files completed.
- 8-12 public culture health cards.
- One public judgment tracker with locked thresholds and deadlines.
- Continuous weekly publishing for at least 6 weeks.
- At least 10 useful reader feedback conversations.
