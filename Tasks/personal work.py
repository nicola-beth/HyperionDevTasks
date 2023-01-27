#understanding the below with multiple variables in line & key/values in dictionaries
#practice functions online (uncderstand where to put variables & when to return)
#finish capston 2, start capstone 3
#look @ build your brand

usernames = []
passwords = []

for line in user_data:
    username, password = line.strip("\n").split(", ")
    usernames.append(username)
    passwords.append(password)
    print(usernames)
    print(passwords)


def print_values_of(dictionary, keys):
   for key, value in dictionary.items():  #for loop through all keys and values in dictionary
       if key in keys:                #if statement to check if k is in keys list
        print(value)                #print value
