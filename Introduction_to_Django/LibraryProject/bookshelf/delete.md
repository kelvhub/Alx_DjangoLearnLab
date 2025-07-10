>>> b = Book.objects.get(pk=b.pk)
>>> b.delete()
(1, {'bookshelf.Book': 1})
>>> list(Book.objects.all())
[]
