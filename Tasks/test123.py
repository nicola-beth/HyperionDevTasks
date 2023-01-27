# finance_calculator

import math

print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan\n")

user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if user_input == "investment":

    deposit = float(input("Please enter the amount you would like to deposit: "))
    interest_rate = float(input("Please enter your interest rate: ")) / 100
    year = int(input("Please input the number of years you would like to invest"))
    interest = input(
        "Please input either 'simple' or 'compound' depending on the type of interest you would like: ").lower()

    if interest == "simple":
        total_amount = deposit * (1 + interest_rate * year)
        print(f"The amount you will receive is {total_amount}")


    elif interest == "compound":
        total_amount = round(deposit * math.pow((1 + interest_rate), year), 2)
        print(f"The amount you will receive is {total_amount}")


    else:
        print("You have not entered a valid interest type")


elif user_input == "bond":
    house_value = float(input("Please enter the present value of your house"))
    interest_rate = (float(input("Please enter your interest rate: ")) / 100)
    final_interest = interest_rate / 12
    months = int(input("Please enter the number of months you plan to take to repay the bond"))

    repayment = round((final_interest * house_value) / (1 - (1 + final_interest) ** (-months)), 2)
    print(f"You will have to repay {repayment} each month")


else:
    print("You have not entered a valid option from the menu")