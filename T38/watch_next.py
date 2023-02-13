import spacy
nlp = spacy.load("en_core_web_md")


def movie_recomendation(movie_description):
    nlp_movie_description = nlp(movie_description)
    read_movies = open("movies.txt", "r")
    movies_data = read_movies.readlines()
    movies_dict = {}
    for line in movies_data:
        key, value = line.strip("\n").split(":")
        movies_dict[key] = value
    for value in movies_dict.values():
        similarity = nlp(value).similarity(nlp_movie_description)
        print(movies_dict[key] + "-", similarity)

# for sentence in sentences:
#     similarity = nlp(sentence).similarity(model_sentence)
#     print(sentence + "-", similarity)
#


user_movie_title = "Planet Hulk"
user_movie_description = "Will he save their world or destroy it? When the hulk becomes too dangerous for the earth, the illuminati trick hulk into a shuttle and launch him into space to a planet where hulk can live in peace. Unfortuently, Hulk land on the planet Sakaar where he is sold into slavery nd trained as a gladiator."


movie_recomendation(user_movie_description)