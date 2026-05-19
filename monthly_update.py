"""Monthly automated data refresh script. Run via Windows Task Scheduler or cron."""

import os
import sys
import datetime
import json

sys.path.insert(0, os.path.dirname(__file__))

from fred_fetcher import fetch_all_series
from analyzer import analyze_all


def run_monthly_update():
    print(f"[{datetime.datetime.now()}] PPI monthly update started...")

    raw_data = fetch_all_series(force=True)
    results = analyze_all(raw_data)

    report_dir = os.path.join(os.path.dirname(__file__), "data")
    report_path = os.path.join(report_dir, f"report_{datetime.date.today().strftime('%Y%m')}.json")

    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)

    strong = [r for r in results if r["signal"] in ("Strong Uptrend", "Momentum")]
    decline = [r for r in results if r["signal"] in ("Mild Decline", "Deep Decline")]
    reversal = [r for r in results if r["signal"] == "Reversal"]

    print(f"  Total {len(results)} series analyzed")
    print(f"  Strong Up/Momentum: {len(strong)}")
    print(f"  Decline: {len(decline)}")
    print(f"  Reversal: {len(reversal)}")
    print(f"  Report saved: {report_path}")
    print(f"[{datetime.datetime.now()}] Done!")


if __name__ == "__main__":
    run_monthly_update()
