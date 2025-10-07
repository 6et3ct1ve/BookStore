from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .models import Book
from .serializers import (
    BookListSerializer,
    BookDetailSerializer,
    BookCreateUpdateSerializer,
)
from publishers.models import Publisher


class BookListCreateView(APIView):

    def get(self, request):
        books = Book.objects.select_related("author", "publisher").all()

        search = request.query_params.get("search")
        if search:
            books = books.filter(
                Q(title__icontains=search) | Q(author__name__icontains=search)
            )

        genre = request.query_params.get("genre")
        if genre:
            books = books.filter(genre__iexact=genre)

        publisher_id = request.query_params.get("publisher")
        if publisher_id:
            books = books.filter(publisher_id=publisher_id)

        min_price = request.query_params.get("min_price")
        if min_price:
            books = books.filter(price__gte=min_price)

        max_price = request.query_params.get("max_price")
        if max_price:
            books = books.filter(price__lte=max_price)

        # Ordering
        ordering = request.query_params.get("ordering", "title")
        allowed_orderings = ["price", "-price", "title", "-title", "genre", "-genre"]
        if ordering in allowed_orderings:
            books = books.order_by(ordering)

        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetailView(APIView):

    def get_object(self, pk):
        try:
            return Book.objects.select_related("author", "publisher").get(pk=pk)
        except Book.DoesNotExist:
            return None

    def get(self, request, pk):
        book = self.get_object(pk)
        if book is None:
            return Response(
                {"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookDetailSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        if book is None:
            return Response(
                {"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookCreateUpdateSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        if book is None:
            return Response(
                {"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND
            )
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublisherBooksView(APIView):

    def get(self, request, publisher_id):
        try:
            publisher = Publisher.objects.get(pk=publisher_id)
        except Publisher.DoesNotExist:
            return Response(
                {"error": "Publisher not found"}, status=status.HTTP_404_NOT_FOUND
            )

        books = Book.objects.filter(publisher=publisher).select_related(
            "author", "publisher"
        )
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
