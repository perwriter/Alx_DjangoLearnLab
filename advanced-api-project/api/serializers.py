import datetime
from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    """
    BookSerializer serializes book details and includes validation to ensure
    the publication year is not in the future.
    """

    class Meta:
        model = Book
        fields = "__all__"

    def validate_publication_year(self, value):
        current_year = datetime.datetime.now().year
        if value > current_year:
            raise serializers.ValidationError(
                "Publication year cannot be in the future."
            )
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    AuthorSerializer serializes the name of the author and the nested
    books associated with the author.
    """

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]
