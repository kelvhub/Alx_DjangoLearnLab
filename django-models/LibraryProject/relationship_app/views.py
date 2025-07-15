from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library
from django.http import HttpResponse
from relationship_app.models import Author, Librarian

def list_books_view(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
