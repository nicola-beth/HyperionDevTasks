import math
# Lecture 1
#Do Pseudo code on notes in numbered steps
#Write steps down before writing code in a text file
# 1. Check if user wants cup of tea
# 2. What cup of tea do they want
    # If yes, boil the kettle
    # If yes, boil the kettle

#read user input for username
#read user input for password
#if username and password match
#log user in

# Lecture 2

print("Hello World")

name = input("What is your name?")
print("Your name is", name)
print(f"Your name is {name}")

#Lecture 3
name = "Nicola"
surname = "Brown"
full_name = name + " " + surname
full_name = f"{name} {surname}"
print(f"First name: {name}. Last name: {surname}")
print("Nicola/'s cat")

name = nicola
print(name)
print(name.capitalized())

name = nicola
name = nicola.upper()
print(len(name))

sentence = "Nicola is from Woodford Green"
split_data = sentence.split(" ")
print(split_data) #splits into a list
print("|".join(split_data)) #makes a string again
print(sentence.replace(" ","|")) #this does the same as the line above
print(sentence.replace("a", "A").replace("d", "DDDD"))

string = "Hello Nicola"
string_idx = string[3]
print(string_idx)
string_idx = string[3:7]
print(string_idx)


name = "Nicola \nBrown" #puts name and surname of seperate lines
print(name)

txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(",.grt") #Remove the leading and trailing characters:
print(x)

name = "    Nicola     "
print(name)
name2 = name.strip() #removes the spaces
print(name2)

#Lecture4
import math

my_number = 69.69
print(math.floor(my_number)) #roundown
print(math.ceil(my_number)) #roundup
help(print(math.floor(my_number)))

num_1 = 8 #int
num_2 = "8" #string
num_3 = 8.0 #float
print(float(num_1)) #convert int to flaot
print(str(num_1)) #convert int to string

num_1 = 8
num_2 = 7
placeholder = 0 #logical operator allows us to change the above variables, set to 0 as a default int number but can change later

placeholder = num_1
num_1 = num_2
num_2 = placeholder

number_11 = 45
number_11 += 5 #add 5 to number_11
print(number_11)

nicola_number = input("Nicola, what is you number?")
print(f"Nicola chose to enter: {nicola_number}")

#Lecture5
print("line1 \n line2") #new line
print("name: \t nicola") #tab space

print("my name is\n\n")
print("Nicola")

my_string = "Nicola Elizabeth Jane Brown"
print(my_string[0:10:2]) #slice[start:stop:step], step will default to 1 if not defined
#or can do via slice
s1 = slice(0,10,2)
print(my_string[s1])

#docstring - a string used to document a Python module, class, function or method
"""

"""

#multi-line strings, triple quoation marks perserves the formatting of the string
print("""my
sentence
on
different
lines""")

#Todo -make sure you add.. (can then reference your to do list!)

greeting = "Merry Christmas"
print(greeting[0] + greeting[1] + greeting [2] + greeting[3] + greeting[4]) #start with 0, square bracket denotes the index
print(len(greeting)) #length of the string
print(greeting[0:4])

a_string="Hello World!"
print(a_string.upper()) #prints in upper case
print(a_string.replace("o", "@"))

b_string = "%%%%%%Hey%you!%%%%%%%"
print(b_string.strip("%")) #strips string of character at end/begininng of word (not in the middle), good ro remove unwnated spaces at end of words

c_string = "Dear Mum, \nHappy Birthday! \n\tLove Nicola" #\ s an escape character
print(c_string)

sent = input("Type out a sentence: ")
words = sent.split(" ") #splits string "sent" into a list
print(words)
if len(words) < 5: #counts number of list items
    print("Too few words")
else:
    print("valid setence!")


    """"
    Three "'s becomes a comment unless in a variable/input/print
    """

num = 23
name = input("What is your name?")

if num == 23:
    if name == "Nicola":
    print ("Name & age as expected!")