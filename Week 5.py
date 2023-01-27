#dictionaries
#good for user information
#cannot have duplicate keys! will error out, nice to format on different lines
#reference using the key!
#can't look up values, only keys!
user_database = {
    "001": "Jess",
    "002": "Nicola",
    "003": "Max"
}
print(user_database[002])
#return values
for value in user_database.values():
    print(value)
#return keys
for key in user_database.keys():
    print(key)
#return keys & values
for items in user_database.items():
    print(items)

#dictionary with multiple values
user_database = {
    "001": ["Jess", "Rush"],
    "002": ["Nicola", "Brown"],
    "003": ["Max", "Burton"],
}

#dictionary from txt file
file = open("data.txt", "r")
user_database = {}
for line_num, line in enumerate(file):      #enumerate counts each value 1, 2, 3, .. therefore line_num is always going to be a num (will set the key to a number)
    user_database[line_num] = line
print(user_databse)

#repalce value
user_databse = {
    "001" : "Jess"
}
user_database[001] = "Nicola"

#to for loop a dictionary
for key, value in user_database.items():
    print(f"Key: {key} Value: {value}")

#adding to dictionary
user_database = {
    "Nicola": 1
}
tasks = ["Nicola", "Jess", "sam"]
for task in tasks:
    if task == "Nicola":
        user_database["Nicola"] += 1


#FUNCTIONS, inbuilt
#zip() takes 2 iterable lists  and zips them together in a for loop
list_a = [1, 2, 3, 4, 5]
list_b = [10, 9, 8, 7, 6]
for a, b in zip(list_a, list_b):
    print(a, b)


#make sure function only does ONE thing! if want 3 things done, make THREE functions
#functions can see out , but rest of code cannot see in!

def addition(x,y): #parameters are the data you'll need to feed into your function
    total = x + y
    print(total)

def addition(x,y):
    total = x + y
    return total

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter a number: "))

#how to call the function, including required parameters (these values are called arguments)
addition(num1, num2)


def add_one(x): #function has one parameter, x (parameter = declared in function definition, they store the data needed to perform the lofic that the function specifes)
    y = x + 1
    return y    #return will pass back the value to whatever code called the function
result_num - add_one(5) #5 = argument
print(result_num)

def multiple(num1, num2 = 5):
    total = num1 + num2
    print(f"{num1} + {num2} = {total}")
times_5 - multiple(6)
print(times_5)          #defaults to 5, as set as default in function
times_5 - multiple(6, 7)
print(times_7)      #7 overrides the default



#FUCTIONS WITH LOGAN
#program - import, global_vars, functions, main body of code - THIS ORDER
#variables made inside a function cannot be used after
#variables made inside for/while loop can be used elsewhere BUT will ONLY save if code runs through that part
#global-variables: take up memory, reduces efficiency - try avoid where can

def boil_water():       #function can have 0 or many parametrs, which you DO NOT need to define!!
    print("Boil the water")

def add_milk(milk_type):            #milk_type is a variable which doesn't have a value yet, replacing value of milk_type = what_milk (make sure they are different!)
    print(f"Add {what_milk} milk to the drink")

what_drink = input("Coffee or tea or hot chocolate?")
what_milk = print("What milk would you like?: ")

if what_drink == "coffee":
    boil_water()
    print("Add coffee")
    add_milk(what_milk)
elif what_drink == "tea":
    boil_water()
    print("Add tea")
    add_milk(what_milk)
elif what_drink == "hot chocolate":
    boil_water()
    print("Add hot chocolate")
    add_milk(what_milk)

#RETURN on FUNCTIONS
def add_numners (num1, num2):       #parameters are variables which don't exist
    return num1 + num2          #return if will use the data further down your code

def add_numners (num1=5, num2=17):       #can add default values but will be ignored if replaced when function is called
    return num1 + num2

def add_numbers(num1, num2)
    total = num1 + num 2
    return total

added = add_numbers(5,6)        #adding values to the parameters

#example using the above
total = 0
first_run = True
while True:
    if first_run:
        num1_input = int(input("Enter your first number: "))
        num2_input = int(input("Enter your second number: "))
        new total = add_numners(num1_input, num2_input)
        total = new_total
        first_run = False
        continue
    num1_input = int(input("Enter your number: "))
    if num1_input == -1:        #quitting system to stop infinite loop
        break
    total = add_numbers(total, num1_input)
    print(f"New total = {total}")

#function which has a print and a return
 def subtract_numbers(num1, num2):
     print(f"Number 1: {num1}, Number 2: {num2}")       #print statement comes before return as return marks end of a function
     return num2 - num2                 #return variable value to be used outside of function #return marks END of function

