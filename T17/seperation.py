#programe to input sentence and display each word of the sentence on a seperate line

sentence = "This is the sentence I have typed out"      #define sentence to manipulate
sentence_list = sentence.split()                        #split sentence into list of words & define as variable
print("\n".join(sentence_list))                         #join list with new line between each input