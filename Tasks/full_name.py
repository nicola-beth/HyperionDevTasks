full_name = input("What is your full name: ")
name_length = len(full_name)
if name_length == 0:
    print ("You haven't entered anything. Please enter your full name.")
elif name_length < 4:
    print("Please make sure that you have entered your name and surname.")
elif name_length > 25:
    print("Please make sure that you have only entered your full name.")
else:
    print("Thank you for entering your name.")
    print(f'Your full name is {full_name}')