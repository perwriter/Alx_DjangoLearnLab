from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("create_book/", views.create_book, name="create-book"),
    path("list_book/", views.book_list, name="list-book"),
    path("view_book/<int:book_id>/", views.view_book, name="view-book"),
    path("edit_book/<int:book_id>/", views.edit_book, name="edit-book"),
    path("delete_book/<int:book_id>/", views.delete_book, name="delete-book"),
]
