age = int(input("How old are you?")) #int user input for age
if age >= 18:
    print("You are old enough!")
elif age < 18 and age > 16:
    print("Almost there")
else:
    print("You're just too young!")