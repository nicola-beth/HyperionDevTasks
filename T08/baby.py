year = 2022
user_year = int(input("What year were you born?")) #request user birth year
if year - user_year >= 18: #check in age is greater than or equal to 18
    print("Congrats you are old enough")
else:
    print("You are too young")