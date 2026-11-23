from task3 import Expense, read_expenses


class ExpenseBook:
    def __init__(self):
        self.items = []

    def add(self, expense):
        self.items.append(expense)

    def total(self):
        s = 0
        for e in self.items:
            s = s + e.amount
        return s

    def by_category(self, category):
        s = 0
        for e in self.items:
            if e.category == category:
                s = s + e.amount
        return s

    def top(self, n):
        sorted_items = sorted(self.items, key=lambda e: e.amount, reverse=True)
        return sorted_items[:n]


if __name__ == "__main__":
    book = ExpenseBook()
    for e in read_expenses("data/expenses.csv"):
        book.add(e)

    print("Всього витрат:", len(book.items))
    print("Загальна сума: %.2f" % book.total())

    print()
    print("Суми за категоріями:")
    categories = []
    for e in book.items:
        if e.category not in categories:
            categories.append(e.category)
    for c in categories:
        print(" ", c, "%.2f" % book.by_category(c))

    print()
    print("Топ-3 витрат:")
    for e in book.top(3):
        print(" ", e.describe())
