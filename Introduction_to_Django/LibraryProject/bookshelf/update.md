>>> b = Book.objects.get(title="1984")
>>> b.title = "Nineteen Eighty-Four"
>>> b.save()
>>> Book.objects.get(pk=b.pk).title
'Nineteen Eighty-Four'
