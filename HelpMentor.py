user_sen = input("Enter a random sentence: ")
new_user_sen = ""

def replace_hello():
    split_user_sen = user_sen.split(" ")
    new_sentence = []
    for i in split_user_sen:
        if i % 2 == 0:
            new_sentence.append("Hello")
        else:
            new_sentence.append(word)
    new_user_sen = " ".join(new_sentence)
    return new_user_sen

print(new_user_sen)
