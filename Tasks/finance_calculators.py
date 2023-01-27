import math
#detirmine if interest is on cash investment or house loan
#if cash investment get user input for value , interest rate, length of time
#calcualate how much the cash investment will be worth
#if hosue loan get user input for house value, interest rate, length of time
#calculate the loans monthly repayments

#get user input for whether they want to calculate an interest on an investment or bond installments
print("investment - to calculate the amount of interest you'll earn on your investment\nbond\t   - to calculate the amount you'll have to pay on a home loan")
interest_reason = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
interest_total = 0
monthly_bond_repayment = 0

while True:
    #investment section - user input for cash amount, ineterst rate and investment length (in years)
    if interest_reason == "investment":
        deposit_amount = int(input("How much money are you depositing?: "))
        interest_rate = int(input("What is the interest rate (as a %)?: "))
        investment_years = int(input("How many years are you planning to invest?: "))
        interest = input("Would you like simple or compound interest?: ")
        #checks type of interest User selects and calculates total interest based off selection
        if interest == "simple":
            interest_total = deposit_amount*(1 + ((interest_rate/100) * investment_years))  #calculation for simple investment
            interest_total = round(interest_total, 2)           #round figure to 2 d.p
            print(f"Your investment will be worth: £{interest_total}")
        elif interest == "compound":
            interest_total = deposit_amount*(1 + (interest_rate/100))**investment_years   #calculation for simple investment
            interest_total = round(interest_total, 2)               #round to 2 d.p
            print(f"Your investment will be worth: £{interest_total}")
        #incase user input does not fit what expect, ask them to try again
        else:
            print ("Invalid input, try again")
            interest_reason = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()
        break
    #bond section - user inout for house value, interest rate and how many months will take to repay
    elif interest_reason == "bond":
        house_value = int(input("What is the current value of the house?: "))
        interest_rate = int(input("What is the interest rate (as a %)?: "))
        investment_months = int(input("How many months will you take to repay the bond?: "))
        monthly_interest_rate = (interest_rate / 100) / 12      #calculate interest per month
        monthly_bond_repayment = ((monthly_interest_rate) * house_value) / (1 - (1 + monthly_interest_rate) ** (-investment_months)) #calculation for monthly bond repayments
        monthly_bond_repayment = round(monthly_bond_repayment, 2)               #round figure to 2 d.p.
        print(f"Your monthly bond repayments will be: £{monthly_bond_repayment}")
        break
    #incase user input does not fit what expect, ask User again
    else:
        print("Invalid entry, please retry")
        interest_reason = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

