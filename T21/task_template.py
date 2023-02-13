#=====importing libraries===========
from datetime import date

#====Login Section====
read_user = open("user.txt", "r")
user_data = read_user.readlines()
print(user_data)

user_credentials = []

for line in user_data:
    split_data = line.strip("\n").split(", ")
    print(split_data)
    user_credentials.append(split_data)
    print(user_credentials)

counter = 0

while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    for i in range(len(user_credentials)):
        if username == user_credentials[i][0] and password == user_credentials[i][1]:
            print("You have successfully logged in.")
            break

        elif username != user_credentials[i][0] or password != user_credentials[i][1]:
            counter += 1
            if counter >= len(user_credentials):
                print("Incorrect credentials, please try again.")
                continue

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        new_username = input("Enter a username: ")
        for i in range(len(user_credentials)):
            if username == user_credentials[i][0]:
                print("This user name is already taken, please try again.")
                new_username = input("Enter a username: ")
                contine
            else:
                while True:
                    new_password = input(print("Enter a password: "))
                    confirm_password = input(print("Confirm password"))
                    if new_password == confirm_password:
                        write_user = open("user.txt", "w")
                        write_user.write(f"{new_username}, {new_password}")
                        print("You have successfully registered a user.")
                        break
                    else:
                        print("Passwords do not match, try again.")
        write_user.close()


        # pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

    elif menu == 'a':
        new_task_username = input("Enter username task assigned to: ")
        new_task_title = input("Enter title of the task: ")
        new_task_description = input("Enter a description of the task: ")
        new_task_current_date = date.today().strftime('%d %b %Y')
        new_task_due_date = input("Enter task due date: ")
        new_task_complete = "No"
        write_task = open("tasks.txt.txt", "w")
        write_user.write(f"{new_task_username}, {new_task_title}, {new_task_description}, {new_task_current_date}, {new_task_due_date}, {new_task_complete}\n")
        write_task.close()
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

    elif menu == 'va':
        read_tasks = open("tasks.txt", "r")
        tasks_data = read_tasks.readlines()
        for line in tasks_data:
            split_data = line.strip("\n").split(", ")
            print("------------------------------------------------------")
            print(f"Task: \t\t\t {split_data[1]}")
            print(f"Assigned to: \t {split_data[0]}")
            print(f"Date assigned: \t {split_data[3]}")
            print(f"Due date: \t\t {split_data[4]}")
            print(f"Task complete?:  {split_data[5]}")
            print(f"Task description: \n \t {split_data[2]}")
            print("------------------------------------------------------")

        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        if username == split_data[0]:       #will it iterate through whole list?? no loop
            print("------------------------------------------------------")
            print(f"Task: \t\t\t {split_data[1]}")
            print(f"Assigned to: \t {split_data[0]}")
            print(f"Date assigned: \t {split_data[3]}")
            print(f"Due date: \t\t {split_data[4]}")
            print(f"Task complete?:  {split_data[5]}")
            print(f"Task description: \n \t {split_data[2]}")
            print("------------------------------------------------------")
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")