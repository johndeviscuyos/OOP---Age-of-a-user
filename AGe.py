import datetime

print(datetime.date.today())
class Person():
    def __init__(self, name = "", country = "", birthyear = 0, birthmonth = 0):
        self.name = name
        self.birthyear = birthyear
        self.birthmonth = birthmonth
        self.county = country
        self.age = 0


    def get_name(self):
        self.name = input("Enter your name: ")

    def get_birthyear(self):
        while True:
            try:
                self.birthyear = int(input("Enter your birth year: "))
                if 1920 <= self.birthyear <= 2024:
                    break
                else:
                    print("Invalid birth year")
            except ValueError:
                print("Invalid birth year input")


    def get_birthmonth(self):
        while True:
            try:
                self.birthmonth = int(input("Enter your birth month: "))
                if  1 <= self.birthmonth <= 12:
                    break
                else:
                    return "Invalid birthmonth"
            except ValueError:
                return "Invalid input for birth month"

    def get_county(self):
        self.county = input("Enter your county: ")

    def calculate_age(self):
        if self.birthmonth <= 7:
            self.age = (2024 - self.birthyear)
        else:
            self.age = (2023 - self.birthyear)
        return self.age


person1 = Person()
person1.get_name()
person1.get_birthyear()
person1.get_birthmonth()
person1.get_county()
person1.calculate_age()

print(f'your age is ',person1.calculate_age())

