import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from connect_db import Base, Director, Movie, Genre

DATABASE_URL = "sqlite:///movies.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

def init_db():
    
    Base.metadata.create_all(engine)
    print("Database Initialized")

def create_movie():
    title = input("Enter movie title: ")
    year = int(input("Enter movie year: "))
    rating = float(input("Enter movie rating: "))
    director_id = int(input("Enter director ID: "))
    genre_id = int(input("Enter genre ID: "))
    
    movie = Movie(title=title, year=year, rating=rating, director_id=director_id, genre_id=genre_id)
    session.add(movie)
    session.commit()
    print(f"Movie '{title}' created with ID {movie.id}")

def update_movie():
    movie_id = int(input("Enter movie ID to update: "))
    movie = session.get(Movie, movie_id)
    if not movie:
        print(f"Movie with ID {movie_id} does not exist.")
        return
    movie.title = input(f"Enter new title for movie (current: {movie.title}): ") or movie.title
    movie.year = int(input(f"Enter new year for movie (current: {movie.year}): ") or movie.year)
    movie.rating = float(input(f"Enter new rating for movie (current: {movie.rating}): ") or movie.rating)
    session.commit()
    print(f"Movie ID {movie_id} updated successfully")

def delete_movie():
    movie_id = int(input("Enter movie ID to delete: "))
    movie = session.get(Movie, movie_id)
    if not movie:
        print(f"Movie with ID {movie_id} does not exist.")
        return
    session.delete(movie)
    session.commit()
    print(f"Movie ID {movie_id} deleted successfully.")

def create_director():
    name = input("Enter director name: ")
    age = int(input("Enter director age: "))
    director = Director(name=name, age=age)
    session.add(director)
    session.commit()
    print(f"Director '{name}' created with ID {director.id}")

def delete_director():
    director_id = int(input("Enter director ID to delete: "))
    director = session.get(Director, director_id)
    if not director:
        print(f"Director with ID {director_id} does not exist.")
        return
    
    # Check if director has any movies
    if director.movies:
        print(f"Cannot delete director. They have {len(director.movies)} movies assigned.")
        return
        
    session.delete(director)
    session.commit()
    print(f"Director ID {director_id} deleted successfully.")

def list_directors_and_movies():
    directors = session.query(Director).all()
    if not directors:
        print("No directors found.")
    for director in directors:
        print(director)
        for movie in director.movies:
            print(f"  - {movie}")

def view_movies_by_genre():
    genre_id = int(input("Enter genre ID to view movies: "))
    movies = session.query(Movie).filter(Movie.genre_id == genre_id).all()
    if not movies:
        print(f"No movies found for genre ID {genre_id}.")
        return
    for movie in movies:
        print(movie)

def view_movies_by_director():
    director_id = int(input("Enter director ID to view movies: "))
    movies = session.query(Movie).filter(Movie.director_id == director_id).all()
    if not movies:
        print(f"No movies found for director ID {director_id}.")
        return
    for movie in movies:
        print(movie)

def create_genre():
    name = input("Enter genre name: ")
    genre = Genre(name=name)
    session.add(genre)
    session.commit()
    print(f"Genre '{name}' created with ID {genre.id}")

def delete_genre():
    genre_id = int(input("Enter genre ID to delete: "))
    genre = session.get(Genre, genre_id)
    if not genre:
        print(f"Genre with ID {genre_id} does not exist.")
        return
    
    # Check if genre has any movies
    if genre.movies:
        print(f"Cannot delete genre. It has {len(genre.movies)} movies assigned.")
        return
        
    session.delete(genre)
    session.commit()
    print(f"Genre ID {genre_id} deleted successfully.")

def main_menu():
    while True:
        print("\nWelcome to the Movie Management Application. What would you like to do?")
        print("1. Create Director")
        print("2. Delete Director")
        print("3. Create Genre")
        print("4. Delete Genre")
        print("5. Create Movie")
        print("6. Update Movie")
        print("7. Delete Movie")
        print("8. List Directors and Movies")
        print("9. View Movies by Genre")
        print("10. View Movies by Director")
        print("11. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_director()
        elif choice == "2":
            delete_director()
        elif choice == "3":
            create_genre()
        elif choice == "4":
            delete_genre()
        elif choice == "5":
            create_movie()
        elif choice == "6":
            update_movie()
        elif choice == "7":
            delete_movie()
        elif choice == "8":
            list_directors_and_movies()
        elif choice == "9":
            view_movies_by_genre()
        elif choice == "10":
            view_movies_by_director()
        elif choice == "11":
            print("Exiting.......")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    init_db()
    main_menu()
