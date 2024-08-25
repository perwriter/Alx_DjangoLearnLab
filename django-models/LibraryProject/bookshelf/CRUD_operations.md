book = Book(title="1984", author="George Orwell", publication_year=1949)
<Book: Book object (1)>

book = Book.objects.get(pk=1)
vars(book)
{'_state': <django.db.models.base.ModelState object at 0x0000015EDF36E310>, 'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}

book.title = "Nineteen Eighty-Four"
{'_state': <django.db.models.base.ModelState object at 0x0000015EDF36E310>, 'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}

book.delete()
bookshelf.models.Book.DoesNotExist: Book matching query does not exist.