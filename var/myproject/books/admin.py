from django.contrib import admin
from .models import Book, Author, City, Stock, Quantity
# Register your models here.

admin.site.register(Book)
admin.site.register(City)
admin.site.register(Stock)
admin.site.register(Author)
admin.site.register(Quantity)