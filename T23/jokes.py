#programe to reutrn a random joke
import random
#list of jokes
jokes = ["Did you hear about the mathematician who's afraid of negative numbers?: He'll stop at nothing to avoice them",
         "Why do we tell actors to break a leg?: Because every play has a cast",
         "Did you hear about the claustrophobic astronaut?: He just needed a little space",
         "Why don't scientists trust atoms: Because they make up everything"]

#print random choice from list using raddom libary 
joke = random.choice(jokes)
print(joke)