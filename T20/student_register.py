#programe to requets number of students in exam and their student ID's, print ID's and dotted l ine to sign to txt file

total_students = int(input("How many students are registering?: "))     #user input for total number of students sitting exam
write_file = open("reg_form.txt", "w")      #write to file

#iterate through same number as total_students to ask for their id's, print to txt file
for number in range(total_students):
    student_id = input("Enter Student ID: ")
    write_file.write(f"{student_id}: _________________\n")

write_file.close()

