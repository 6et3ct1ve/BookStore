from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import ProtectedError
from .models import Author
from .serializers import GetAuthorList, GetAuthorDetails, PostAuthorUpdate


class AuthorListCreateView(APIView):

    def get(self, request):
        authors = Author.objects.all()
        serializer = GetAuthorList(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostAuthorUpdate(data=request.data)
        if serializer.is_valid():
            author = serializer.save()
            response_serializer = GetAuthorList(author)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailView(APIView):

    def get_object(self, pk):
        try:
            return Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return None

    def get(self, request, pk):
        author = self.get_object(pk)
        if author is None:
            return Response(
                {"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = GetAuthorDetails(author)
        return Response(serializer.data)

    def put(self, request, pk):
        author = self.get_object(pk)
        if author is None:
            return Response(
                {"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = PostAuthorUpdate(author, data=request.data)
        if serializer.is_valid():
            author = serializer.save()
            response_serializer = GetAuthorList(author)
            return Response(response_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        author = self.get_object(pk)
        if author is None:
            return Response(
                {"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            author.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            return Response(
                {
                    "error": "Cannot delete author with existing books. Please remove all books first."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
