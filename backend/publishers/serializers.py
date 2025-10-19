from rest_framework import serializers
from .models import Publisher


class GetPublisherList(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["id", "name", "description", "website"]


class GetPublisherDetails(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["id", "name", "description", "website", "established", "country"]


class PostPublisherUpdate(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ["name", "description", "website", "established", "country"]
