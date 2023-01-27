#programe to get user to input number and then calc the average of these
#total variable to add user numbers to
#counter variable to count number of user entries
#average calculated by total divided by counter

user_num = int(input("Please enter a number (or -1 to exit): "))
total = 0
counter = 0

#while loop to see if user enters number which is not -1, perform in calculations
while user_num != -1:
    total += user_num       #add user number to total
    counter += 1            #add to counter
    user_num = int(input("Please enter a number (or -1 to exit): "))

    #if user enters -1, break loop, calculate the average and return figure
    if user_num == -1:
        total_ave = total / counter             #average calcualtion is sum of all inputs devided by number of inputs
        print(f'The average of the inputted numbers is {total_ave}.')
        break