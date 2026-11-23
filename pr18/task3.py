import csv


class Expense:
    def __init__(self, date, category, amount, comment):
        self.date = date
        self.category = category
        self.amount = amount
        self.comment = comment

    def is_big(self, limit):
        return self.amount > limit

    def describe(self):
        return self.date + " " + self.category + " " + format(self.amount, ".2f") + " (" + self.comment + ")"


def read_expenses(path):
    result = []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            e = Expense(row["date"], row["category"], float(row["amount"]), row["comment"])
            result.append(e)
    return result


if __name__ == "__main__":
    expenses = read_expenses("data/expenses.csv")
    print("Кількість витрат:", len(expenses))
    limit = 100
    print("Великі витрати (більше", limit, "):")
    for e in expenses:
        if e.is_big(limit):
            print(e.describe())
