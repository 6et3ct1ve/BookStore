from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "biography", "birth_year", "nationality"]
        read_only_fields = ["id"]


class AuthorDetailSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ["id", "name", "biography", "birth_year", "nationality", "books"]
        read_only_fields = ["id"]

    def get_books(self, obj):
        return [
            {
                "id": book.id,
                "title": book.title,
                "price": str(book.price),
                "genre": book.genre,
            }
            for book in obj.books.all()
        ]
