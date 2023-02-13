#user input for number
user_num = int(input("Please enter a number: "))

#if number if greater than 10, return users number as many times as its value
for i in range(user_num+1):
    if user_num > 10:
        print(user_num)
    else:
        print("Sorry, too small!")  #if user num < 10