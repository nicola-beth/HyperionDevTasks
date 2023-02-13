full_name = input("What is your full name: ")
name_length = len(full_name) #calculate length of full name inputted
if name_length == 0: #length equal to 0
    print ("You haven't entered anything. Please enter your full name.")
elif name_length < 4: #length less than 4
    print("Please make sure that you have entered your name and surname.")
elif name_length > 25: #length greater than 25
    print("Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")
    print(f'Your full name is {full_name}')