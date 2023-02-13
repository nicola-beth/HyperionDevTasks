#function to print every day of the week
def weekdays():
    print("Monday")
    print("Tuesday")
    print("Wednesday")
    print("Thursday")
    print("Friday")
    print("Saturday")
    print("Sunday")
weekdays()      #call function to execute

#function to replace every other word in User sentence to "Hello"
#define user input for sentence and empty list fot sentence manipulation
user_sen = input("Enter a random sentence: ")
new_sentence = []

#function with parameter "sentence" which user_sen will be argument for in this example
def replace_hello(sentence):
    split_user_sen = user_sen.split(" ")        #split sentence into list
    for i in range(len(split_user_sen)):        #for number in length of list
        if i % 2 == 0:                          #if number is devisable by 2 add "Hello" to new sentence list for this index position
            new_sentence.append("Hello")
        else:                                   #otherwise add word via index in original split list to new list
            new_sentence.append(split_user_sen[i])
    print(" ".join(new_sentence))           #join list into a string (seperate items by a space) & print it out

replace_hello(user_sen)     #call function with argument to run

