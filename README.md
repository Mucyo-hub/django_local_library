# Library Management System API

A RESTful API for managing a library’s books, authors, genres, and user interactions. Built with Django and Django REST Framework as part of a backend development capstone project.
# Features
- CRUD operations for Books, Authors, and Genres
- Token-based Authentication for secure access
- Django Admin panel for managing data
- RESTful API endpoints with browsable interface
- DRF's built-in documentation support
  # Tech Stack
  - Django
- Django REST Framework (DRF)
- SQLite3 (default, can be switched)
- JWT Authentication (via `SimpleJWT`)
- python 3.12.5
  # Authentication
  The API uses token-based authentication. To access protected endpoints (`POST`, `PUT`, `DELETE`):

1. Obtain a token:
   POST/api/ 20c25dbb75cd4c40d5619357b0763d179df45540/
   {
    "username": "Chloe"
   "password":"M0786853722m@"
   }

# Books

Method	Endpoint	Description
GET	/catalog/api/books/	List all books
POST	/catalog/api/books/	Add a new book
GET	/catalog/api/books/<id>/	Get details of a book
PUT	/catalog/api/books/<id>/	Update a book
DELETE	/catalog/api/books/<id>/	Delete a book

# Authors

Method	Endpoint	Description
GET	/catalog/api/authors/	List all authors
POST	/catalog/api/authors/	Add a new author
GET	/catalog/api/authors/<id>/	Get details of an author
PUT	/catalog/api/authors/<id>/	Update an author
DELETE	/catalog/api/authors/<id>/	Delete an author

# Genres 

Method	Endpoint	Description
GET	/catalog/api/genres/	List all genres
POST	/catalog/api/genres/	Add a new genre
GET	/catalog/api/genres/<id>/	Get genre details
PUT	/catalog/api/genres/<id>/	Update a genre
DELETE	/catalog/api/genres/<id>/	Delete a genre

# Set up and run 

# Clone the repository
git clone https://github.com/Mucyo-hub/Alx_DjangoLearnLab.git
cd Introduction_to_Django

# Activate my  virtual environment
source myworld/bin/activate

# Install dependencies
pip install -r requirements.txt

# Migrate and run
python manage.py migrate
python manage.py runserver


