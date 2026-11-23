class Student:
    
    college = "FKTBP VNU"
    count = 0

    def __init__(self, name, surname, group, birth_year):
        self.name = name
        self.surname = surname
        self.group = group
        self.birth_year = birth_year
        Student.count = Student.count + 1

    def full_name(self):
        return self.name + " " + self.surname

    def age(self, year):
        return year - self.birth_year

    def card(self):
        line1 = self.full_name()
        line2 = "group: " + self.group
        line3 = "age in 2026: " + str(self.age(2026))
        width = 21
        border = "+" + "-" * width + "+"
        text = border + "\n"
        for line in [line1, line2, line3]:
            text = text + "| " + line.ljust(width - 2) + " |\n"
        text = text + border
        return text


if __name__ == "__main__":
    me = Student("Nazar", "Mischuk", "IT-32", 2009)
    friend = Student("Vlad", "Kudryk", "IT-32", 2009)
    print(me.card())
    print(friend.card())
