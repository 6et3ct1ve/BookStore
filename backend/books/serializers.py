from rest_framework import serializers
from .models import Book
from authors.models import Author
from publishers.models import Publisher


class GetBookForAuthor(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "price", "genre"]


class GetBookList(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ["id", "title", "author", "price", "genre", "cover_image"]

    def get_author(self, obj):
        return {
            "id": obj.author.id,
            "name": obj.author.name,
            "href": f"/api/authors/{obj.author.id}",
        }


class GetBookDetails(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    publisher = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "publisher",
            "isbn",
            "description",
            "price",
            "genre",
            "publication_year",
            "pages",
            "language",
            "stock_quantity",
            "cover_image",
        ]

    def get_author(self, obj):
        return {
            "id": obj.author.id,
            "name": obj.author.name,
            "biography": obj.author.biography,
        }

    def get_publisher(self, obj):
        return {"id": obj.publisher.id, "name": obj.publisher.name}


class PostBookCreate(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(), source="author", write_only=True
    )
    publisher_id = serializers.PrimaryKeyRelatedField(
        queryset=Publisher.objects.all(), source="publisher", write_only=True
    )

    class Meta:
        model = Book
        fields = [
            "title",
            "author_id",
            "publisher_id",
            "isbn",
            "description",
            "price",
            "genre",
            "publication_year",
            "pages",
            "language",
            "stock_quantity",
            "cover_image",
        ]

    def validate_isbn(self, value):
        isbn_digits = value.replace("-", "")
        if len(isbn_digits) != 17:
            raise serializers.ValidationError("ISBN must be 17 digits")
        if not isbn_digits.isdigit():
            raise serializers.ValidationError("ISBN must contain only digits")
        return value

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than 0")
        return value

    def validate_stock_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError("Stock quantity cannot be negative")
        return value


class PostBookResponse(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    publisher = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "publisher",
            "isbn",
            "price",
            "genre",
            "publication_year",
            "pages",
            "language",
            "stock_quantity",
            "cover_image",
        ]

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
