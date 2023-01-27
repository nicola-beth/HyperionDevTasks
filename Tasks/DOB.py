#print movies from list individually

fav_movies = ["Frozen", "Lion King", "Moana", "Aladin", "Switch"]       #list of movies

#for loop to go through list and print each movie
for movie in fav_movies:
    print(f'Movie: {movie}')

#use enumerate to go through each list item and print title depending on index
for x, movie in enumerate(fav_movies):
    print(f'Movie {x+1}: {movie}')  #x+1 due to 0 being first index
