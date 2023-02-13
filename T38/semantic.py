import spacy
nlp = spacy.load("en_core_web_sm")

tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


#What I found interesting:
#1. That apple and cat were similar more than I thought, would like to know how they are 0.20368057489395142 related
#2.  That banana and cat were similar more than I thought, would like to know how they are 0.2235882729291916 related
#3. That cat and banana are more similar than cat and apple - how?
#4. The highest score was banana and apple on similarity scale - this makes sense as both fruits but why higher than cat and monkey which are both animals

#en_core_web_md vs. en_core_web_sm
#noticed that with simpler model less accurate similarity scores are generated (i.e. cat apple gets higher score than cat monkey where the latter are two animals so would expect them to be more similar)
#banana and apple (both fruits) get a much lower score with the simple model
