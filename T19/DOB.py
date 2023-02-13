#programe to read txt file and print names and birthdates in two seperate & headed lists

read_dob = open("DOB.txt", "r")     #open the file in read mode
dob_data = read_dob.readlines()     #create a variable of file data

#code for making heading bold and body of list normal
BOLD = '\033[1m'
NON_BOLD = '\033[0m'

#print name header in bold
print(f"{BOLD}Name{NON_BOLD}")

#for every line in text data variable, remove the new line notation & split by the spaces between words to create a list
for line in dob_data:
    split_data = line.strip("\n").split(" ")
    name = split_data[0] + " " + split_data[1]          #name will contain first and last names
    print(name)

#print birthdate header in bold
print(f"\n{BOLD}Birthdate{NON_BOLD}")

#for every line in text data variable, remove the new line notation & split by the spaces between words to create a list
for line in dob_data:
    split_data = line.strip("\n").split(" ")
    birthdate = split_data[2] + " " + split_data[3] + " " + split_data[4]       #birthdare will contain date, month and year
    print(birthdate)

read_dob.close()
