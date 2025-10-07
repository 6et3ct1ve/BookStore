from rest_framework import serializers
from .models import Book
from authors.serializers import AuthorSerializer
from publishers.serializers import PublisherSerializer


class BookListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    publisher = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher', 'price', 'genre', 'cover_image']

    def get_author(self, obj):
        return {
            "id": obj.author.id,
            "name": obj.author.name,
            "href": f"/api/authors/{obj.author.id}",
        }

    def get_publisher(self, obj):
        return {
            "id": obj.publisher.id,
            "name": obj.publisher.name,
            "href": f"/api/publishers/{obj.publisher.id}",
        }


class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    publisher = PublisherSerializer(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"


class BookCreateUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0.")
        return value

    def validate_stock_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative.")
            return value
