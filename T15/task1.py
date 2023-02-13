#ask user to input a number to calculate times table up to & including 12
multiply_num = int(input("Enter a number you would like to multiply by: "))
calculation = 0     #empty variable to use in multiplcation calculation later

print(f'The {multiply_num} times table is:')

#loop for all numbers 1-12 inclusive, calculate user numner times by 1-12 and print equation
for number in range(1, 13):
    calculation = multiply_num * number
    print(f'{multiply_num} x {number} = {calculation}')
