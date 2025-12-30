import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# On récupère le chemin du dossier 'api'
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# On pointe directement sur le fichier DANS le dossier api
db_path = os.path.join(BASE_DIR, "movies.db")

# Construction de l'URL pour SQLite
SQLALCHEMY_DATABASE_URL = f"sqlite:///{db_path.replace(os.sep, '/')}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

print(f"Base de données utilisée : {db_path}")


# tester la connexion
# if __name__ == "__main__":
#     try:
#         # Essayer de se connecter à la base de données
#         with engine.connect() as connection:
#             print("Connexion à la base de données réussie.")
#     except Exception as e:
#         print(f"Erreur lors de la connexion à la base de données : {e}")### Classes ###


