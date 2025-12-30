import models 

#  film
def get_movies(db: Session, movie_id: int = None, skip: int = 0, limit: int = 10):
    """Récupère une liste de films avec une pagination optionnelle."""
    if movie_id is not None:
        return db.query(models.Movie).filter(models.Movie.movieId == movie_id).first()
    return db.query(models.Movie).offset(skip).limit(limit).all()
#  ratings
def get_ratings(db: models.Session, skip: int = 0, limit: int = 10):
    """Récupère une liste de ratings avec une pagination optionnelle."""
    return db.query(models.Rating).offset(skip).limit(limit).all()

    """recuperer une evaluation en fonction du couple userId et movieId  """
def get_rating_by_user_and_movie(db: models.Session, user_id: int, movie_id: int):
    return db.query(models.Rating).filter(
        models.Rating.userId == user_id,
        models.Rating.movieId == movie_id
    ).first()
""" recuperer une liste d'evaluation en fonction d'un movieId """
def get_ratings_by_movie(db: models.Session, movie_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Rating).filter(
        models.Rating.movieId == movie_id
    ).offset(skip).limit(limit).all()

#  tags
def get_tags(db: models.Session, skip: int = 0, limit: int = 10):
    """Récupère une liste de tags avec une pagination optionnelle."""
    return db.query(models.Tag).offset(skip).limit(limit).all()
#  links
def get_links(db: models.Session, skip: int = 0, limit: int = 10):
    """Récupère une liste de liens avec une pagination optionnelle."""
    return db.query(models.Link).offset(skip).limit(limit).all()    
def get_movie_by_id(db: models.Session, movie_id: int):
    """Récupère un film par son ID."""
    return db.query(models.Movie).filter(models.Movie.movieId == movie_id).first()
def get_rating_by_id(db: models.Session, rating_id: int):
    """Récupère une évaluation par son ID."""
    return db.query(models.Rating).filter(models.Rating.id == rating_id).first()
def get_tag_by_id(db: models.Session, tag_id: int):
    """Récupère un tag par son ID."""
    return db.query(models.Tag).filter(models.Tag.id == tag_id).first()
def get_link_by_id(db: models.Session, link_id: int):
    """Récupère un lien par son ID."""
    return db.query(models.Link).filter(models.Link.id == link_id).first()  
def get_ratings_for_movie(db: models.Session, movie_id: int, min_rating: float):
    """Récupère les évaluations pour un film donné avec une note minimale."""
    return db.query(models.Rating).filter(
        models.Rating.movieId == movie_id,
        models.Rating.rating >= min_rating
    ).all() 
def get_tags_for_movie(db: models.Session, movie_id: int):
    """Récupère les tags pour un film donné."""
    return db.query(models.Tag).filter(
        models.Tag.movieId == movie_id
    ).all() 
def get_link_for_movie(db: models.Session, movie_id: int):
    """Récupère le lien pour un film donné."""
    return db.query(models.Link).filter(
        models.Link.movieId == movie_id
    ).first()
def get_movies_with_min_rating(db: models.Session, min_rating: float):
    """Récupère les films avec une note minimale."""
    return db.query(models.Movie).join(models.Rating).filter(
        models.Rating.rating >= min_rating
    ).all()
def get_movies_with_tags(db: models.Session, tag_text: str):
    """Récupère les films avec un tag spécifique."""
    return db.query(models.Movie).join(models.Tag).filter(
        models.Tag.tag == tag_text
    ).all()
def get_movies_with_links(db: models.Session):
    """Récupère les films qui ont des liens associés."""
    return db.query(models.Movie).join(models.Link).all()   
def get_high_rated_movies(db: models.Session, min_rating: float):
    """Récupère les films avec des évaluations supérieures ou égales à une note minimale."""
    return db.query(models.Movie, models.Rating).join(models.Rating).filter(
        models.Rating.rating >= min_rating
    ).all()
def get_tags_of_movie(db: models.Session, movie_id: int):
    """Récupère les tags associés à un film donné."""
    movie = get_movie_by_id(db, movie_id)
    if movie:
        return movie.tags
    return None
def get_link_of_movie(db: models.Session, movie_id: int):
    """Récupère le lien associé à un film donné."""
    movie = get_movie_by_id(db, movie_id)
    if movie:
        return movie.links
    return None 
def get_links_of_movies(db: models.Session, limit: int = 10):
    """Récupère les liens associés à plusieurs films."""
    movies = db.query(models.Movie).limit(limit).all()
    links = []
    for movie in movies:
        if movie.links:
            links.append((movie, movie.links))
    return links            

def get_multiple_movies(db: models.Session, limit: int = 10):
    """Récupère plusieurs films avec une limite spécifiée."""   
    return db.query(models.Movie).limit(limit).all()
def get_multiple_movies_with_links(db: models.Session, limit: int = 10):
    """Récupère plusieurs films avec leurs liens associés."""   
    movies = db.query(models.Movie).limit(limit).all()
    movies_with_links = []
    for movie in movies:
        movies_with_links.append((movie, movie.links))
    return movies_with_links    