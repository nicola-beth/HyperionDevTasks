num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter another number: "))
operator = input("Enter an operator (x, -, * or /): ")

try:
    if operator == "+":
        ans = num_1 + num_2
        print(ans)
        write_task = open("equations.txt", "a")
        write_task.write(f"{str(num_1)} {operator} {str(num_2)} = {ans}")
        write_task.close()
    elif operator == "-":
        ans = num_1 - num_2
        print(ans)
        equation = (f"{str(num_1)} {operator} {str(num_2)} = {ans}")
        print(equation)
    elif operator == "*":
        ans = num_1 * num_2
        print(ans)
        equation = (f"{str(num_1)} {operator} {str(num_2)} = {ans}")
        print(equation)
    elif operator == "/":
        ans = num_1 / num_2
        print(ans)
        equation = (f"{str(num_1)} {operator} {str(num_2)} = {ans}")
        print(equation)
    else:
        print("Invalid operator")
except Exception as error:
    print(f"Ops something went wrong. See error: {error}")
