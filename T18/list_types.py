#create list of friends names and another list of friends ages - print first and last friend and number of friends names entered

friends_names =[]   #empty list to append to
i = 0               #counter
for i in range(3):  #go through loop 3 times
    name = input("Enter name of friend: ")  #user input for friends name
    friends_names.append(name)          #append input to friends_names list
    i += 1          #add to counter

print(f'Friend named first was {friends_names[0]}') #print first name entered
print(f'Friend named last was {friends_names[-1]}') #print last name entered
print(f'Total number of friends named: {len(friends_names)}')   #print total number of names entered

friends_ages = []   #empty list to append to
i = 0               #counter
for i in range(3): #go through loop 3 times
    age = input("Enter age of friend: ")    #user input for friends age
    friends_ages.append(age)        #append input to friends_ages list
    i += 1          #add to counter
