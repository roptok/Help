from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Book, Quantity, Author, Stock
from django.http import Http404
from rest_framework import status
from django.db.models import Sum


class Books(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = serializers.BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Authors(APIView):

    def get(self, request):
        authors = Author.objects.all()
        serializer = serializers.AuthorSerializer(authors, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Stocks(APIView):

    def get(self, request):
        stocks = Stock.objects.all()
        serializer = serializers.StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class BooksDetail(APIView):

    def get(self, request, book_id):
        try:
            boks = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            raise Http404
        serializer = serializers.BookSerializer(boks)
        return Response(serializer.data)

    def delete(self, request, book_id):
        try:
            boks = Book.objects.get(pk=book_id)
        except Book.DoesNotExist:
            raise Http404
        boks.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, book_id):
        try:
            boks = Book.objects.get(pk=book_id)
            serializer = serializers.BookSerializer(boks, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            raise Http404


class AuthorDetail(APIView):

    def get(self, request, author_id):
        try:
            aut = Author.objects.get(pk=author_id)
        except Author.DoesNotExist:
            raise Http404
        serializer = serializers.AuthorSerializer(aut)
        return Response(serializer.data)

    def delete(self, request, author_id):
        try:
            aut = Author.objects.get(pk=author_id)
        except Book.DoesNotExist:
            raise Http404
        aut.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, author_id):
        try:
            aut = Author.objects.get(pk=author_id)
            serializer = serializers.AuthorSerializer(aut, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            raise Http404


class AuthorSelection(APIView):

    def get(self, request, author_id):
        boks = Book.objects.filter(author=author_id)
        if not boks:
            raise Http404
        serializer = serializers.BookSerializer(boks, many=True)
        return Response(serializer.data)


class StockDetail(APIView):

    def get(self, request, Stock_id):
        try:
            boks = Quantity.objects.filter(stock_id=Stock_id).aggregate(Sum("quantity"))
        except boks.DoesNotExist:
            raise Http404
        return Response(boks)


class QuantityStockDetail(APIView):

    def get(self, request, Stock_id):
        stocks = Quantity.objects.all().filter(stock_id=Stock_id)
        serializer = serializers.QuantitySerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self, request, Stock_id):
        serializer = serializers.QuantitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuantityBookStockDetail(APIView):

    def get(self, request, Stock_id, book_id):
        if not Quantity.objects.all().filter(stock_id=Stock_id, book_id=book_id):
            raise Http404
        stocks = Quantity.objects.all().filter(stock_id=Stock_id, book_id=book_id)
        serializer = serializers.QuantitySerializer(stocks, many=True)
        return Response(serializer.data)

    def put(self, request, Stock_id, book_id):
        try:
            stock = Quantity.objects.get(stock_id=Stock_id, book_id=book_id)
            serializer = serializers.QuantitySerializer(stock, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Quantity.DoesNotExist:
            raise Http404
