#=====importing libraries===========
#import date time library needed for writing new task
from datetime import date

#====Login Section====
#read user file and put data into variable
read_user = open("user.txt", "r")
user_data = read_user.readlines()

usernames = []
passwords = []

#iterate through all lines in the data variable to split line by "," to username and password variables & append to empty lists above
for line in user_data:
    username, password = line.strip("\n").split(", ")
    usernames.append(username)
    passwords.append(password)

#while loop to take User input for username and password and check if relates to registered user
while True:
    username = input("Enter your username: ")
    if username in usernames:          #validate if username already in list taken from user.txt
        password = input("Enter your password: ")
        username_index = usernames.index(username)      #get username index to validate against the password
        if password == passwords[username_index]:       #validate username matches appropiate password (using list inedex)
            print("You are logged in!")
            break
        else:       #if password does not match username
            print("Incorrect password, please try again")
    else:
        print("Incorrect username, please try again")   #if enter unregistered username

while True:
    #presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    if username == "admin":
        menu = input('''Select one of the following Options below:
    r - Registerading a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    s - display statistics
    e - Exit
    : ''').lower()
    else:
        menu = input('''Select one of the following Options below:
        r - Registering a user
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()

#if statement when user wants to register a new user to user.txt
    if menu == 'r' and username == "admin": #validation check that is admin user signed in: mentor told me it had to be the admin user to register a new user
        new_username = input("Enter a new username: ")
        #interate through usernames to see if the new user already exists
        for i in range(len(usernames)):
            if new_username == usernames[i]:
                print("This user name is already taken, please try again.")
                new_username = input("Enter a username: ")
            else:
                #loop to ask user to enter password twice to ensure they equal eachother, if so append to user.txt file username & password
                while True:
                    new_password = input("Enter a password: ")
                    confirm_password = input("Confirm password: ")
                    if new_password != confirm_password:
                        print("Passwords do not match, try again.")     #otherwise ask User to try again
                    else:
                        write_user = open("user.txt", "a")
                        write_user.write(f"\n{new_username}, {new_password}")
                        write_user.close()
                        print("You have successfully registered a user.")
                        break
                break
                #break claus if passwords match
        break
#elif statement when user wants to add a new task to task.txt & append to task file
    elif menu == 'a':
        #user input for all task requirements
        new_task_username = input("Enter username task assigned to: ")
        new_task_title = input("Enter title of the task: ")
        new_task_description = input("Enter a description of the task: ")
        new_task_current_date = date.today().strftime('%d %b %Y')  #use datetime library to reference curennt date
        new_task_due_date = input("Enter task due date: ")
        new_task_complete = "No"
        write_task = open("tasks.txt", "a")
        write_task.write(f"\n{new_task_username}, {new_task_title}, {new_task_description}, {new_task_current_date}, {new_task_due_date}, {new_task_complete}")
        write_task.close()
        break
# elif statement when user wants to view all existing tasks in task.txt, displayed in an easy to read way
    elif menu == 'va':
        read_tasks = open("tasks.txt", "r")
        tasks_data = read_tasks.readlines()
        #for every line in task file, split by "," and print against heading to clearly display info
        for line in tasks_data:
            split_data = line.strip("\n").split(", ")
            print("------------------------------------------------------")
            print(f"Task: \t\t\t {split_data[1]}")
            print(f"Assigned to: \t {split_data[0]}")
            print(f"Date assigned: \t {split_data[3]}")
            print(f"Due date: \t\t {split_data[4]}")
            print(f"Task complete?:  {split_data[5]}")
            print(f"Task description: \n \t {split_data[2]}")
        read_tasks.close()
        break
# elif statement when user wants to view all tasks assigned to their user in task.txt, displayed in an easy to read way
    elif menu == 'vm':
        read_tasks = open("tasks.txt", "r")
        tasks_data = read_tasks.readlines()
        #for every line in task file, split by "," and print against heading to clearly display info
        for line in tasks_data:
            split_data = line.strip("\n").split(", ")
            if username == split_data[0]:      #only return
                for i in range(len(tasks_data)):
                    print(f"-------------------------[Task number: {i + 1}]---------------------------")
                    print(f"Task: \t\t\t {split_data[1]}")
                    print(f"Assigned to: \t {split_data[0]}")
                    print(f"Date assigned: \t {split_data[3]}")
                    print(f"Due date: \t\t {split_data[4]}")
                    print(f"Task complete?:  {split_data[5]}")
                    print(f"Task description: \n \t {split_data[2]}")
                read_tasks.close()
        break
# elif statement for when admin user wants to display statistics
    elif menu == "s":
        read_tasks = open("tasks.txt", "r")
        tasks_data = read_tasks.readlines()
        sum_users = len(usernames)      #total number of users will be length of user list
        sum_tasks = len(tasks_data)     #total number of tasks will be number of lines read from tasks.txt file
        print(f"Total number of users: {sum_users}")
        print(f"Total number of tasks: {sum_tasks}")
        break
        read_tasks.close()
    #elif statement for when user wants to exit the programe
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
#else, do not recognise option chosen (error handling)
    else:
        print("You have made a wrong choice, Please Try again")