from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    pub_date = models.DateTimeField
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
