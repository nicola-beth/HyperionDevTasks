#STACK TRACE! big dump of error details, link in this text
#errors related to functions, recurrsive call (steps it took to get to this error)
#list of errors but best to go to the last line first
#lots of different types of errors (exception = error)
#hypothesis-driven debugging - change something with a hypothesis something will happen, ger closer to understand code
#break it down based on stack trace
#Questions:
        #1. When did it start? (new line/variable)
        #2. Is it a recent change?
        #3. Could it have arisen from a recent change?
#try, #except - error handling options

#capston3
details = open('details.txt', 'r')
details_dict = {}
for detail in details:
    key, value = detail.split(", ")
    details_dict[key] = value.strip("\n")

while True:
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    correct_pass = details_dict.get(username)
    if correct_pass == password:
        print("Welcome, you are logged in!")
        break
    print("Incorrect details, try again.")


username = "admin"
option = input("Select an option: ")
if option == "r" and username == admin:
    print("Hi, admin - you can add an account.")
else:
    print("You are not allowed to add an account.")

list_one = ['a', 'b', 'c']
list_two = [1,2,3]
dict_data = {}

for i in ragne(len(list_two)):
    dict_data[list_one[i]] = list_two[i]

num_overdue = {'bob', 0}
num_overdue["bob"] += 1

num_completed = {}
num_uncomp = {}

num_dict = {
    'bob': 0,
    'nicola': 7,
    'harry': 9
}
for k, v in num_dict.index():
    print(k, v)

data = {'g': 2, 'o': 3, 'l': 1, 'e': 1}

#2D lists
multi_list = ["ally", 22, "jeff", 33, "sam", "jemmy", 67]       #ISSUE & how to solve, put list in list
multi_list = [["ally", 22], ["jeff", 33], ["sam"], ["jemmy", 67]]
multi_list = [
            ["ally", 22],
            ["jeff", 33],
            ["sam"],
            ["jemmy", 67]
]
print(multi_list[1])
print(multi_list[1][1])     #index in both lists

#for loop twice for first list then nested list (inner list)
for data in multi_list:
    for info in data:
        print(info)

#ragged lists, rows of different lengths (calc length of rows dynamically) i.e. sam above (only 1 index)
for data in range(len(multi_list)): #only looping on length of data
    for info in range(len(data)):
        print(info)

#multi-dimentional lists
multi_list = [
            ["ally", ["doctor", "lecturer"]],
            ["jeff", 33],
            ["sam"],
            ["jemmy", 67]
]


#ERROR HANDLING!
#if statements
output = "r - reg user"
output += "v - view all users"
while True:
    print(output)
    choice = input("Enter a choice: ")_
    if choice == "r":
        print("Register")
        break
    elif choice == "v":
        print("view")
        break
    else:
        print("You have selected an invalid option")        #THIS IS ERROR HANDLING
        continue #will run the rest of the code & take back to the while True

#TRY/EXCEPT --- try to run code you tell it to go through (if crashes, will go down to except & show there was an error)
try:
    choice  = int(input("Enter a number: "))
    print(choice)
except ValueError:      #can have without error type (default crash catch)
    print("Hey, you entered a word, not a number!")
    choice == "ERR"
except FileExistsError:     #multipe excepts based off error

if choice == "ERR":
    print("Hey, this program crashed")
else:
    print(choice)

#----handle error using if statement
choice = input("Enter number 1: ")
num_2 = int(input("Enter number 2: ")
if num_2 == 0:
    print("We can't devide by 0. Setting number 2 to 1")
    num_2 = 1

choice = "fdvc"
if type(choice) == type(1):
    print("Same variable type")

#-------final will ALWAYS run, irrespective of if the try or except ran
try:
    choice  = int(input("Enter a number: "))
    print(choice)
except ValueError:      #can have without error type (default crash catch)
    print("Hey, you entered a word, not a number!")
    choice == "ERR"
except ZeroDivisionError:     #multipe excepts based off error
    print("Hey, tou can't divide by a number by 0")
finally:            #remove/close/edit as final step
    print("This runs as a last position!")

#example, making error/exception an object
file = None
try:
    file = open('input.txt', 'r')
    #do stuff to the file
except FileNotFoundError as error:
    print("The file you are trying to open does not exist.")
    print(error)
finally:
    if file is not None:
        file.close()

#raising exceptions
num = int(input("Please enter a value greater than 10")))
if num < 10:
    raise Exception(f"num was less than 10, the value of num was: {num}")


#DATETIME RUN THROUGH
import datetime import date
date_str = "2023-01-23"
date_format = "%Y-%m-%d"
dt = datetime.datetime.strptime(date_str, date_format)
print(dt)
date_object = datetime.datetime.strptime(date_str, date_format)
#options on ... date_object.c...
#conditional checks with the date
if date_object > datetime.datetime.today():
    print("This is in the future")
else:
    print("THis is in the past")
date - input("Enter the day it's due (1-31): ")
if date > 31:
    print("Oh, too big - try again!")

month = input()
year = input()
date = f'{date}-{month}-{year}'

import datetime  # datetime is the name of a package and a module

# to use it as normal in code without doing the below 'datetime.datetime....', you would do:
# import datetime (this is the module) from datetime (this is the package)

while True:
    try:
        new_task_due_date = input("Enter task due date (17 Jan 2023)): ")

        # strftime would require a datetime object. 'strptime' creates this
        new_task_due_date_obj = datetime.datetime.strptime(new_task_due_date, '%d %b %Y')        new_task_due_date = input("Enter task due date (17 Jan 2023)): ")

        # strftime would require a datetime object. 'strptime' creates this
        new_task_due_date_obj = datetime.datetime.strptime(new_task_due_date, '%d %b %Y')

