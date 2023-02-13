#calculator programe
#function to add two numbers
def add_num(num1, num2):
    add_calc = num1 + num2
    print(add_calc)

#function to subtract two numbers
def subtract_num(num1, num2):
    subtract_calc = num1 - num2
    print(subtract_calc)

#function to multiply two numbers
def multiply_num(num1, num2):
    multiply_calc = num1 * num2
    print(multiply_calc)

#function to divide two numbers
def divide_num(num1, num2):
    divide_calc = num1 / num2
    print(divide_calc)

#user input for two numbers and calc they would like to perform on them
user_num1 = int(input("Enter a number: "))
user_num2 = int(input("Enter another number: "))
user_calc = input("Which calculation would you like to perform on your numbers?:\nOption 1 - add\nOption 2 - subtract\nOption 3 - multiply\nOption 4 - divide\n")

#if statement to detirmine which function to run & pass in user inputs as the number arguments
if user_calc == "add":
    add_num(user_num2, user_num2)
elif user_calc == "subtract":
    subtract_num(user_num1, user_num2)
elif user_calc == "multiply":
    multiply_num(user_num1, user_num2)
elif user_calc == "divide":
    divide_num(user_num1, user_num2)