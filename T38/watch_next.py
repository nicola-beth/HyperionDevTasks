import spacy
nlp = spacy.load("en_core_web_md")


def movie_recomendation(movie_description):
    nlp_movie_description = nlp(movie_description)
    read_movies = open("movies.txt", "r")
    movies_data = read_movies.readlines()
    movies_dict = {}
    movies_similarity_ratings = {}
    for line in movies_data:
        key, value = line.strip("\n").split(":")
        movies_dict[key] = value
    for key, value in movies_dict.items():
        similarity = nlp(value).similarity(nlp_movie_description)
        movies_similarity_ratings[key] = similarity
    print(f"Most similar movie in our database: {max(movies_similarity_ratings)}\n", value)

user_movie_title = "Planet Hulk"
user_movie_description = "Will he save their world or destroy it? When the hulk becomes too dangerous for the earth, the illuminati trick hulk into a shuttle and launch him into space to a planet where hulk can live in peace. Unfortuently, Hulk land on the planet Sakaar where he is sold into slavery nd trained as a gladiator."

movie_recomendation(user_movie_description)