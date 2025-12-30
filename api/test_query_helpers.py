
#%%
from database import SessionLocal
import models
from query_helpers import *
#%%
db = SessionLocal()

#%%Créer la session
db = SessionLocal()

from database import SessionLocal
import models

db = SessionLocal()

# On récupère un film et une note de référence pour les tests par ID
ref_movie = db.query(models.Movie).first()
ref_rating = db.query(models.Rating).first()
ref_tag = db.query(models.Tag).first()

print(f"--- DÉBUT DES TESTS CRUD ---")
print("\n[SECTION 1] : Récupérations par ID et Listes")

# Test Movie
movie = get_movie_by_id(db, ref_movie.movieId)
print(f"✅ get_movie_by_id : {movie.title if movie else 'Fail'}")

# Test Ratings list
ratings_list = get_ratings(db, limit=5)
print(f"✅ get_ratings : {len(ratings_list)} éléments récupérés")

# Test Tag par ID
if ref_tag:
    tag = get_tag_by_id(db, ref_tag.id)
    print(f"✅ get_tag_by_id : {tag.tag if tag else 'Fail'}")



print("\n[SECTION 2] : Filtres et Jointures")

# Test couple User/Movie
if ref_rating:
    r_user_movie = get_rating_by_user_and_movie(db, ref_rating.userId, ref_rating.movieId)
    print(f"✅ get_rating_by_user_and_movie : {'Trouvé' if r_user_movie else 'Fail'}")

# Test films avec note minimale (Jointure)
high_movies = get_movies_with_min_rating(db, min_rating=4.0)
print(f"✅ get_movies_with_min_rating (4.0+) : {len(high_movies)} films trouvés")

# Test films par Tag spécifique
if ref_tag:
    tagged_movies = get_movies_with_tags(db, ref_tag.tag)
    print(f"✅ get_movies_with_tags ('{ref_tag.tag}') : {len(tagged_movies)} films")


print("\n[SECTION 3] : Relations et Objets liés")

# Test tags via la relation movie.tags
tags_rel = get_tags_of_movie(db, ref_movie.movieId)
print(f"✅ get_tags_of_movie : {len(tags_rel) if tags_rel else 0} tags via relation")

# Test films avec liens
movies_links = get_multiple_movies_with_links(db, limit=5)
for m, l in movies_links:
    link_status = f"TMDB: {l.tmdbId}" if l else "Pas de lien"
    print(f"   - {m.title} -> {link_status}")
    movies = db.query(models.Movie).join(models.Tag).filter(
        models.Tag.tag == tag_text
    ).all()
    
db.close()
print("\n--- TOUS LES TESTS SONT TERMINÉS ---")

def get_tags_of_movie(db: models.Session, movie_id: int):
    """Récupère les tags associés à un film via la relation."""
    movie = db.query(models.Movie).filter(models.Movie.movieId == movie_id).first()
    return movie.tags if movie else []
def get_multiple_movies_with_links(db: models.Session, skip: int = 0, limit: int = 10):
    """Récupère plusieurs films avec leurs liens associés."""
    movies = db.query(models.Movie).offset(skip).limit(limit).all()
    result = []
    for movie in movies:
        link = get_link_for_movie(db, movie.movieId)
        result.append((movie, link))
    return result   