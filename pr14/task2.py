import sys
from pathlib import Path

from tabulate import tabulate


NAME = "Nazar"
SURNAME = "Mischuck"
GROUP = "IT-32"


DATA_FILE = Path(__file__).parent / "data" / "expenses.csv"

print(f"{NAME} {SURNAME}, {GROUP}")

if not DATA_FILE.exists():
    print(f"error: file {DATA_FILE} not found", file=sys.stderr)
    sys.exit(1)


groups = {}
with DATA_FILE.open(encoding="utf-8") as f:
    for number, line in enumerate(f, start=1):
        line = line.strip()
        if line == "" or line.startswith("#"):
            continue
        parts = line.split(";")
        try:
            category = parts[1]
            amount = float(parts[2])
        except (IndexError, ValueError):
            print(f"warning: line {number} skipped: {line}", file=sys.stderr)
            continue
        if category not in groups:
            groups[category] = [0, 0.0]
        groups[category][0] += 1
        groups[category][1] += amount

rows = []
total_count = 0
total_sum = 0.0
for category, (count, total) in groups.items():
    rows.append([category, count, total])
    total_count += count
    total_sum += total
rows.append(["TOTAL", total_count, total_sum])

print(tabulate(rows, headers=["category", "count", "total"],
               tablefmt="github", floatfmt=".2f"))