formy_list = []
for num in range(100):
    my_list.append(num)
print(my_list)
my_list.sort(reverse=True)      #rule has to be outside a print statement
print(my_list)

my_list[0] = 'pie'      #change index 0 to pie
print(my_list)

for num in range(100):
    my_list.append(f'{num} pie')        #replace in first for loop to see pie added to each number

print(my_list.index('2 pie'))       #prints index number

print (my_list)

for num in range(0, len(my_list), 10):
    print(num)

middle = len(my_list) / 2
middle_value = my_list[int(middle)]      #requesting index of middle value calculatedd above

if "2pie" in my_list:
    value = my_list.index("2pie")
    my_list[value] = "New data"

if "2pie" in my_list:
    my_list[my_list.index("2pie")] = "New data"

value = input("Enter your search query")
if "2pie" in my_list:
    my_list[my_list.index(value)] = "New data"
else:
    print("That wasn't a word")

my_list = []
for num in range (2,11):
    my_list.append(f'{num}PIE')
print(" ".join(my_list))        #turns list into a string

names = ['jeff', 'bob', 'sam']
age = [1, 2, 3]
for i in range(len(names)):  #as both lists are same length this will work
    print(f'{names[i]} is {age[i]}')

names.extend(age)       #will add values into the list
print(names)

names.append(age)       #will add list into list

names.inset(0, "sam")   #add into position you ask it go into (i.e. 0)

names[0] = "sam"       #replaces first name with Sam

names.clear         #deletes the whole list

numbers = [1 ,2, 3, 4, 5]
popped_number = numbers.pop()       #if no index defined, popped will remove last item in list and return it as a variable

double_numbers = [num * 2 for num in numbers]

#define variables included in if statement before, as if 'if statement' isn't run, then variable won't be created & could break programme

#i/o - input/output
#read from a file, we must open it first open() and save as file object in a variable
#txt file must be in same project file on computer
#file = open(file_name.txt, access_mode)
#access_modes =
# r (read),
# w (write),
# r+ (read and write)
# w+ (read and write) - creates file if does not exist
#a - add to end of file write only
#a+ - add to end of the file and can read and write
#print(file_name.txt.readLine()) - returns ONE line
#print(file_name.txt.readLines()) - returns ALL lines
#if file remains open, w will add to file (not overwrite)
#if file is closed then reopened, will overwrite


for line in age:
    print(line) #prints every line in text file

file = open('folder/file.txt', 'r') #if file in a specific folder

file_name = input("What is the file name?") + '.txt'
f = open(file_name, "r")
print(f.read())
print(f.readLine())
print(f.readLines())

lines = f.readline()
lines = f.read()
print(lines)

f.close()       #close the file

#opition1, file set as variable
file_2 = open('file.txt', 'a+')
file_2.write("\nNew line in file")

#option2, create variable but do not need to close
with open('file.txt', 'w') as file_3:
    file_3.read()
    print(file_3.read())
print("You've left and the file is closed")

file_read = open('data/ages.txt', 'r')
file_write = open('data/ages.txt', 'w')

file_read = open('data/ages.txt', 'r')
new_ages = open('data/ages2.txt', 'r+')
current_data = file_read.readLines()
new_data = new_ages.readLines()
for line in current_data:
    new_ages.write(line)
file_read.close()     #must close first to see it printed?
new_ages.close()

file_read = open('data/ages.txt', 'r')
new_ages = open('data/ages2.txt', 'r')
current_data = file_read.readLines()
new_data = new_ages.readLines()
current_data.extend(new_data)
print(current_data)
print(new_data)
file_read.close()
new_ages.close()


file_read.seek(0) #goes tp top of file, without having to close and reopen

name_read = open('data/ages.txt', 'r', encoding='utf-8')
name_write = open('data/ages.txt', 'w')

print(name_read.readLines())
print("&&&&")
print(name_read.readLines()) #at bottom of file so will be empty
name_read.seek(0)   #takes to beginning of file
print(name_read.readLines())

f = open('test.txt', 'r')
print(f.mode)
print(f.name)
f.close()

with open('test.txt', 'r') as f:
    f_contents = f.read()   #load ALL of contents of file into memory via a variable
    print(f_contents)
    f_contents = f.read(100)   #read first 100 characters
    print(f_contents)
    f_contents = f.readLine()   #load 1 line
    print(f_contents)
    for line in f:
        print(line, end="") #removes empty line between lines in a file

#automatically closed the file, inc. if any exceptions - clean up taken care of
print(f.closed)     #will show file is closed: True
print(f.read())     #will not work

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


all_movies = ["Interstella", "Submarine", "Avengers", "Roma"]

print(len(all_movies))  #number of items in the list
print(all_movies[0:2]) #first position defined is included, last position defined is not included

var = "Roma" in all_movies
print(var)      #prints out True or False
var_2 = "Godfather" in all_movies
print(var)

for movie in all_movies:
    print(movie)

#add one item to the end of the list
all_movies.append("Godfather")

#add multiple items to the end of the list via another list
all_movies.extend(["Moana", "Pineapple Express", "Mulan"])

#add to specific index
all_movies.insert(1, "Inception")

#change item in a list
all_movies[0] = "New Movie"

#remove everything from the list
all_movies.clear()

#remove item in the list and returns it (can make a new variable), default is last item unless index defined
var = all_movies.pop()
all_movies.pop()
all_movies.pop(2)

#create new list and make nested list
fav_stuff = ["Movies", "Food", "Sport"]
fav_stuff = [["Interstella", "Submarine", "Roma"], ["Bread", "Cheese", "Milk"], ["Netball", "Running", "Tennis"]]
#fist index is for list number then index of that list
fav_stuff[0][1]
print(fav_stuff[0][1])

#loop over lists
food_list = ["pizza", "toast", "choc"]
i = 0

#example1
while i < len(food_list):
    print(food_list[i])
    i += 1

#example2
for food in food_list:
    print(food)

#check if something is in a list
if "pizza" in food_list:
    print("Pizza is in the list!")
else:
    print("Pizza is not in the list")

test_list1 = [7]*5  #print 7 five times over into a list

#CASTING to a list
string = "Hello world!"
string_list = list(string)

#range
num_till_10 = list(range(0,11))
print(num_till_10)

file = open("input.txt", "r")
lines = file.readlines()
for line in lines:
    temp = line.strip()     #removes any empty spaces at end of the line
    temp = line.split(', ') #split into list at the commas
    print(temp)         #prints each line as a whole list

for line in lines:
    temp = line.strip()
    temp = line.split()
    print(temp)  #prints each word as item in a list on seperate line for each sentence

for line in lines:
    temp = line.strip()
    temp = line.split()
    print(temp[0])      #prints first word of each list, index 0

###LOGAN LECTURE
tasks_read = open("data.txt", "r")
data = tasks_read.readlines()       #takes every line and places it into a long list

print(data)         #returns everything inside a singular list, each line is an item and \n denotes the new line

for line in data:       #item in the list reflects a line in the text file
    print(line)

for line in data:
    split_data = line.split(", ")       #as each word/variable (on same line) is split by a , in the txt file (or could be space " ")
    output = "-------------\n"
    print(split_data)

for line in data:
    split_data = line.split(", ")       #as each word/variable is split by a , in the txt file (or could be space " ")
    output = "-------------\n"          #output rather than print as create one variable we can print
    output += '\n'
    output += f"Assigned to: {split_data[0]}\n"        #would be better practice to name variables, for readability
    output += f"Task: {split_data[1]}\n"
    output += f"Description: {split_data[2]}\n"
  #  output += ALL OTHER SECtIONS
    output += '\n'
    output = "-------------\n"
    print(output

#pos - position (i.e. print(pos)) - CAPSTONE 2
for pos, line in enumerate(data, 1):        #pos and line are variables (enumerate uses this as has position to count (data is the range) & line is from text file) and start at 1
    split_data = line.split(", ")
    output = "-------[{pos}]------\n"
    output += '\n'
    output += f"Assigned to: {split_data[0]}\n"
    output += f"Task: {split_data[1]}\n"
    output += f"Description: {split_data[2]}\n"
  #  output += ALL OTHER SECTIONS
    output += '\n'
    output = "-------------\n"
    print(output)

#select input, make sure we have no errors
while True:
    task_choice = int(input("Please select a task number to edit: "))-1  #minus 1 to account for starting at 1 above

    if task_choice < 0 or task_choice > len(data): #length counts from 1
        print("You have selected an invalid option, try again.")
        continue
    #print index if exists, return choice
    edit_data = data[task_choice]        #gets index of user choice
    break

#EDIT INPUT
while True:
    output = f"------[SELECT AN OPTION]------\n"
    output += "1 - Edit due date \n"
    output += "2 - Mark as completed \n"
    output += "-------------\n"

    choice = int(input(output))

    if choice <= 0 or choice >= 3:
        print("You have selected an invaldi option, try again")
        continue

    if choice == 1:
        print("")   #TODO - I need to do this thing...
    elif choice == 2:
        split_date = edit_data.split(", ") #block warning on edit_data incase it is undefined, but we have error handled above
        split_date[-1] = 'Yes\n'        #want to change element -1, last one
        new_data = ", ",join(split_date)
        data[task_choice] = new_data


    tasks_write = open("data.txt", "w")  # WRITE after read otherwise will overwrrite itself (or could open as r+ - NOT a+ as would duplicate data not rewrite)
    for line in data:
        tasks_write.write(line)

    break

print("you have finished the task")
tasks_write.close()
tasks_read.close()


#files play-around
names = []
ages = []

with open("student.txt", "r") as student_file:
    print(student_file.readlines())

with open("student.txt", "r") as student_file:
    data = student_file.readlines()
    print(data)         #can see the extra line caused from new line in txt file
    for line in data:
        print(line)         #adds extra empty lines due to \n in list
        print(line.strip("\n"))     #removes new line character and empty lines returned
        print(line.strip("\n").split(", "))     #removes new line character and empty lines returned
    for line in student_file:
        name, age = line.strip("\n").split(", ")
        print(name, age)
    for line in student_file:
        name, age = line.strip("\n").split(", ")
        names.append(name)
        ages.append(age)

#DO NOT SORT if rely on the index (i.e. authentification)
names.sort()        #sort in alphabetical order
names.sort(reverse = True)     #sort backwards of alphabetical order
names.reverse()             #reverses order of the list

#check index of lists
#AUTHENTIFICATION
n = input("Enter a name: ")
while not n in names:
    n = input("Invalid name, try again.\nEnter a name: ")
post = names.index(n)
print(ages[post])

a = input(f"Enter the age of {n}")
while a != ages[post]:
    a = input(f"Wrong age, please enter age of {n}")

print(names)
print(ages)                 #verification, check if name in list and if in there look for age at same index


#MORE examples
contents = ""
f = open("example.txt", "r+")
for line in f:
    contents += line        #variable contains content of txt file
print(contents)
#-----------------
#CAPSTONE2
#multiple lists!!
user_file = open("login.txt", "r+")
username_list = []
password_list = []
for line in user_file:
    user, psw = line.strip("\n").split(", ")
    username_list.append(user)
    password_list.append(psw)
user_file.close()

username = input("Username: ")

while not username in username_list:
    print("Invalid user name")
    username = input("Username: ")

position = username_list.index(username)
password = input("Password: ")

while password != password_list[position]:
    password = input("Password: ")

print(f"Welcome: {username}")
#----------------
#randomness
import random
number = 5
random_number = random.randint(0, 2)
if (random_number == 1):
    number += 25
number += 5
print(number)
