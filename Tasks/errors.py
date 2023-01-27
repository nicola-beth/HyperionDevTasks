
# This example program is meant to demonstrate errors.

# There are some errors in this program, try run the program by pressing F5.
# Now look at the error messages and find and fix the errors.

print("Welcome to the error program")   #syntax error - missing brackets
print("\n")         #syntax error - missing brackets & indented when not required

#syntax errpr - all of the below 2 blocks was indented when not required
ageInt = 24  #syntax error - additional '=' not needed as a variable & runtime error - should be an int not string for calc below (answerYears), change variable to reflect this
ageStr = str(ageInt)   #runtime error - age must be converted to string for print statement below, change variable to reflect this
print("I'm " + ageStr + " years old.") #syntax error - add space between words & update variable name
three = 3.5       #runtime error - should be an float not string for calc below (answerYears) #logaical error - has 3 years when trying to calc 3.5 years

answerYears = ageInt + three       #logical error -  edit for new variable name above

print(f"The total number of years: {answerYears}")     #syntax error - missing brackets & logical error - make f string to combine string and int's
answerMonths = answerYears * 12     #runtime error, undefined variable needed changing to defined "answerYears"
print(f"In 3 years and 6 months, I'll be {answerMonths}  months old")   #syntax error - missing brackets & logical error - make f string to combine string and int's

# HINT, 330 months is the correct answer
