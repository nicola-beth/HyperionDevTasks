# #natural language processing - computer understands text
# #import library & load relevant spacy mode
import spacy
nlp = spacy.load("en_core_web_sm")

# #list of garden path sentences
garden_path_sentences = ["sandra decided she wanted to paint the blue wall with cracks.", "Have the Pursian students who failed the exam take the supplementary.", "The girl told the story cried back in 1066.", "I convinced her ten children are noisy.", "The man who whistles tunes pianos, 500 in one day."]

# Get labels for entities and print them
for sen in garden_path_sentences:
    nlp_garden_path_sentences = nlp(sen)
    print([(i, i.label_, i.label) for i in nlp_garden_path_sentences.ents])

print(spacy.explain("NORP"))
print(spacy.explain("CARDINAL"))

#NORP - Nationalities or religious or political groups
#Makes sense as this was returned for Pursian which is a nationality

#CARDINAL - Numerals that do not fall under another type
#Makes sense as this was returned for 2 numbers, numeric and in text formfs