#programe to display good error handling with try/except
while True:
    choice = input('''Choose from the below:
    c - calculation
    pe - print equations from file
    ''')
    print("")
    if choice == "c":
            #check user enters int for two requested numbers
            try:
                num_1 = int(input("Enter a number: "))
            except Exception as error:
                print(f"This is not a valid number. Error: {error}")
                break
            try:
                num_2 = int(input("Enter another number: "))
            except Exception as error:
                print(f"This is not a valid number. Error: {error}")
                break
            operator = input("Enter an operator (x, -, * or /): ")

        #first try to complete & return the calculation requested by the user and also write this equation to the file
            try:
                if operator == "+":
                    ans = num_1 + num_2
                    print(ans)
                    write_file = open("equations.txt", "a")
                    write_file.write(f"{str(num_1)} {operator} {str(num_2)} = {ans}")
                    write_file.close()
                elif operator == "-":
                    ans = num_1 - num_2
                    print(ans)
                    write_file = open("equations.txt", "a")
                    write_file.write(f"{str(num_1)} {operator} {str(num_2)} = {ans}")
                    write_file.close()
                elif operator == "*":
                    ans = num_1 * num_2
                    print(ans)
                    write_file = open("equations.txt", "a")
                    write_file.write(f"{str(num_1)} {operator} {str(num_2)} = {ans}")
                    write_file.close()
                elif operator == "/":
                    ans = num_1 / num_2
                    print(ans)
                    write_file = open("equations.txt", "a")
                    write_file.write(f"{str(num_1)} {operator} {str(num_2)} = {ans}")
                    write_file.close()
                #error handling for unrecognised operator
                else:
                    print("Invalid operator")
            # return Exception as a variable & print out to user to give context on what went wrong
            except Exception as error:
                print(f"Ops something went wrong. See error: {error}")
            break
    elif choice == "pe":
        while True:
            #try to read the file name provided by user by adding .txt to name
            try:
                file_name = input("Enter name of file: ")
                file_name = file_name + ".txt"
                read_file = open(f"{file_name}", "r")
                file_lines = read_file.readlines()
                for line in file_lines:
                    equation_line = line.strip("\n").split(", ")
                    print(equation_line)
                read_file.close()
                break
            # return Exception as a variable & print out to user to give context on what went wrong
            except Exception as error:
                print(f"Ops something went wrong. See error: {error}")
        break
    else:
        print("Do not recognise choice selection. Try again.")