from django.shortcuts import render
from django.views.generic import DetailView
from .models import Author, Book, Library, Librarian



# Create your views here.
def list_books_view(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/book_list.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'