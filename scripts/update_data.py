#!/usr/bin/env python3
"""把 data/judgments/*.jsonl 聚合为 latest.json，供前端加载。"""
import json, pathlib, datetime

JUDGMENTS_DIR = pathlib.Path(__file__).resolve().parents[1] / "data" / "judgments"
OUTPUT = JUDGMENTS_DIR / "latest.json"

def build_latest():
    all_judgments = []
    for f in sorted(JUDGMENTS_DIR.glob("*.jsonl")):
        if f.name.startswith("_"):
            continue
        for line in f.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                all_judgments.append(json.loads(line))

    # 按日期倒序
    all_judgments.sort(key=lambda x: x.get("date", ""), reverse=True)

    OUTPUT.write_text(json.dumps({
        "generated_at": datetime.datetime.now().isoformat(),
        "count": len(all_judgments),
        "judgments": all_judgments
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[update_data] 写入 {len(all_judgments)} 条判断 → {OUTPUT}")

if __name__ == "__main__":
    build_latest()
