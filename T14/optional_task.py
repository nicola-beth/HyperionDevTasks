#Loop to ask for user input for number over 100, if even multiple by 2 , if odd multiply by 3
while True:
    user_num = int(input("Enter a number less than or equal to 100: "))
    #check to see if user number is less than or equal to 100
    if user_num <= 100:
        #check to see if user number if even
        if user_num % 2 == 0:
            calc = user_num * 2 #calc to multiple user number by 2
            print(calc)
        #if user number not even, it is odd
        else:
            calc = user_num * 3 #calc to multiple user number by 3
            print(calc)
    #if number greater 100, ask for another number
    else:
        user_num = int(input("Please enter a number (or -1 to exit): "))