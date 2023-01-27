while True:
    user_num = int(input("Enter a number less than or equal to 100: "))
    if user_num <= 100:
        if user_num % 2 == 0:
            calc = user_num * 2
            print(calc)
        else:
            calc = user_num * 3
            print(calc)
    else:
        user_num = int(input("Please enter a number (or -1 to exit): "))