# Movie Management CLI Application

A command-line interface application for managing movies, directors, and genres using SQLAlchemy and SQLite.

## Installation

1. Clone the repository
2. Create a virtual environment:
3. Install dependencies:
4. Run the application:

## Usage

1. Run the application:
2. Follow the prompts to manage movies, directors, and genres.

## Contributing

1. Fork the repository
2. Create a new branch:
3. Make changes and commit:
4. Push to the branch:
5. Submit a pull request

## License

This project is open-sourced under the MIT License - see the LICENSE file for details.

The application will initialize the database and present you with a menu of options:

1. Create Director - Add a new director with name and age
2. Create Genre - Add a new movie genre
3. Create Movie - Add a new movie with title, year, rating, and associations
4. Update Movie - Modify existing movie details
5. Delete Movie - Remove a movie from the database
6. List Directors and Movies - View all directors and their movies
7. View Movies by Genre - Filter movies by genre
8. View Movies by Director - Filter movies by director
9. Exit - Close the application

## Features

### Director Management
- Create new directors with name and age
- View directors and their associated movies
- Directors are automatically assigned a unique ID

### Genre Management
- Create new genres
- View movies by genre
- Genres are automatically assigned a unique ID

### Movie Management
- Create movies with:
  - Title
  - Release year
  - Rating (0-10)
  - Associated director (via director_id)
  - Associated genre (via genre_id)
- Update movie details
- Delete movies
- View movies filtered by director or genre

## Database Schema

The application uses SQLite with the following structure:

### Directors Table
- id (Primary Key)
- name
- age

### Genres Table
- id (Primary Key)
- name

### Movies Table
- id (Primary Key)
- title
- year
- rating
- director_id (Foreign Key)
- genre_id (Foreign Key)

## Dependencies

- SQLAlchemy
- Python 3.x
- Additional dependencies listed in requirements.txt

## Error Handling

The application includes basic error handling for:
- Invalid input types
- Non-existent IDs
- Invalid menu choices

## Contributing

Feel free to submit issues and enhancement requests.

## License

[Add your chosen license here]

