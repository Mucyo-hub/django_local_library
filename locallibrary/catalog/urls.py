from django.urls import path
from . import views
from .views import (BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView,
                    AuthorListCreateAPIView, AuthorRetrieveUpdateDestroyAPIView,
                    GenreListCreateAPIView, GenreRetrieveUpdateDestroyAPIView)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
  path('', views.index, name='index'),
  path('books/', views.BookListView.as_view(), name='books'),
  path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
  path('authors/', views.AuthorListView.as_view(), name='authors'),
  path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
  path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
  path('borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed'),
  path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
  path('author/create/', views.AuthorCreate.as_view(), name='author-create'),
  path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
  path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
  #Book API
  path('api/books/', BookListCreateAPIView.as_view(), name='book-list-create'),
  path('api/books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
  # Author API
  path('api/authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
  path('api/authors/<int:pk>/', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='author-detail'),
  
  #Genre API
  path('api/genres/', GenreListCreateAPIView.as_view(), name='genre-list-create'),
  path('api/genres/<int:pk>/', GenreRetrieveUpdateDestroyAPIView.as_view(), name='genre-detail'),
  path('api-token-auth/', obtain_auth_token, name='api_token_auth'),


]