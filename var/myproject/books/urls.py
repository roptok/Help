
from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.Books.as_view()),
    path('authors/', views.Authors.as_view()),
    path('stocks/', views.Stocks.as_view()),
    path('books/<str:book_id>/', views.BooksDetail.as_view()),
    path('books/authorselection/<str:author_id>/', views.AuthorSelection.as_view()),
    path('stocks/<str:Stock_id>/', views.StockDetail.as_view()),
    path('stocks/<str:Stock_id>/quantity', views.QuantityStockDetail.as_view()),
    path('stocks/<str:Stock_id>/quantity/<str:book_id>', views.QuantityBookStockDetail.as_view()),
    path('authors/<str:author_id>', views.AuthorDetail.as_view()),
]