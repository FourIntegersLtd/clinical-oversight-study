"""Write the blind sheet for the second rater: 30 answers, no labels, no error types.

Run after the items are checked and frozen. Send only review/rater2_sheet.csv to the colleague.
"""
import csv
from pathlib import Path

from study import items as items_mod

OUT = Path(__file__).resolve().parent.parent / "review" / "rater2_sheet.csv"


def main():
    sample = items_mod.rater_sample(items_mod.load())
    with OUT.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["item", "question", "answer", "verdict", "reason"])
        for i, a in enumerate(sample, 1):
            w.writerow([f"R{i:02d}", a["question"], a["text"], "", ""])
    print(f"Wrote {len(sample)} answers to {OUT}")


if __name__ == "__main__":
    main()
