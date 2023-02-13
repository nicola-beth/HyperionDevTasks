names = "" #empty string to add student names to
while True:
    name = input("Enter student name (or stop to finish): ").lower()  # user input for student name
    if name != 'stop': #if name is not equal to stop
        names += name + ", " #add name to list with comma inbetween
    else:
        break #if 'stop' is entered, break the loop
print(names) #print list of student names 