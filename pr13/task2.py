import math
import sys
from datetime import date, datetime, timedelta
from pathlib import Path


NAME = "Ivan"
SURNAME = "Petrenko"
GROUP = "PZ-11"


DATA_FILE = Path(__file__).parent / "data" / "expenses.csv"
WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday"]


def days_in_month(year, month):
    """Кількість днів у місяці через різницю дат."""
    first = date(year, month, 1)
    if month == 12:
        next_first = date(year + 1, 1, 1)
    else:
        next_first = date(year, month + 1, 1)
    return (next_first - first).days


def read_expenses(path):
    """Повертає словник {дата: сума за цей день}."""
    per_date = {}
    with path.open(encoding="utf-8") as f:
        for number, line in enumerate(f, start=1):
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            parts = line.split(";")
            try:
                day = datetime.strptime(parts[0], "%Y-%m-%d").date()
                amount = float(parts[2])
            except (ValueError, IndexError):
                print(f"warning: line {number} skipped: {line}", file=sys.stderr)
                continue
            per_date[day] = per_date.get(day, 0.0) + amount
    return per_date


print(f"{NAME} {SURNAME}, {GROUP}")

if not DATA_FILE.exists():
    print(f"error: file {DATA_FILE} not found", file=sys.stderr)
    sys.exit(1)

per_date = read_expenses(DATA_FILE)
if not per_date:
    print("error: no valid expenses in file", file=sys.stderr)
    sys.exit(1)

first_day = min(per_date)
last_day = max(per_date)
period_days = (last_day - first_day).days + 1

print(f"period: {first_day:%d.%m.%Y} ({first_day:%A}) - "
      f"{last_day:%d.%m.%Y} ({last_day:%A}), {period_days} days")
print()


week_totals = [0.0] * 7
for day, amount in per_date.items():
    week_totals[day.weekday()] += amount

print("weekday      total")
for i in range(7):
    print(f"{WEEKDAYS[i]:<12} {week_totals[i]:>7.2f}")
print()


all_amounts = []
no_spend = 0
for i in range(period_days):
    day = first_day + timedelta(days=i)
    amount = per_date.get(day, 0.0)
    all_amounts.append(amount)
    if amount == 0:
        no_spend += 1

total = math.fsum(all_amounts)
average = total / period_days
variance = math.fsum((a - average) ** 2 for a in all_amounts) / period_days
std = math.sqrt(variance)

top_day = max(per_date, key=per_date.get)

print(f"total:        {total:.2f}")
print(f"per day:      {average:.2f} +- {std:.2f}")
print(f"top day:      {top_day:%d.%m.%Y} ({top_day:%A}), {per_date[top_day]:.2f}")
print(f"no-spend days: {no_spend}")

month_days = days_in_month(last_day.year, last_day.month)
left = month_days - last_day.day
forecast = average * month_days
print(f"days in {last_day:%B}: {month_days}, left after {last_day:%d.%m}: {left}")
print(f"month forecast: {forecast:.2f}")
