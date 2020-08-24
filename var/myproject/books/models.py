from django.db import models


# Create your models here.


class Author(models.Model):
    firstname = models.CharField('Имя', max_length=50)
    secondname = models.CharField('Фамилия', max_length=50)

    def __str__(self):
        return self.firstname[0] + '.' + self.secondname


class Book(models.Model):
    cost = models.IntegerField()
    title = models.CharField('Название', max_length=50)
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField('Название', max_length=50)

    def __str__(self):
        return self.title


class Stock(models.Model):
    title = models.CharField('Название', max_length=50)
    city = models.ForeignKey("City", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Quantity(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, null=True)
    stock = models.ForeignKey("Stock", on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField()
