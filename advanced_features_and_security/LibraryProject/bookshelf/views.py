from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .forms import BookForm  # Assuming you have a form for Book model

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
        # Handle form submission
        return redirect('book_list')
    return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def book_edit(request, pk):
    if request.method == 'POST':
        form = BookForm(request.POST, instance=Book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=Book)
    return render(request, 'bookshelf/book_form.html', {'form': form})
@permission_required('bookshelf.can_delete', raise_exception=True)
def book_delete(request, pk):
    pass