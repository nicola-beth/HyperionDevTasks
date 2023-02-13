#programe to count and return number of times letters appear in a sentence
sentence = input("Enter a sentence: ")

#create dictionary variable to store letters
my_count = {}

#iterate through all letters in sentence and letter as key = 1 if not counted yet or add 1 to value if already in dictionary as a key
for i in sentence:
    if i not in my_count:
        my_count[i] = 1
    else:
        my_count[i] += 1
print(my_count)

