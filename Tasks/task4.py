user_number = int(input("Enter an integer: ")) #user input to enter number

if user_number % 2 == 0 and user_number % 5 == 0: #calc if remainder after dividing by 2 and 5
    print("Your number is divisible by 2 and 5!")
elif user_number % 2 == 0 or user_number % 5 == 0: #calc if remainder after dividing by 2 or 5
    print("Your number is divisible by 2 or 5.")
else:
    print("Your number is not divisible by 2 or 5.")