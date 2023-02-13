num = int(input("Please enter a number: "))
num_check = num % 2 #use modulus to see if num is divisible by 2
if num_check != 0: #not equal to 0, num is odd
    print("Your number is odd!")
else:
    print("Your number is even!")