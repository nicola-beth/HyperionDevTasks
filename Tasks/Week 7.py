

#OBJECT ORIENTATED PROGRAMMING
#methods can be applied to variable objects (i.e. variable.split() for string method present in the string object)
#class is different to an object (object is the ho use, class is the blueprint (contains all the info)
#print(dir("string")) - returns methods the string has
"fjvdsc".split()

class Cat():      #start new word with capital letter, different to other code in python (only CLASS Name!)
    print("fvdcsdcs".__str__())     #dedicated method names for our objects (i.e. string here) - convert object into actual text

class Cat():
    def __init__(self, name, breed, gender, age, is_asleep):       #init = initiate, self must always be first in function within a class
        #init keyword inside a class create a constructor
        self.name = name            #self key word - references object itself (this objects name variable = name)
        self.breed = breed          #self. shows where it is being applied
        self.gender = gender
        self.age = age
        self.is_asleep = is_asleep
    def __str__(self):
        return f"Name: {self.name} \n Breed: {self.breed}\n gender: {se;f.gender}\n age: {self.age}\n is asleep: {self.is_asleep}"
    #method example called pet below
    def pet(self):              #pet- custom method name in python
        return f"You pet {self.name}"
    def get_name(self):         #GETTERS
        return self.name            #return gets a value and can then place it into a variable later (or inside a print)
    def set_name(self, name):           #SETTERS
        self.name = name
    def set_sleeping(self):
        if(self.is_asleep):
            self.is_asleep = False
        else:
            self.is_asleep = True

bella = Cat("Bella", "tabby", "F", 12, False)
tabby = Cat("Bella", "Siamese", "F", 1, False)
spike = Cat("Bella", "Orange", "M", 13, True)

cats = [bella, tabby, spike]
#note; variable names are diffferent but can have same values in the object

print(bella)
print("\n")
print(tabby)

for obj in cats:
    print(obj)

for obj in cats:
    print(obj.get_name())

print(bella.pet())
print(tabby.get_name())
tabby.set_name("billy")
print(tabby)

#using return value to create variable or printing
cats_name = bella.get_name()
print(cats_name)
print(bella.get_name())

name = input("Enter name of your cat: ")
millie = Cat(name, "irritating", "F", 3, False)         #must always contain all the values


#inheritance, different classes can inherit attributes from the same class
#fruit class is parent class or apple/banana/mango child class
class Car:
    is_running = False
    def __init__(self, make, model):
        self.make = make
        self.model = model
class PickupTruck(Car):         #whats in the brackets is the inheritance, child has more features than the parent (as has all of parent plus some)
    is_loaded = False
    def load(self):
        self.is_loaded = True
    def unload(self):
        self.is_loaded = False

#example of super() function
class Computer():
    def __init__(self, computer, ram, ssd):
        self.computer = computer
        self.ram = ram
        self.ssd = ssd
class Laptop(Computer):
    def __init__(self, computer, ram, ssd, model):
        super().__init__(computer, ram, ssd)
        self.model = model

class Games:
    #def is a method when used in a classss!!!
    def __init__(self, name, type, developer):      #init needed to make an object & takes in parameters in brackets
        """
        Space to explain what function does
        :param name: description of name (name of game)
        :param type: type of game
        :param developer: who developed the game
        """
        self.name = name        #the objects name will be variable passed in, how object knows what to refer to
        self.type = type
        self.developer = developer      #could have default by doing self.developer = "default value"
    def pirate_game(self):          #methods only run for this object (functions can be run at any time!)
        return f"You got the {self.name} for free"
class ConsoleGame(Games):       #consoleGame is child of Games
    def __init__(self, console, name, type, developer):
        super().__init__(name, type, developer)     #pycharm recognised you need to get super of parent, does it for you!
        #super().__init__ ==== allows child to inherit from parent object, otherwise doesn't know values exist ("GO to my superclass & initialise the variables")
        self.console = console      #anything that's unique to the child gets placed below parent defaults
    def is_too_old(self):
        print(f"The console is too old to run this game")

game = Games("Mario Kart", "RPG", "Niantic")
game.pirate_game()
#CANT HAVE .game.is_too_old()

game = ConsoleGame("Nintendo switch", "Mario Kart", "RPG", "Niantic")
game = ConsoleGame("Nintendo switch", input("Enter a game name: "), "RPG", "Niantic")       #can have input value too
game.is_too_old()
game.pirate_game()      #can have ALL, inc functions in parent

for key in my_dict.keys():
    Games(key)      #creates object based on keys


#multiple inhertiance, limit to 3 MAX! otherwise can loose links
class grandparent:
    def __init__(self, eye_colour):
        self.eye_colour = eye_colour

class parent(grandparent):
    def __init__(self, eye_colour, nose):
        super().__init__(eye_colour)
        self.nose = nose

class child(parent):
    def __init__(self, eye_colour, nose, is_cool):
        super().__init__(eye_colour, nose)
        self.is_cool = is_cool

#EXAMPLES, look at things we can generalise
#CLASS
class Car:
    def __init__(self, make, top_speed, weight):     #method is a function inside a class (init = initialise)
        self.make = make        #these attributes belong to THIS class, can only be used for this class
        self.top_speed = top_speed
        self.weight = weight
    def get_speed(self):
        return self.top_speed
    def set_speed(self, new_speed):
        self.top_speed = new_speed
    def __str__(self):
        return f"{self.make}, {self.top_speed}, {self.weight}"
#OBJECTS
car_one = Car("BWM", 300, 1250)
print(car_one.make, car_one.top_speed, car_one.weight)      #when not added __str__ method
print(car_one)      #when have added __str__ method

#GETTER
print(car_one.get_speed())
#SETTER
car_one.set_speed(350)
print(car_one)

#class vs. instance variable
class Wolf:
    #class variables
    classification = "canine"
    habitat = "forest"
    is_sleeping = False

    def __init__(self, name, age):
        #instance variables
        self.name = name
        self.age = age

    def wake_up(self):
        self.is_sleeping = False

    def sleep(self):
        self.is_sleeping = True

    def show_sleep_status(self):
        if self.is_sleeping == "False":
            return self.name + " is awake"
        else:
            return self.name + " is sleeping"

    def main():
        silver_tooth = Wolf("Wilver Tooth", 6)
        print(silver_tooth.show_sleep_status())

        #method 1 to change sleep state
        silver_tooth.sleep()
        print(silver_tooth.show_sleep_status())

        #method 2 to change sleep state using dot notation
        silver_tooth.is_sleeping = True
        print(silver_tooth.show_sleep_status())

    main()