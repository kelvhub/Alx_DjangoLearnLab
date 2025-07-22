from django.shortcuts import redirect, render
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book
from .forms import BookForm


def home_view(request):
    return render(request, 'relationship_app/home.html')


@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Book_list")
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})



@permission_required('relationship_app.can_change_book')
def change_book(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("Book_detail", pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form': form, 'book': book})


@permission_required('relationship_app.can_delete_book')
def delete_book(request, pk):
    book = Book.objects.get(id=pk)
    if request.method == 'POST':
        book.delete()
        return redirect("Book_list")
    return render(request, 'relationship_app/delete_book.html', {'book': book})

def role_check(role):
    def check(user):
        return hasattr(user, 'profile') and user.profile.role == role
    return check

