#programe to read txt file and calculate the number of lines, words and characters

read_input = open("input.txt", "r")     #open the file in read mode
input_data = read_input.readlines()     #create a variable of file data


print(f"There are {len(input_data)} lines in this .txt file")       #length of input data will return number of lines

word_count = 0          #create variable to add word count to
character_count = 0     #create variable to add character count to

#for every line in text data variable, remove the new line notation & split by the spaces between words to create a list
for line in input_data:
    split_data = line.strip("\n").split(" ")
    word_count += len(split_data)           #add length of each word to total
    #loop over every word in the list to calculate the length of each
    for i in split_data:
        character_count += len(i)           #add number of characters in each word to total

print(f"There are {word_count} words in this .txt file")
print(f"There are {character_count} characters in this .txt file")

read_input.close()
