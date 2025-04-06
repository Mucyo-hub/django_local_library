# Library Management System API

# Overview
The Library Management System API is a backend project built using Django and Django REST Framework. The API allows the management of books, users, and book transactions within a library. It supports CRUD operations for books and users, and includes endpoints for checking out and returning books. This system leverages Django ORM for database interactions and is designed for use in a library setting.

# Features
- *Book Management*: 
  - Create, read, update, and delete books in the library.
  - Each book has a title, author, ISBN, and availability status.
  
- *User Management*: 
  - Create, read, update, and delete user accounts.
  - Users can borrow and return books.
  
- *Checkout and Return*: 
  - Users can check out and return books.
  - The system tracks which books are checked out and when they are returned.

- *Django REST Framework*: 
  - API endpoints for all operations (CRUD for books and users, checkout/return).
  
- *Authentication*: 
  - Basic authentication or token-based authentication (JWT or others can be implemented).

# Installation

- Python  3.12.5
- Django
- Django REST Framework
