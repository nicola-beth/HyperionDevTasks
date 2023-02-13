#programe to change even characters in string to captial

string = "My name is Nicola"        #define starting string which you want to edit
new_string = ""                     #define empty new string which will contain edited version
#for loop to iterate through same number of times as number of chaacters in string
for i in range(len(string)):
    if i % 2 == 0:      #calc if i is devisable by 2 (i.e. even)
        new_string = new_string + string[i].upper()     #add to new string, what has been written plus new character in upper case
    else:
        new_string = new_string + string[i].lower()     #add to new string, what has been written plus new character in lower case
print(new_string)