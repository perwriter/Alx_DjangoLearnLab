from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import ExampleForm

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/view_book.html', {'book': book})
  
@permission_required('bookshelf.can_list', raise_exception=True)
def book_list(request):
  books = Book.objects.all()
  context = {"books": books}
  return render(request, "bookshelf/list_books.html", context)

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        book = Book.objects.create(title=title, content=content)
        return redirect('view-book', book_id=book.id)
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.content = request.POST['content']
        book.save()
        return redirect('view-book', book_id=book.id)
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book)
    book.delete()
    return redirect('list-book')

def example_view(request):
  if request.method == 'POST':
      title = request.POST['title']
      author = request.POST['author']
      book = Book.objects.create(title=title, author=author)
      return redirect('list_book', book_id=book.id)
  return render(request, 'bookshelf/form_example.html')