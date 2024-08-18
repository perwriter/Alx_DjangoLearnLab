from django.urls import path
from .views import custom_login_view, RegisterView, list_books, LibraryDetailView

urlpatterns = [
    path('login/', custom_login_view, name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    # Add other URL patterns here
]
