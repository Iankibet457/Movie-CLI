from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
 

DATABASE_URL = "sqlite:///movies.db"
 

engine = create_engine(DATABASE_URL)
 

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 

Base = declarative_base()
 

class Director(Base):
    __tablename__ = 'directors'
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    birth_year = Column(Integer)
 
    movies = relationship("Movie", back_populates="director")
 
    def __repr__(self):
        return f"<Director(name='{self.name}', birth_year='{self.birth_year}')>"
 

class Genre(Base):
    __tablename__ = 'genres'
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
 
    movies = relationship("Movie", back_populates="genre")

    def __repr__(self):
        return f"<Genre(name='{self.name}')>"
 

class Movie(Base):
    __tablename__ = 'movies'
 
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    director_id = Column(Integer, ForeignKey('directors.id'))
    year = Column(Integer)
    rating = Column(Float)
    genre_id = Column(Integer, ForeignKey('genres.id'))
 
    director = relationship("Director", back_populates="movies")
    genre = relationship("Genre", back_populates="movies")
 
    def __repr__(self):
        return f"<Movie(title='{self.title}', year='{self.year}', rating='{self.rating}')>"
 
#data
Base.metadata.create_all(bind=engine)
 

db = SessionLocal()
 

# new_director = Director(name="Christopher Nolan", birth_year=1970)
# db.add(new_director)
# db.commit()
 

# new_genre = Genre(name="Science Fiction")
# db.add(new_genre)
# db.commit()
 

# new_movie = Movie(title="Inception", director_id=new_director.id, year=2010, rating=8.8, genre_id=new_genre.id)
# db.add(new_movie)
# db.commit()
 

directors = db.query(Director).all()
for director in directors:
    print(director)
    for movie in director.movies:
        print(movie)
 

db.close()