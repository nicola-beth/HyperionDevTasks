#programe to make letters user inputs disappear from user input sentence

user_sentence = input("Please input a sentence: ")      #user input for sentence

remove_chars = []   #empty list for remove characters inputted by user
user_remove = input("Please entered a character you would like to make disappear or 'stop' to run: ")       #user input for remove characters or stop

#loop to add user_remove character to remove_chars list by appending, break loop if stop is entered by the user
while True:
    if user_remove != "stop":
        remove_chars.append(user_remove)
        user_remove = input("Please entered a character you would like to make disappear or 'stop' to run: ")
    else:
        break

#when charcater in remove list appears in user_sentence, replace remove character with nothing ""
for i in remove_chars:
    user_sentence = user_sentence.replace(i, "")

print(user_sentence)