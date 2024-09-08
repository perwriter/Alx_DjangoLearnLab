import datetime
from .models import Book
from rest_framework import generics
from django.shortcuts import render
from .serializers import BookSerializer
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.exceptions import ValidationError
from django_filters import rest_framework, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


class BookListView(generics.ListAPIView):
    """
    Allows read-only access to all users.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ["title", "author__name", "publication_year"]
    search_fields = ["title", "author__name"]
    ordering_fields = ["title", "publication_year", "author__name"]
    ordering = ["title"]
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveAPIView):
    """
    Allows read-only access to all users.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    Allows only authenticated users to create new books.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        current_year = datetime.datetime.now().year
        if serializer.validated_data["publication_year"] > current_year:
            raise ValidationError("Publication year cannot be in the future.")

        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Allows only authenticated users to update existing books.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        current_year = datetime.datetime.now().year
        if serializer.validated_data["publication_year"] > current_year:
            raise ValidationError("Publication year cannot be in the future.")

        serializer.save()


class BookDeleteView(generics.DestroyAPIView):
    """
    Allows only authenticated users to delete books.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
