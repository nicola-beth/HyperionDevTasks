#program to take two number files and sort all numbers from both in ascending order

#read both number files and save data to variables
read_num1 = open("numbers1.txt", "r")
num1_data = read_num1.readlines()
read_num2 = open("numbers2.txt", "r")
num2_data = read_num2.readlines()

#empty list to add all numbers to
all_numbers = []

#loop over all numbers in first file, remove new line characters and split using space between numbers & add each to all numbers list
for num_1 in num1_data:
    split_num1 = num_1.strip("\n").split(" ")
    all_numbers += split_num1

#loop over all numbers in first file, remove new line characters and split using space between numbers  & add each to all numbers list
for num_2 in num2_data:
    split_num2 = num_2.strip("\n").split(" ")
    all_numbers += split_num2

#cast list items to int and sort in ascending order
all_numbers.sort(key=int)

#open file to write to
write_file = open("all_numbers.txt", "w")

#write each number in list to file with new line inbetween
for num in all_numbers:
    write_file.write(f"{num}\n")

read_num1.close()
read_num2.close()
write_file.close()
