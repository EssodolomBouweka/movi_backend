#%%
from database import SessionLocal, engine
from models import Base, Movie, Rating, Tag, Link
#%%
db = SessionLocal()

#%%
movies = db.query(Movie).limit(10).all()

for movie in movies:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Rating: {movie.rating}")
else:
    print("No more movies found.")  
# %%
def get_movie_by_id(movie_id: int):
    return db.query(Movie).filter(Movie.movieId == movie_id).first()

# %%
movie = get_movie_by_id(1)
if movie:
    print(f"Found Movie: ID {movie.movieId}, Title: {movie.title}, Rating: {movie.rating}")
else:
    print("Movie not found.")
# %% recuperer les ratings d'un film
movie = get_movie_by_id(1)
if movie:
    print(f"Ratings for Movie ID {movie.movieId}, Title: {movie.title}")
    for rating in movie.ratings:
        print(f"User ID: {rating.userId}, Rating: {rating.rating}, Timestamp: {rating.timestamp}")
else:
    print("Movie not found.")
# %% film dont genre esr "Comedy"
comedy_movies = db.query(Movie).filter(Movie.title.ilike("%Comedy%")).all()
for movie in comedy_movies:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Rating: {movie.rating}")
# %% film dont genre est "Action"
action_movies = db.query(Movie).filter(Movie.title.ilike("%Action%")).all()
for movie in action_movies:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Rating: {movie.rating}")

# %% film dont genre est "Drama"
drama_movies = db.query(Movie).filter(Movie.title.ilike("%Drama%")).all()
for movie in drama_movies:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Rating: {movie.rating}")
# %% film dont genre est "Horror"
horror_movies = db.query(Movie).filter(Movie.title.ilike("%Horror%")).all()
for movie in horror_movies:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Rating: {movie.rating}")
# %% film dont genre est "Romance"
romance_movies = db.query(Movie).filter(Movie.title.ilike("%Romance%")).all()
for movie in romance_movies:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Rating: {movie.rating}")
# %% film dont genre est "Sci-Fi"
scifi_movies = db.query(Movie).filter(Movie.title.ilike("%Sci-Fi%")).all()
for movie in scifi_movies:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Rating: {movie.rating}")

# %%    db.close()
db.close()  

# %% ouvrir une nouvelle session
db = SessionLocal()

# %% des jointures entre movies et ratings
results = db.query(Movie, Rating).join(Rating, Movie.movieId == Rating.movieId).filter(Rating.rating >= 4.5).all()

# %%
for movie, rating in results:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Rating: {rating.rating} by User ID: {rating.userId}")  

# %% sans definition explicite de la jointure
results = db.query(Movie, Rating).join(Rating).filter(Rating.rating >= 4.5).all()   
for movie, rating in results:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Rating: {rating.rating} by User ID: {rating.userId}")  
    

# %% definir une fonction pour les jointures
def get_high_rated_movies(min_rating: float):
    return db.query(Movie, Rating).join(Rating).filter(Rating.rating >= min_rating).all()   


# %%
high_rated_movies = get_high_rated_movies(4.5)
for movie, rating in high_rated_movies:
    print(f"Movie ID: {movie.movieId}, Title: {movie.title}, Rating: {rating.rating} by User ID: {rating.userId}")  

# %% recupearer les tags d'un film
movie = get_movie_by_id(1)
if movie:
    print(f"Tags for Movie ID {movie.movieId}, Title: {movie.title}")
    for tag in movie.tags:
        print(f"User ID: {tag.userId}, Tag: {tag.tag}, Timestamp: {tag.timestamp}")
else:
    print("Movie not found.")   

# %% recuperer le link d'un film
movie = get_movie_by_id(1)
if movie and movie.links:
    link = movie.links
    print(f"Link for Movie ID {movie.movieId}, Title: {movie.title}")
    print(f"IMDB ID: {link.imdbId}, TMDB ID: {link.tmdbId}")
else:
    print("Movie or link not found.")

# %% recuperer le link d'un film sans verification
movie = get_movie_by_id(1)
link = movie.links
print(f"Link for Movie ID {movie.movieId}, Title: {movie.title}")
print(f"IMDB ID: {link.imdbId}, TMDB ID: {link.tmdbId}")

# %% recuperer les links de plusieurs films
movies = db.query(Movie).limit(5).all()
for movie in movies:
    link = movie.links
    print(f"Link for Movie ID {movie.movieId}, Title: {movie.title}")
    print(f"IMDB ID: {link.imdbId}, TMDB ID: {link.tmdbId}")

# %% recuperer les links de plusieurs films avec verification
movies = db.query(Movie).limit(5).all() 
for movie in movies:
    if movie.links:
        link = movie.links
        print(f"Link for Movie ID {movie.movieId}, Title: {movie.title}")
        print(f"IMDB ID: {link.imdbId}, TMDB ID: {link.tmdbId}")
    else:
        print(f"No link found for Movie ID {movie.movieId}, Title: {movie.title}")
# %% fermer la session
db.close()

# %%
# tester la connexion a la base de donnée
from database import engine 
# %%
try:
    with engine.connect() as conn:
        print("connexion a la database réussi")
except Exception as e:
    print(f"Erreur de cnnexion a la database : {e}")
# %%
