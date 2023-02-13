#programe to store incorrect names in a list, correct name is John

name = input("Enter a name: ").lower()  #user input for name, converted to lower case
incorrect_names = []        #empty list to store incorrect names
#while loop to keep asking for another name unlesss John is entered
while True:
    if name != "john":
        incorrect_names.append(name)    #add incorrect name to list
        name = input("Enter a name: ").lower()  #ask user to input another name
    else:
        break   #if John is entered, break the loop
print(f'Incorrect names: {incorrect_names}')