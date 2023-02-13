print("activity 1")
while True:
    for i in range(20,-1, -1):       #starts with negative -20 (not inclusive of -21) and increased to 1 (not includive of 0) in increments of 1
        print(i)
    break
#
print("\nactivity 2")
for i in range (0,21):  #range from 1-20 inclusive
    if i % 2 == 0:      #calc to check if number if even
        print(i)        #only print even number

print("\nactivity 3")
for i in range(6):      #range 1-5 inclusive
    print(i*"*")        #multiple number by string "*"

print("\nactivity 4")
#request user input for two numbers
int_1 = int(input("Enter a number: "))
int_2 = int(input("Enter another number: "))

#GCD = greatest common divisor
GCD = 0

#check which number is smaller for the range later on
if int_1 > int_2:
    small = int_2
else:
    small = int_1

#check for all numbers up until smallest to check if divisiable by that number, as inceases in size the biggest multiple will be returned as GCD
for i in range(1, small + 1):
    if (int_1 % i == 0) and (int_2 % i == 0):
        GCD = i

print(f'The GCD of {int_1} and {int_2} is: {GCD}')