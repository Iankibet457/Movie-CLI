import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from connect_db import Base, Director, Movie, Genre

DATABASE_URL = "sqlite:///movies.db"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

# def init_db():
#     # Initialize Database
#     Base.metadata.create_all(engine)
#     print("Database Initialized")

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
    birth_year = int(input("Enter director birth year: "))
    director = Director(name=name, birth_year=birth_year)
    session.add(director)
    session.commit()
    print(f"Director '{name}' created with ID {director.id}")

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

def main_menu():
    while True:
        print("\nWelcome to the Movie Management Application. What would you like to do?")
        print("1. Create Movie")
        print("2. Update Movie")
        print("3. Delete Movie")
        print("4. Create Director")
        print("5. List Directors and Movies")
        print("6. View Movies by Genre")
        print("7. View Movies by Director")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_movie()
        elif choice == "2":
            update_movie()
        elif choice == "3":
            delete_movie()
        elif choice == "4":
            create_director()
        elif choice == "5":
            list_directors_and_movies()
        elif choice == "6":
            view_movies_by_genre()
        elif choice == "7":
            view_movies_by_director()
        elif choice == "8":
            print("Exiting.......")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # init_db()
    main_menu()
