from task1 import Student

me = Student("Nazar", "Mischuk", "IT-32", 2009)
friend = Student("Vlad", "Kudryk", "IT-32", 2009)

print("college через клас:", Student.college)
print("college через обʼєкт me:", me.college)
print("college через обʼєкт friend:", friend.college)


me.college = "Another college"
print()
print("Після me.college = 'Another college':")
print("me.college:", me.college)
print("friend.college:", friend.college)
print("Student.college:", Student.college)

print()
print("Кількість створених студентів:", Student.count)

print()
print("me.__dict__:", me.__dict__)
print("friend.__dict__:", friend.__dict__)
print("'college' in Student.__dict__:", "college" in Student.__dict__)
print("'count' in Student.__dict__:", "count" in Student.__dict__)
