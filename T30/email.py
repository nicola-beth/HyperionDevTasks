#OOP project with email class and appropiate getter and setter methods
class Email:
    #Initalise class with instance and class level variables
    def __init__(self, from_address, subject_line, email_contents):
        self.from_address = from_address
        self.subject_line = subject_line
        self.email_contents = email_contents
        #default values 
        self.has_been_read = False 
        self.is_spam = False

    #Method to mark email as read
    def mark_as_read(self):
        self.has_been_read = True

    #Method to mark email as spam
    def mark_as_spam(self):
        self.is_spam = True

    #Method to return if email has been read
    def get_is_read(self):
        return self.has_been_read

    #Method to return if email has been marked as spam
    def get_is_spam(self):
        return self.is_spam

    #Method to return if email subject line
    def get_subject_line(self):
        return self.subject_line

    #Method to return if sender address
    def get_from_address(self):
        return self.from_address

    #Defined string output of Class
    def __str__(self):
        output = f"From: {self.from_address}\n"
        output += f"Content: \n\t\t\t{self.email_contents}\n"
        return output

#list of Email objects
inbox = []

#Append email objects to list
inbox.append(Email("a", "a", "asjnaxzmfdvnjcx"))
inbox.append(Email("lk@gmail.com", "1234", "asjnaxzmfdvnjcx"))
inbox.append(Email("ea@ea.com", "Now a scam!", "asjnaxzmfdvnjcx"))
inbox.append(Email("jeffy@jeff.com", "ngbfdvcsx", "asjnaxzmfdvnjcx"))

#Function to add email to inbox
def add_email():
    new_from_address = input("Enter from email address: ")
    new_subject_line = input("Enter email subject line: ")
    new_email_contents = input("Enter email contents: ")
    inbox.append(Email(new_from_address, new_subject_line, new_email_contents))

#Function to list emails from user inputted email address
def list_messages_from_sender():
    for index, email_address in enumerate(inbox):
        print(f'{index}: {email_address.get_from_address()}')
    choice = int(input("Enter number of email address: "))
    sender_emails = inbox[choice]
    print(sender_emails)

#Function to return content of user chosen email and mark as read
def get_email():
    for index, email in enumerate(inbox):
        print(f'{index}: {email.get_subject_line()}')
    choice = int(input("Enter email index of the email you would like to display: "))
    email = inbox[choice]
    print(email)
    email.mark_as_read()

#Function to mark user defined email as spam
def mark_as_spam():
    for index, email in enumerate(inbox):
        print(f'{index}: {email.get_subject_line()}')
    choice = int(input("Enter email index which you would like to mark as spam: "))
    inbox[choice].mark_as_spam()

#Function to return unread emails
def get_unread_emails():
    print(f'Unread emails: ')
    for item in inbox:
        if not item.has_been_read:
            print(f"- {item.get_subject_line()}")

#Function to return spam emails
def get_spam_emails():
    print(f'Spam emails: \n')
    for item in inbox:
        if item.get_is_spam:
            print(f"- {item.get_subject_line()}")

#Function to delete emails 
def delete():
    for index, email in enumerate(inbox):
        print(f'{index}: {email.get_subject_line()}')
    choice = int(input("Enter email index which you want to delete: "))
    inbox.remove(inbox[choice])

#Code to get User input for action on Email class of Inbox instances
usage_message = '''
Welcome to the email system! What would you like to do?

s - send email.     #create new email (add new email object and add to inbox)
l - list emails from a sender.
r - read email.
m - mark email as spam.
gu - get unread emails.
gs - get spam emails.
d - delete email.
e - exit this program.
'''

# An Email Simulation

user_choice = ""

while True:
    user_choice = input(usage_message).strip().lower()
    # Send an email (Create a new Email object) and add the email to the Inbox
    if user_choice == "s":
        add_email()
        # Print a success message
        print("Email has been added to inbox.")
        pass
    # List all emails from a sender_address
    elif user_choice == "l":
        list_messages_from_sender()
        pass
    # Read an email
    elif user_choice == "r":
        get_email()
        pass
    # Mark an email as spam
    elif user_choice == "m":
        mark_as_spam()
        # Step 5: print a success message
        print("Email has been marked as spam")
        pass
    # List all unread emails
    elif user_choice == "gu":
        get_unread_emails()
        pass
    # List all spam emails
    elif user_choice == "gs":
        get_spam_emails()
        pass
    # Exit
    elif user_choice == "e":
        print("Goodbye")
        break
    # Delete an email
    elif user_choice == "d":
        delete()
        # Step 5: print a success message
        print("Email has been deleted")
        pass
    # Unrecognised input
    else:
        print("Oops - incorrect input")