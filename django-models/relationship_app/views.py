from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import DetailView

# Custom registration view
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Library, Book

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'



# Custom registration view
class RegisterView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')

# No need to define custom views for LoginView and LogoutView as Django provides them
