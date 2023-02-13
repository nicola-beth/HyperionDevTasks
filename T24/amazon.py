#import math library
import math

#open input file and assign contents to a variable
read_file = open("input.txt", "r", encoding='utf-8-sig')
lines = read_file.readlines()
write_file = open("output.txt", "a")


#create empty lists
operations = []
numbers = []
new_numbers = []
final_num_list = []

#iterate through lines in file and split operator and numbers and append to appropiate list
for item in lines:
    operation, number = item.strip("\n").split(":")  # removes any empty spaces at end of the line
    operations.append(operation)
    numbers.append(number)

#split string of numbers into list
for row in numbers:
    num_list = row.split(",")
    new_numbers.append(num_list)

#cast string numbers to ints
for num in new_numbers:
    final_num_list.append(list(map(int, num)))

#function to calculate min number in list based off index of operator & append to output file
def min_calc(ops_list, num_list):
    for i in range(len(ops_list)):
        if operations[i] == "min":
            index = i
            for list in num_list:
                min_num = min(num_list[index])
    write_file.write(f'The {operations[index]} number of {final_num_list[index]} is {min_num}\n')
    return min_num

#function to calculate max number in list based off index of operator & append to output file
def max_calc(ops_list, num_list):
    for i in range(len(ops_list)):
        if operations[i] == "max":
            index = i
            for list in num_list:
                max_num = max(num_list[index])
    write_file.write(f'The {operations[index]} number of {final_num_list[index]} is {max_num}\n')
    return max_num

#function to calculate ave number in list based off index of operator & append to output file
def ave_calc(ops_list, num_list):
    for i in range(len(ops_list)):
        if operations[i] == "avg":
            index = i
            for list in num_list:
                length = len(num_list[index])
                sum_nums = sum(num_list[index])
                ave_num = sum_nums / length
    write_file.write(f'The {operations[index]} number of {final_num_list[index]} is {ave_num}\n')
    return ave_num

#call functions with arguments
min_calc(operations, final_num_list)
max_calc(operations, final_num_list)
ave_calc(operations, final_num_list)

#close read and write files
read_file.close()
write_file.close()


