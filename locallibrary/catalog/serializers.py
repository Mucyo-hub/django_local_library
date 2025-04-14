from rest_framework import serializers
from .models import Book,Author, Genre #importing my Book Model, Author and Genre 
class AuthorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Author
    fields = '__all__'
class GenreSerializer(serializers.ModelSerializer):
  class Meta:
    model = Genre
    fields = '__all__'
    


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'  #
