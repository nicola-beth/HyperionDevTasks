names = "" #empty string to add student names to
name = input("Enter student name (or stop to finish): ").lower()  # user input for student name

while name != 'stop':
    names += name + ", " #add name to list with comma inbetween
    name = input("Enter student name (or stop to finish): ").lower()  # user input for student name

print(names) #print list of student names