#programe to check if users input is a palindrone

user_word = input("Please enter a word to check if it is a palindrone: ")       #user input for word
list_letters = list(user_word)      #split user word into list of letters which make up the word
list_letters.reverse()      #reverse the order of the list
reversed_word = ("".join(list_letters))     #join the list in reverse order

#if statement to check if users word (user_word) is spelt the same backwards (reversed_word)
if user_word == reversed_word:
    print("Your word is a palindrome")
else:
    print("Your word is not a palindrome")