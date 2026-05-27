# Judgments Data

每个公司一个 JSONL 文件，文件名为 `{TICKER}.jsonl`。
每行一条判断记录，格式如下：

```json
{"date":"2026-05-27","company":"Salesforce","ticker":"CRM","direction":"improving","metric":"Glassdoor CEO approval","threshold":"≥65%","deadline":"2026-08-01","difficulty":"debatable","status":"open","evidence":["https://glassdoor.com/..."],"notes":"Q1 earnings showed..."}
```

字段说明：
- `direction`: `improving` / `stable` / `deteriorating` / `tbd`
- `difficulty`: `obvious` / `debatable` / `contrarian`
- `status`: `open` / `resolved-correct` / `resolved-wrong` / `expired`
- `evidence`: 来源链接数组（可为空数组）
- `notes`: 判断依据的简短描述

新增判断：在对应 `{TICKER}.jsonl` 文件里追加一行 JSON，保存后运行
`python scripts/update_data.py` 重新生成 `latest.json`。
