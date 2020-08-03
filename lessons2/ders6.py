class Person:
    pass

    def __init__(self, name, year):
        self.name = name
        self.year = int(year)
        print("init metodu çalıştı.")

    def calculateAge(self):
        return 2020 - self.year

    def intro(self):
        print("hello yücel bey")


p1 = Person("ahmet", "1989")
p2 = Person("minel", "2007")
print(f"adım: {p1.name} ve yaşım: {p1.calculateAge()}")
print(f"adım: {p2.name} ve yaşım: {p2.calculateAge()}")
