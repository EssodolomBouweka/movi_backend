"""sqlalchemy models"""
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Movie(Base):
    __tablename__ = "movies"

    movieId = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    rating = Column(Float, index=True) # Moyenne des notes

    # Relations (Le "S" à la fin de ratings/tags/links indique une liste)
    ratings = relationship("Rating", back_populates="movie", cascade="all, delete-orphan")
    tags = relationship("Tag", back_populates="movie", cascade="all, delete-orphan")
    links = relationship("Link", back_populates="movie", cascade="all, delete-orphan", uselist=False)

class Rating(Base):
    __tablename__ = "ratings"

    # On utilise un ID auto-incrémenté pour la clé primaire
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, index=True)
    
    # AJOUT de ForeignKey pour lier à la table movies
    movieId = Column(Integer, ForeignKey("movies.movieId"), index=True)
    
    rating = Column(Float, index=True)
    timestamp = Column(Integer, index=True)

    movie = relationship("Movie", back_populates="ratings")

class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, index=True)
    
    # AJOUT de ForeignKey
    movieId = Column(Integer, ForeignKey("movies.movieId"), index=True)
    
    tag = Column(String, index=True)
    timestamp = Column(Integer, index=True)

    movie = relationship("Movie", back_populates="tags")

class Link(Base):
    __tablename__ = "links"

    # Ici movieId est à la fois PK et FK (relation 1-à-1)
    movieId = Column(Integer, ForeignKey("movies.movieId"), primary_key=True)
    imdbId = Column(Integer, index=True)
    tmdbId = Column(Integer, index=True)

    movie = relationship("Movie", back_populates="links")