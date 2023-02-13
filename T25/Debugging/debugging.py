def print_values_of(dictionary, keys):
   for key, value in dictionary.items():  #for loop through all keys and values in dictionary
       if key in keys:                #if statement to check if k is in keys list
        print(value)                #print value

simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": 'd\'oh', "maggie": " (Pacifier Suck)"}
#bug in variable above, 'd'oh' needed a backwards slash infront of the ' to stop it being interepted as end of string

print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])   #argument needs to be inside a list

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''