from urllib import request
from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .forms import ExampleForm # Import BookForm for use in views

def home(request):
    return HttpResponse("Welcome to the Bookshelf Home Page!")

# Create your views here.

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def book_create(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/book_form.html', {'form': form})

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    book = Book.objects.get(pk=pk)
    if request.method == 'POST':
        form = ExampleForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = ExampleForm(instance=book)
    return render(request, 'bookshelf/book_form.html', {'form': form})
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    pass