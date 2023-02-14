#=====importing libraries===========
#import date time library needed for writing new task
import datetime

#=======Global veriables ======
user_dict = {}

#=====defining functions===========
#function to register a new user to user.txt
def reg_user():
    new_username = input("Enter a new username: ")
    #interate through usernames to see if the new user already exists, if not ask for password
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
    print("You have successfully added a task.")
#
#function to view all existing tasks in task.txt, displayed in an easy to read way (using a dictionary & enumerating through)
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

#function to view all tasks assigned to signed in user in task.txt, displayed in an easy to read way  (using a dictionary & enumerating through)
def view_mine():
    read_tasks = open("tasks.txt", "r")
    tasks_data = read_tasks.readlines()
    print(tasks_data)
    tasks_dict = {}
    #for every line in task file, split by "," and print against heading to clearly display info so user can easily identify task to choose later in function
    for count, task_info in enumerate(tasks_data, 1):
        tasks_dict[count] = task_info.strip("\n").split(", ")
        if user_name == tasks_dict[count][0]:
            print(f"-------------------------[Task number: {count}]---------------------------")
            print(f"Task: \t\t\t {tasks_dict[count][1]}")
            print(f"Assigned to: \t {tasks_dict[count][0]}")
            print(f"Date assigned: \t {tasks_dict[count][3]}")
            print(f"Due date: \t\t {tasks_dict[count][4]}")
            print(f"Task complete?:  {tasks_dict[count][5]}")
            print(f"Task description: \n \t {tasks_dict[count][2]}")
            print(f"--------------------------------------------------------------------------")
    #While loop to ask User if they would like to selected a task which they can then mark as complete or edit
    while True:
        user_task_num = int(input("Which task could you like to select? (-1 to exit): "))
        if user_task_num != -1:
            task_menu = input('''Select one of the options below
            mc - mark task as complete
            et - edit task
            ''')
            #Mark as complete: replaces input for this field to "Yes" and writes new & updated data back to file
            if task_menu == "mc":
                update_input = tasks_dict[user_task_num]
                update_input[-1] = "Yes"
                tasks_dict[user_task_num] = update_input
                new_file_contents = ""
                for value in tasks_dict.values():
                    for item in value:
                        if item == value[-1]:
                            new_file_contents += (item + "\n")
                        else:
                            new_file_contents += (item + ", ")
                write_tasks = open("tasks.txt", "w")
                write_tasks.write(new_file_contents)
                break
            #Edit Task: Asks user if they would like to change assignee or due date of selected task
            elif task_menu == "et":
                task_menu_2 = input('''Select one of the options below
                at - change assignee username
                dd - change due date
                ''')
                #Asks for user input and replaces it & rewrites new & updated data to file
                if task_menu_2 == "at":
                    update_input = tasks_dict[user_task_num]
                    update_input[0] = input("Enter username of new assignee: ")
                    tasks_dict[user_task_num] = update_input
                    new_file_contents = ""
                    for value in tasks_dict.values():
                        for item in value:
                            if item == value[-1]:
                                new_file_contents += (item + "\n")
                            else:
                                new_file_contents += (item + ", ")
                    write_tasks = open("tasks.txt", "w")
                    write_tasks.write(new_file_contents)
                    break
                elif task_menu_2 == "dd":
                    update_input = tasks_dict[user_task_num]
                    update_input[4] = input("Enter new due date: ")
                    tasks_dict[user_task_num] = update_input
                    new_file_contents = ""
                    for value in tasks_dict.values():
                        for item in value:
                            if item == value[-1]:
                                new_file_contents += (item + "\n")
                            else:
                                new_file_contents += (item + ", ")
                    write_tasks = open("tasks.txt", "w")
                    write_tasks.write(new_file_contents)
                    break
            else:
                print("Do not recognise that input, please try again.")
        elif user_task_num == -1:
            break

#Function for when admin user wants to display statistics, reading data from task/user overview files (generateing them first incase they don't exist)
def display_stats():
    gen_report()
    read_tasks = open("task_overview.txt", "r")
    tasks_data = read_tasks.readlines()
    read_users = open("user_overview.txt", "r")
    users_data = read_users.readlines()

    sum_users = len(users_data)      #total number of users will be length of user list
    sum_tasks = len(tasks_data)     #total number of tasks will be number of lines read from tasks.txt file

    print(f"Total number of users: {sum_users}")
    print(f"Total number of tasks: {sum_tasks}")
    read_tasks.close()
    read_users.close()

#Function to generate report which includes overview of Tasks and Users & prints to txt file
def gen_report():
    #Task report provides info on overdue and incomplete tasks & percentages these are of overall number of tasks
    read_tasks = open("tasks.txt", "r")
    tasks_data = read_tasks.readlines()
    over_due = 0
    incomplete = 0
    #Incomplete: calculated using last input for each task in task file which represents this with a Yes/No
    for line in tasks_data:
        split_data_tasks = line.strip("\n").split(", ")
        #need to compare two dates (strings needs to be converted to date object)
        if split_data_tasks[-1].lower() == "no":
            incomplete += 1
    #Overdue: calculated by seeing if Due date is less than the current date
    for line in tasks_data:
        split_data_tasks = line.strip("\n").split(", ")
        due_date = split_data_tasks[-2]
        current_date = split_data_tasks[-3]
        if split_data_tasks[-1].lower() == "no" and due_date < current_date:
            over_due += 1
    #list of data points to be added to txt file
    total_task_num = len(tasks_data)
    complete = total_task_num - incomplete
    #Percentages taken by proportion of total tasks
    percentage_incomplete = (incomplete / total_task_num) * 100
    percentage_over_due = (over_due / total_task_num) * 100
    #Write new data and export to new txt file
    write_input_tasks = f"Total number of tasks: {total_task_num}\nNumber of complete tasks: {complete}\nNumber of incomplete tasks: {incomplete}\nNumber of overdue tasks: {over_due}\nPercentage of incomplete tasks: {percentage_incomplete}%\nNumber of overdue tasks: {percentage_over_due}%\n"
    write_tasks = open("task_overview", "w+")
    write_tasks.write(f"{write_input_tasks}")
    write_tasks.close()

    #User report provides info on each User and their total tasks, overude & incomplete/complete
    read_users = open("user.txt", "r")
    users_data = read_users.readlines()
    total_users_num = len(users_data)
    #Data colelcted through empty lists and coutners which reference if tasks are compelte or not and if they are overdue
    for line in users_data:
        split_data_users = line.strip("\n").split(", ")
        user_tasks_counter = {}
        user_completed_counter = {}
        user_overdue_counter = {}
        for count, user in enumerate(split_data_users):
            if count == 0:
                if user not in user_tasks_counter:
                    user_tasks_counter[user] = 0
                    user_completed_counter[user] = 0
                    user_overdue_counter[user] = 0
                for task in tasks_data:
                    current_task = task.strip("\n").split(", ")
                    if user.strip() == current_task[0]:
                        user_tasks_counter[user] += 1
                    if current_task[-1] == "Yes":
                        user_completed_counter[user] += 1
                    if current_task[-2] < current_task[-3] and current_task[-1] == "No":     #due date < current date
                        user_overdue_counter[user] += 1
                for user_value, task_count in user_tasks_counter.items():
                    for user_value, completed_count in user_completed_counter.items():
                        for user_value, overdue_count in user_overdue_counter.items():
                            write_input_users = ""
                            write_input_users += f"Tasks Assigned: {user_value}, {task_count} tasks\nPercentage of total tasks assigned to {user_value}: {task_count/total_task_num * 100}%\nPercentage of completed tasks for {user_value}: {completed_count/task_count * 100}%\nPercentage of incompleted tasks for {user_value}: {(1 - completed_count/task_count) * 100}%\nPercentage of overdue tasks for {user_value}: {(overdue_count/task_count) * 100}%"
    #Write new data and export to new txt file
    write_user = open("user_overview", "w+")
    write_user.write(f"{write_input_users}")
    write_user.close()
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
    #presenting the menu to the user (with extra permissions for admin user)
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