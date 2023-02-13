#natural language processing - computer understands text
import spacy
nlp = spacy.load("en_core_web_md")
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word1.similarity(word3))
print(word3.similarity(word2))

doc = nlp("this is a test sentence")
print([(w.text, w.pos_) for w in doc])

sample = "Build your data science skills to launch an in-demand, valuable career in six months"
doc = nlp(sample)
doc.text.split()            #but doesn't consider punctuation etc.

[token.orth_ for token in doc] #punctuation is included

print([token.orth_ for token in doc if not token.is_punct | token.is_space])

for word in doc:
    if word.is_stop == True:        #spacy has set "stop" words
        print(word)

#lemmatisation (base form)
sing = "sang singing sing"
nlp_practice = nlp(sing)
print([word.lemma_ for word in nlp_practice])           #sing, sing sing

#entity recognition (split out text based on known entities)
wiki_priyanka = """know by her married name Priankta, is an Indian actress, singer, film producer, .."""
nlp_practice = nlp(wiki_priyanka)
print ([i, i.label_, i.label] for i in nlp_practice.ents)



 ------------------------- spaCy -------------------------------------
# spaCy is a Python natural language processing library specifically designed with
# the goal of being a useful library for implementing production-ready systems.
# It is particularly fast and intuitive, making it a top contender for NLP tasks.

# ------------------------- IMPORTANT -------------------------------------
#	Please make sure you have read and understand the instructions for this task.
#	We will be working with the *spaCy* which is an EXTERNAL Python module.
#	YOU MUST INSTALL IT BEFORE YOU CAN COMPLETE THIS TASK.

# ************************** INSTALLATION **************************************
# Before doing anything, you need to have spaCy installed, as well as its English language model.

# Type the following commands in command line
# pip3 install spacy
# python3 -m spacy download en_core_web_sm
# ----------------OR----------------------
# pip install spacy
# python -m spacy download en_core_web_sm

# ======= Working with the spaCy ===== #

import spacy #This statement should work if you have spaCy installed

nlp = spacy.load('en_core_web_sm')

sample = u"Build your data science skills to launch an in-demand, valuable career in six months."

doc = nlp(sample)

# Tokenisation------------------------------------------------------------------

# Tokenisation is a foundational step in many NLP tasks. Tokenising text is the
# process of splitting a piece of text into words, symbols, punctuation, spaces,
# and other elements, thereby creating “tokens”. A naive way to do this is to
# simply split the string on white space:
doc.text.split()

'''Output: ['Build', 'your', 'data', 'science', 'skills', 'to', 'launch', 'an', 'in-demand,'
, 'valuable', 'career', 'in', 'six', 'months.']'''

# On the surface, this looks fine. But, note that a) it disregards the punctuation and
# Put differently, it is naive, it fails to recognise elements of the text that help
# us (and a machine) to understand its structure and meaning. Let’s see how spaCy handles this:
[token.orth_ for token in doc]

''' Output: 
['Build', 'your', 'data', 'science', 'skills', 'to', 'launch', 'an', 'in', '-',
'demand', ',', 'valuable', 'career', 'in', 'six', 'months', '.'] '''

# Here we access the each token’s .orth_ method, which returns a string representation
# of the token rather than a spaCy token object, this might not always be desirable,
# but worth noting. SpaCy recognises punctuation and is able to split these punctuation
# tokens from word tokens. Many of spaCy’s token methods offer both string and integer
# representations of processed text – methods with an underscore suffix return strings,
# methods without an underscore suffix return integers. For example:
print([(token, token.orth_, token.orth) for token in doc])

'''
Output: 
[(Build, 'Build', 5389077834083678306),
(your, 'your', 1572612192562026184),
(data, 'data', 6645506661261177361), ]
...
'''
# If you want to avoid returning tokens that are punctuations or white space, spaCy
# provides convienient methods for this

print([token.orth_ for token in doc if not token.is_punct | token.is_space])

'''Output:
['Build', 'your', 'data', 'science', 'skills', 'to', 'launch', 'an', 'in', 'demand',
 'valuable', 'career', 'in', 'six', 'months']
'''

# Let's identify stop words. We imported the word list above, so it's just a
# matter of iterating through the tokens stored in the Doc object and performing
# a comparison:

for word in doc:
    if word.is_stop == True:
        print(word)
'''
Output:
your
to
an
in
in
six   '''


# Lemmatisation -------------------------------------------------------------

# A related task to tokenisation is lemmatisation. Lemmatisation is the process
# of reducing a word to its base form, its mother word if you like. Different
# uses of a word often have the same root meaning. For example, practice, practised
# and practising all essentially refer to the same thing. It is often desirable
# to standardise words with similar meaning to their base form. With spaCy we can
# access each word’s base form with a token’s .lemma_ method:

sing = "sang singing sing"
nlp_practice = nlp(sing)
print([word.lemma_ for word in nlp_practice])

'''Output: ['sing', 'sing', 'sing'] '''

# Why is this useful? An immediate use case is in machine learning, specifically
# text classification. Lemmatising the text prior to, for example, creating a
# “bag-of-words” avoids word duplication and, therefore, allows for the model to
# build a clearer picture of patterns of word usage across multiple documents.


# Entity recognition

# Entity recognition is the process of classifying named entities found in a text
# into pre-defined categories, such as persons, places, organisations, dates,
# etc. spaCy uses a statistical model to classify a broad range of entities,
# including persons, events, works-of-art and nationalities / religions (see the
# documentation for more information https://spacy.io/docs/usage/entity-recognition).

# For example, let’s take the first two sentences from Priyanka Chopra's wikipedia
# entry. We will parse this text, then access the identified entities using the
# doc object’s .ents method. With this method called on the doc we can access
# additional token methods, specifically .label_ and .label:

wiki_priyanka = """known by her married name Priyanka Chopra Jonas, is an Indian actress,
singer, film producer, philanthropist, and the winner of the Miss World 2000 pageant.
One of India's highest-paid and most popular celebrities, Chopra has received numerous
awards, including a National Film Award and five Filmfare Awards. In 2016, the Government
of India honoured her with the Padma Shri, and Time named her one of the 100 most influential people in the world."""

# Get labels and entities and print them
nlp_priyanka = nlp(wiki_priyanka)
print([(i, i.label_, i.label) for i in nlp_priyanka.ents])

'''Output:
 [(Priyanka Chopra Jonas, 'PERSON', 378), (Indian, 'NORP', 379), (
, 'GPE', 382), (2000, 'CARDINAL', 394), (
, 'GPE', 382), (One, 'CARDINAL', 394), (India, 'GPE', 382), (Chopra, 'ORG', 381), (
, 'GPE', 382), (a National Film Award, 'EVENT', 385), (five, 'CARDINAL', 394),
(Filmfare Awards, 'FAC', 9191306739292312949), (2016, 'DATE', 388), (the Government
, 'ORG', 381), (India, 'GPE', 382), (Padma Shri, 'PERSON', 378), (Time, 'ORG', 381),
(one, 'CARDINAL', 394), (100, 'CARDINAL', 394)]'''

# Get an explanation of an entity and print it
entity_fac = spacy.explain("FAC")
print(f"FAC:{entity_fac}")

#API Calls
import requests
response = requests.request("GET", "url...")
print(response.json())
print(response.json()[KEY])


#SEMANTIC SIMILARITY

tokens = ("cat apple monkey banana")
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
             "Hello, there is my car",
             "I\'ve lost my car in my car"
             "I\'d like my boar back",
             "I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + "-", similarity)

#************* HELP *****************
#REMEMBER THAT IF YOU NEED SUPPORT ON ANY ASPECT OF YOUR COURSE SIMPLY LOG IN TO www.hyperiondev.com/support TO:
#START A CHAT WITH YOUR MENTOR, SCHEDULE A CALL OR GET SUPPORT OVER EMAIL.
#*************************************

# *** NOTE ON COMMENTS ***
# This is a comment in Python.
# Comments can be placed anywhere in Python code and the computer ignores them - they are intended to be read by humans.
# Any line with a # in front of it is a comment and any with  ''' is also a docstring.
# Please read all the comments in this example file and all others.

import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use. Remember to install this model by typing python -m spacy download en_core_web_md into your command line

# Now we are going to look into longer texts and compare them.
# Below we  have two lists: one containing complaints submitted to a company, and another of recipes found online.
# We want to establish how spaCy's model can identify similarities or dissimilarities between complaint and recipes.

# Make sure to run this example file and read through the explanations.

# Below is a list of six complaints.
complaints = [ 'We bought a house in  CA. Our mortgage was handled by a company called ki. Soon after the mortgage was sold to ABC. Shortly after that XYZ took over the mortgage. The other day we got a notice not to send our payment to them but to loi instead. This is all so frustrating and wreaks of the  mortgage nightmare.',
'I got approved for a loan to buy a house I have submitted everything I need to for them I paid for the inspection and paid good faith check after all of that they said I did not get approved for the loan to cancel my contract because they do not want to wait for the down payments assistant said that the Sellers do not want to wait that long I feel like they are getting over on me I feel that they should have told me that I did not get approved before I spent my money and picked out a house Carrington mortgage in Ohio ',
'As per the correspondence, I received from : The University  This is to inform you that I have recently pulled my credit report and noticed that there is a collection listing from The University  on my credit report. I WAS never notified of this collection action or that I owed the debt. This letter is to inform you that I would like a verification of the debt and juilo ability to collect this money from me.',
'I am writing to dispute the follow information in my file.ON BOTH TransUnion & . for {$15000.00}. I have contacted this agency to advise to STOP CALLING ME this case was dismissed in court  2014. Please see the attached document from  County State Court. Thanking you in advanced regarding this matter.',
'I have not had a XXXX phone since early 2007. I have tried to resolve my bill in the past but it keeps reposting an old bill. I have no way to provide financial info from 8 years ago and they know that so they want me to prove it to them but I have no way to do that. Is there anyway to get  to find out how old it is.',
'I posted dated a check and mailed it for 2015 for my mortgage payment as my mortgage company will only take online payments if all the late charges are paid at once ( also illegal ), and the check was cashed on 2015 which cost me over {$70.00} in over draft fees with my bank.'
]

# We will now compare the similarity of the complaints to ascertain if spaCy's similarity
# model is able to distinguish between these long pieces of text.

print("-------------Complaints similarity---------------")
for token in complaints:
    token = nlp(token)
    for token_ in complaints:
        token_ = nlp(token_)
        print(token.similarity(token_))

# Below is a list of six recipe instructions.

recipes= [ 'Bake in the preheated oven, stirring every 20 minutes, until sugar mixture has baked and caramelized onto popcorn and cashews, about 1 hour. Spread cashew caramel corn onto a parchment paper-lined baking sheet to cool. If desired, form into balls while still warm.',
'Combine brown sugar, corn syrup, butter, salt, and cream of tartar in a large saucepan. Bring to a boil, stirring constantly, until a candy thermometer inserted into the middle of the syrup, not touching the bottom, reads 260 degrees F (127 degrees C), 6 to 8 minutes.',
'Lift marshmallow fudge out of the pan by the edges of the foil and place on a large cutting board. Dip a large knife in the remaining confectioners\' sugar and slice fudge into 1 1/2-inch squares, continually dipping knife in the sugar after each slice.',
'Melt butter in a medium saucepan over medium heat; stir in condensed milk. Pour in chocolate chips; cook and stir until melted, 5 to 10 minutes.',
'Lightly grease a cookie sheet. Deflate the dough and turn it out onto a lightly floured surface. Roll the marzipan into a rope and place it in the center of the dough. Fold the dough over to cover it; pinch the seams together to seal. Place the loaf, seam side down, on the prepared baking sheet. Cover with a damp cloth and let rise until doubled in volume, about 40 minutes. Meanwhile, preheat oven to 350 degrees F (175 degrees C)',
'In a large bowl, cream together the butter, brown sugar, and white sugar. Beat in the instant pudding mix until blended. Stir in the eggs and vanilla. Blend in the flour mixture. Finally, stir in the chocolate chips and nuts. Drop cookies by rounded spoonfuls onto ungreased cookie sheets.'
]

# We will now compare the similarity of the recipes. to ascertain how well spaCy's similarity
# model is able to distinguish between them.

print("-------------Recipes similarity---------------")
for token in recipes:
    token = nlp(token)
    for token_ in recipes:
        token_ = nlp(token_)
        print(token.similarity(token_))

# Now we want to obtain the extent of similarity between the complaints and the recipes.
# we will loop through every recipe instruction and compare it with a complaint.

print("-------------Recipes similarity---------------")

for token in recipes:
    token = nlp(token)
    for token_ in complaints:
        token_ = nlp(token_)
        print(token.similarity(token_))

# What do you observe? Note that the similarity index has reduced from what we observed in the short-text example discussed in the content PDF.


# There are several ways to make your model more accurate with the similarity
# or even prediction such as feeding it with some training data. This could include
# more vocabulary about food and recipes if you are building a models concerning food.
# You can also head over to spaCy documentation here: https://spacy.io/usage/vectors-similarity
# and check out other cool stuff!


#Capstone4 practive

class Product:
    def __init__(self, barcode, prod_label, prod_price, prod_qty):
        self.barcode = barcode
