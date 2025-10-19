from rest_framework import serializers
from .models import Author
from books.serializers import GetBookForAuthor


class GetAuthorList(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name", "biography", "birth_year", "nationality"]


class GetAuthorDetails(serializers.ModelSerializer):
    books = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ["id", "name", "biography", "birth_year", "nationality", "books"]

    def get_books(self, obj):
        return GetBookForAuthor(obj.books.all(), many=True).data


class PostAuthorUpdate(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["name", "biography", "birth_year", "nationality"]
