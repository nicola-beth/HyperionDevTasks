#inport relevant libaries & nlp load
import spacy
nlp = spacy.load("en_core_web_md")

#Function to take in movie description and read into nlp to compare to list of movie descriptions in a txt file
def movie_recomendation(movie_description):
    nlp_movie_description = nlp(movie_description)
    read_movies = open("movies.txt", "r")
    movies_data = read_movies.readlines()
    movies_dict = {}                #empty dictionary to add movie letter and description to
    movies_similarity_ratings = {}  #empty dictionary to add movie similarity rating to so can extract most similar
    for line in movies_data:
        key, value = line.strip("\n").split(":")
        movies_dict[key] = value
    for key, value in movies_dict.items():
        similarity = nlp(value).similarity(nlp_movie_description)
        movies_similarity_ratings[key] = similarity
    most_similar_rating = max(movies_similarity_ratings.values())
    for k, v in movies_similarity_ratings.items():
        if v == most_similar_rating:
            most_similar_movie = k
    print(f"Most similar movie in our database: {most_similar_movie} at a rating of {most_similar_rating}\n", value)

#Provided inputs to feed into the function
user_movie_title = "Planet Hulk"
user_movie_description = "Will he save their world or destroy it? When the hulk becomes too dangerous for the earth, the illuminati trick hulk into a shuttle and launch him into space to a planet where hulk can live in peace. Unfortuently, Hulk land on the planet Sakaar where he is sold into slavery nd trained as a gladiator."

#Run the function
movie_recomendation(user_movie_description)