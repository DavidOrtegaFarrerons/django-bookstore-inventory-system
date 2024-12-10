from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='books')
    pub_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isbn = models.CharField(max_length=255)
    book_cover = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
