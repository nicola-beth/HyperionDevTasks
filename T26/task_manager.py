#=====importing libraries===========
#import date time library needed for writing new task
import datetime

#=======Global veriables ======
user_dict = {}

#=====defining functions===========
#function to register a new user to user.txt
def reg_user():
    new_username = input("Enter a new username: ")
    #interate through usernames to see if the new user already exists
    while new_username in user_dict:
        print("Username already exists")
        new_username = input("Enter a new username: ")
    while new_username not in user_dict:
        new_password = input("Enter a password: ")
        confirm_password = input("Confirm password: ")
        if new_password == confirm_password:
            write_user = open("user.txt", "a")
            write_user.write(f"\n{new_username}, {new_password}")
            write_user.close()
            print("You have successfully registered a user.")
            break
        else:       #break claus if passwords do not match, ask User to reenter
            print("Passwords do not match, try again.")


#function to add a new task to task.txt & append to task file
def add_task():
    #user input for all task requirements
    new_task_username = input("Enter username task assigned to: ")
    new_task_title = input("Enter title of the task: ")
    new_task_description = input("Enter a description of the task: ")
    new_task_current_date = datetime.datetime.today().strftime('%d %b %Y')  #use datetime library to reference current date
    new_task_due_date = input("Enter task due date (17 Jan 2023)): ")
    new_task_complete = "No"
    write_task = open("tasks.txt", "a")
    write_task.write(f"\n{new_task_username}, {new_task_title}, {new_task_description}, {new_task_current_date}, {new_task_due_date}, {new_task_complete}")
    write_task.close()
    print("You have succesfully added a task.")
#
#function to view all existing tasks in task.txt, displayed in an easy to read way
def view_all():
    read_tasks = open("tasks.txt", "r")
    tasks_data = read_tasks.readlines()
    tasks_dict = {}
    #for every line in task file, split by "," and print against heading to clearly display info
    for count, task_info in enumerate(tasks_data, 1):
        tasks_dict[count] = task_info.strip("\n").split(", ")
        for count, task_info in tasks_dict.items():
            print("------------------------------------------------------")
            print(f"Task: \t\t\t {tasks_dict[count][1]}")
            print(f"Assigned to: \t {tasks_dict[count][0]}")
            print(f"Date assigned: \t {tasks_dict[count][3]}")
            print(f"Due date: \t\t {tasks_dict[count][4]}")
            print(f"Task complete?:  {tasks_dict[count][5]}")
            print(f"Task description: \n \t {tasks_dict[count][2]}")
        read_tasks.close()

# # function to view all tasks assigned to signed in user in task.txt, displayed in an easy to read way
def view_mine():
    read_tasks = open("tasks.txt", "r")
    tasks_data = read_tasks.readlines()
    print(tasks_data)
    tasks_dict = {}
    #for every line in task file, split by "," and print against heading to clearly display info
    for count, task_info in enumerate(tasks_data, 1):
        tasks_dict[count] = task_info.strip("\n").split(", ")
        # for count, task_info in tasks_dict.values():
        print(tasks_dict)
        if user_name == tasks_dict[count][0]:
            print(f"-------------------------[Task number: {count}]---------------------------")
            print(f"Task: \t\t\t {tasks_dict[count][1]}")
            print(f"Assigned to: \t {tasks_dict[count][0]}")
            print(f"Date assigned: \t {tasks_dict[count][3]}")
            print(f"Due date: \t\t {tasks_dict[count][4]}")
            print(f"Task complete?:  {tasks_dict[count][5]}")
            print(f"Task description: \n \t {tasks_dict[count][2]}")
            print(f"--------------------------------------------------------------------------")
    while True:
        user_task_num = input("Which task could you like to select? (-1 to exit): ")
        if user_task_num != -1:
            task_menu = input('''Select one of the options below
            mc - mark task as complete
            et - edit task
            ''')

            # if task_menu == "mc":
                # for task_info in tasks_data:
                #     if tasks_dict[user_task_num] in task_info:
                #         update_data = task_info.replace("No", "Yes")
                #         write_tasks = open("tasks.txt", "w")
                #         write_tasks.write(update_data)
                # mark_as_completed = tasks_dict[user_task_num][5] == "Yes"
                # update_data = read_task({tasks_dict[user_task_num][5]}, mark_as_completed)
            # elif task_menu == "et":
            #     task_menu_2 = print('''Select one of the options below
            #     at - change assignee username
            #     dd - change due date
            #     ''')
            #     if task_menu_2 == "at":
            #         assigned_to = tasks_dict[user_task_num][0] = input("Enter username of new assignee: ")
            #         update_data = read_task.replace({tasks_dict[user_task_num][0]}, assigned_to)
            #         break
            #     elif task_menu_2 == "dd":
            #         due_date = tasks_dict[user_task_num][4] = input("Enter new due date: ")
            #         update_data = read_task.replace({split_data[4]}, due_date)
            #         break
            #     else:
            #         print("Do not recognise that input, please try again.")
            # write_tasks = open("tasks.txt", "w")
            # write_tasks.write(update_data)
            # read_tasks.close()
            # write_tasks.close()
        # elif user_task_num == -1:
        #     break

# function for when admin user wants to display statistics
def display_stats():
    read_tasks = open("tasks.txt", "r")
    tasks_data = read_tasks.readlines()
    read_users = open("tasks.txt", "r")
    users_data = read_users.readlines()
    sum_users = len(users_data)      #total number of users will be length of user list
    sum_tasks = len(tasks_data)     #total number of tasks will be number of lines read from tasks.txt file
    print(f"Total number of users: {sum_users}")
    print(f"Total number of tasks: {sum_tasks}")
    read_tasks.close()
    read_users.close()

def gen_report():
    read_tasks = open("tasks.txt", "r")
    tasks_data = read_tasks.readlines()
    over_due = 0
    incomplete = 0
    for line in tasks_data:
        split_data = line.strip("\n").split(", ")
        #need to compare two dates (strings needs to be converted to date object)
        if split_data[5].lower() == "no":
            incomplete += 1
    print(incomplete)
    for line in tasks_data:
        split_data = line.strip("\n").split(", ")
        due_date = split_data[-2]
        current_date = split_data[-3]
        if split_data[5].lower() == "no" and due_date < current_date:
            over_due += 1
    print(over_due)
    #list of data points to be added to txt file
    total_task_num = len(tasks_data)
    complete = total_task_num - incomplete
    incomplete = incomplete
    over_due = over_due
    percentage_incomplete = (incomplete / total_task_num) * 100
    percentage_over_due = (over_due / total_task_num) * 100

    print(total_task_num)
    print(complete)
    print(incomplete)
    print(over_due)
    print(percentage_incomplete)
    print(percentage_over_due)

    read_users = open("tasks.txt", "r")
    users_data = read_users.readlines()
    for line in users_data:
        split_data = line.strip("\n").split(", ")

    total_users_num = len(users_data)



    read_tasks.close()
    read_users.close()




#====Login Section====
#read user file and put data into variable
read_user = open("user.txt", "r")
user_data = read_user.readlines()
read_user.close()

#iterate through all lines in the data variable to split line by "," to username and password variables & append to empty lists above
for line in user_data:
    username, password = line.strip("\n").split(", ")
    user_dict[username] = password

#while loop to take User input for username and password and check if relates to registered user
while True:
    user_name = input("Enter your username: ")
    resp = user_dict.get(user_name, "Invalid user")       #set variable for username key, but if key doesnt exist will return "Invalid user"
    if resp != "Invalid user":                            #if value is returned for resp, then user_name exists
        user_pass = input("Enter your password: ")        #ask for password and check if relates to corresponding to key
        if resp == user_pass:
            print(f"Welcome {user_name}")
            break
        else:
            print("Wrong password")
    else:
        print(resp)


while True:
    #presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    if user_name == "admin":
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    gr - generate report
    ds - display statistics
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

    if menu == 'r' and user_name == "admin": #validation check that is admin user signed in: mentor told me it had to be the admin user to register a new user
        reg_user()
        break
    elif menu == 'a':
        add_task()
        break
    elif menu == 'va':
        view_all()
        break
    elif menu == 'vm':
        view_mine()
        break
    elif menu == "gr":
        gen_report()
        break
    elif menu == "ds":
        display_stats()
        break
#elif statement for when user wants to exit the programe
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
#else, do not recognise option chosen (error handling)
    else:
        print("You have made a wrong choice, Please Try again")