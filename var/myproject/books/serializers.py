from rest_framework import serializers
from . import models
import base64
from django.conf import settings
import os


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ['id', 'firstname', 'secondname']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ['id', 'title']


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stock
        fields = ['id', 'title', 'city']


class QuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Quantity
        fields = ['id', 'book', 'stock', 'quantity']
