class Person:
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person created")

    def who_am_i(self):
        print("Im Amdin")

    def eating(self):
        print("Im eating")


class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        print("Student Created..")


p1 = Person("Ali", "Veli")
p2 = Student("Minel", "Deli")

print(p1.firstName + " " + p1.lastName)
print(p2.firstName + " " + p2.lastName)

p1.who_am_i()
p2.who_am_i()
p1.eating()
p2.eating()
