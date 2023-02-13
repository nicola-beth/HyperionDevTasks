class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour

    def can_drive(self):
        print(f"Name: {self.name} is {self.age} and are therefore old enough to drive.")

class Child(Adult):
    def __init__(self, name, age, hair_colour, eye_colour):
        super().__init__(name, age, hair_colour, eye_colour)

    def can_drive(self):
        print(f"Name: {self.name} is {self.age} and are therefore too young to drive.")

name = input("Enter a name: ")
age = input("Enter an age: ")
hair_colour = input("Enter a hair colour: ")
eye_colour = input("Enter an eye colour: ")

person_1 = []
person_1.append(name)
person_1.append(age)
person_1.append(hair_colour)
person_1.append(eye_colour)

if age >= 17:
    Adult.can_drive(person_1)
else:
    Child.can_drive(person_1)