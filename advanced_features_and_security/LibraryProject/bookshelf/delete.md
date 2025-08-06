from bookshelf.models import Book


>>> book = Book.objects.get(pk=b.pk)
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> list(Book.objects.all())
[]
