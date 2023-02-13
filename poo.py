import spacy
nlp = spacy.load("en_core_web_sm")

wiki_priyanka = """known by her married name Priyanka Chopra Jonas, is an Indian actress,
singer, film producer, philanthropist, and the winner of the Miss World 2000 pageant.
One of India's highest-paid and most popular celebrities, Chopra has received numerous
awards, including a National Film Award and five Filmfare Awards. In 2016, the Government
of India honoured her with the Padma Shri, and Time named her one of the 100 most influential people in the world."""

# Get labels and entities and print them
nlp_priyanka = nlp(wiki_priyanka)
print([(i, i.label_, i.label) for i in nlp_priyanka.ents])
#
# # #list of garden path sentences
# garden_path_sentences = ["We painted the wall with cracks.", "Have the students who failed the exam take the supplementary.", "The girl told the story cried.", "I convinced her children are noisy.", "The man who whistles tunes pianos."]
#
# # Get labels and entities and print them
# for sen in garden_path_sentences:
#     nlp_garden_path_sentences = nlp(sen)
#     print([(i, i.label_, i.label) for i in nlp_garden_path_sentences.ents])