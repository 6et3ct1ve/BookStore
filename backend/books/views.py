from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from .models import Book
from .serializers import GetBookList, GetBookDetails, PostBookCreate, PostBookResponse
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

        ordering = request.query_params.get("ordering", "title")
        allowed_orderings = ["price", "-price", "title", "-title", "genre", "-genre"]
        if ordering in allowed_orderings:
            books = books.order_by(ordering)

        paginator = PageNumberPagination()
        paginated_books = paginator.paginate_queryset(books, request)

        serializer = GetBookList(paginated_books, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = PostBookCreate(data=request.data)
        if serializer.is_valid():
            try:
                book = serializer.save()
                response_serializer = PostBookResponse(book)
                return Response(
                    response_serializer.data, status=status.HTTP_201_CREATED
                )
            except Exception as e:
                if "unique constraint" in str(e).lower() or "isbn" in str(e).lower():
                    return Response(
                        {"error": "Book with this ISBN already exists"},
                        status=status.HTTP_409_CONFLICT,
                    )
                raise
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

        serializer = GetBookDetails(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        if book is None:
            return Response(
                {"error": "Book not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = PostBookCreate(book, data=request.data)
        if serializer.is_valid():
            try:
                book = serializer.save()
                response_serializer = PostBookResponse(book)
                return Response(response_serializer.data)
            except Exception as e:
                if "unique constraint" in str(e).lower() or "isbn" in str(e).lower():
                    return Response(
                        {"error": "Book with this ISBN already exists"},
                        status=status.HTTP_409_CONFLICT,
                    )
                raise
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

        search = request.query_params.get("search")
        if search:
            books = books.filter(
                Q(title__icontains=search) | Q(author__name__icontains=search)
            )

        genre = request.query_params.get("genre")
        if genre:
            books = books.filter(genre__iexact=genre)

        min_price = request.query_params.get("min_price")
        if min_price:
            books = books.filter(price__gte=min_price)

        max_price = request.query_params.get("max_price")
        if max_price:
            books = books.filter(price__lte=max_price)

        ordering = request.query_params.get("ordering", "title")
        allowed_orderings = ["price", "-price", "title", "-title", "genre", "-genre"]
        if ordering in allowed_orderings:
            books = books.order_by(ordering)

        paginator = PageNumberPagination()
        paginated_books = paginator.paginate_queryset(books, request)

        serializer = GetBookList(paginated_books, many=True)
        return paginator.get_paginated_response(serializer.data)
