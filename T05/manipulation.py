str_manip=input("Enter a sentence of your choice: ")
print(len(str_manip))

last_letter = str_manip[-1]
print((str_manip).replace(last_letter, "@"))

print(str_manip[-1:-4:-1])

print(str_manip[0:3] + str_manip[-2::])

print(str_manip.replace(" ", "\n"))