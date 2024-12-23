from rest_framework import serializers
from apps.book.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['uuid', 'title', 'author', 'published_date', 'isbn']