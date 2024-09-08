from django.db import models


class Author(models.Model):
    """
    Author model to store author details. An author can have multiple books.
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Book model to store book details, including title, publication year,
    and the author (foreign key).
    """

    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
