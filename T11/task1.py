num1 = float(input("Enter a number: ")) #float input for num1
num2 = float(input("Enter a number: ")) #float input for num2
num3 = float(input("Enter a number: ")) #float input for num3

if num1 > num2: #calc if num1 greater than nu
    print(f"Largest of first two numbers is {num1}")
else:
    print(f"Largest of first two numbers is {num2}")

if num1 % 2 == 0: #calc if num1 is divisible by 2
    print("Number 1 is even")
else:
    print("Number 1 is odd")

if num1 > num2 and num2 > num3: 
    print(f"Largest > Smallest: {num1}, {num2}, {num3}.")
elif num1 > num2 and num3 > num2:
    print(f"Largest > Smallest: {num1}, {num3}, {num2}.")
elif num1 > num2 and num3 > num1:
    print(f"Largest > Smallest: {num3}, {num1}, {num2}.")
elif num3 > num2 and num2 > num1:
    print(f"Largest > Smallest: {num3}, {num2}, {num1}.")
elif num2 > num3 and num3 > num1:
    print(f"Largest > Smallest: {num2}, {num3}, {num1}.")
else:
    print(f"Largest > Smallest: {num2}, {num1}, {num3}.")