from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView, ListView


def list_books(request):
  books = Book.objects.all()
  context = {"books": books}
  return render(request, "list_books.html", context)


class LibraryDetailView(ListView):
  model = Library
  context_object_name = "library"
  template_name = "library_detail.html"
  
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["library"] = Library.objects.all()
        return context
