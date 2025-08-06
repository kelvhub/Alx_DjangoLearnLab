>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> Book.objects.get(pk=b.pk).title
'Nineteen Eighty-Four'
