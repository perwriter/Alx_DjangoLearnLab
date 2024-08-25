from django.urls import path
from . import views

urlpatterns = [
    path("list_books/", views.list_books, name="list-books"),
    path("library_detail/", views.LibraryDetailView.as_view(), name="library-detail"),
]
