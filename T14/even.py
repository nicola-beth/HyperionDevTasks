num = int(input("Please enter a number: "))    #user input for int number
while True:
    for i in range(1, num+1):   #for loop for range 0 to User number(inclusive)
        if i % 2 == 0:       #check if i is even
            print(i)        #print all numbers
    break                   #break the loop to exit