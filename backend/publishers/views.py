from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import ProtectedError
from .models import Publisher
from .serializers import GetPublisherList, GetPublisherDetails, PostPublisherUpdate


class PublisherListCreateView(APIView):

    def get(self, request):
        publishers = Publisher.objects.all()
        serializer = GetPublisherList(publishers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostPublisherUpdate(data=request.data)
        if serializer.is_valid():
            publisher = serializer.save()
            response_serializer = GetPublisherDetails(publisher)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublisherDetailView(APIView):

    def get_object(self, pk):
        try:
            return Publisher.objects.get(pk=pk)
        except Publisher.DoesNotExist:
            return None

    def get(self, request, pk):
        publisher = self.get_object(pk)
        if publisher is None:
            return Response(
                {"error": "Publisher not found"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = GetPublisherDetails(publisher)
        return Response(serializer.data)

    def put(self, request, pk):
        publisher = self.get_object(pk)
        if publisher is None:
            return Response(
                {"error": "Publisher not found"}, status=status.HTTP_404_NOT_FOUND
            )

        serializer = PostPublisherUpdate(publisher, data=request.data)
        if serializer.is_valid():
            publisher = serializer.save()
            response_serializer = GetPublisherDetails(publisher)
            return Response(response_serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        publisher = self.get_object(pk)
        if publisher is None:
            return Response(
                {"error": "Publisher not found"}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            publisher.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            return Response(
                {
                    "error": "Cannot delete publisher with existing books. Please remove all books first."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
