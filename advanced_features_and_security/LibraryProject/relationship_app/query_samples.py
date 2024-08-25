from .models import Book, Author, Library, Librarian

# Query all books by a specific author.
author_name = "John Doe"
author = Author.objects.get(name=author_name)
books = Book.objects.filter(author=author)

# List all books in a library.
books = Library.objects.get(name=library_name)
books.all()

# Retrieve the librarian for a library
library_name = "Prempeh library"
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)