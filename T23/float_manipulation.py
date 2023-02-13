#apply math libray functions to list of numbers
#inport math library so we can use its in-built functions
import math
user_numbers = []       #empty list to add user inputs to

#ask user for 10 number inputs
for i in range(10):
    num = float(input("Enter a number (decimal or whole): "))
    user_numbers.append(num)

#cum all numbers in the list
sum_numbers = print(sum(user_numbers))

#return index of max number in the list
max_index = print(user_numbers.index(max(user_numbers)))

#return index of min number in the list
min_index = print(user_numbers.index(min(user_numbers)))

#calc average of numbers in list to 2 d.p. by dividing sum of all numbers by lenght of list
total_no = len(user_numbers)
sum_numbers = sum(user_numbers)
rounded_ave = print(round((sum_numbers/total_no), 2))

#calc medium by taking floor of middle number if list length is even and calc average of two middle numbers if list length is odd
total_no = len(user_numbers)
user_numbers.sort()

if total_no % 2 == 0:
    medium1 = user_numbers[total_no//2]     #index of floored number
    medium2 = user_numbers[total_no//2 - 1]
    medium = (medium1 + medium2) / 2
else:
    medium = user_numbers[total_no//2]
print(medium)