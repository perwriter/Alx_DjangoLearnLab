book = Book.objects.get(pk=1)
vars(book)
{'_state': <django.db.models.base.ModelState object at 0x0000015EDF36E310>, 'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}