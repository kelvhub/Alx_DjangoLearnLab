from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test,permission_required
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

@login_required
@user_passes_test(role_check('member_view'))
def member_view(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'member':
        return render(request, 'relationship_app/member_dashboard.html')
    return HttpResponse("Unauthorized", status=401)

@login_required
@user_passes_test(role_check('Admin'))
def admin_view(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'admin':
        return render(request, 'relationship_app/admin_dashboard.html')
    return HttpResponse("Unauthorized", status=401)

@login_required
@user_passes_test(role_check('Librarian'))
def librarian_view(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'librarian':
        return render(request, 'relationship_app/librarian_dashboard.html')
    return HttpResponse("Unauthorized", status=401)

@login_required
@user_passes_test(role_check('Member'))
def member_view(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'member':
        return render(request, 'relationship_app/member_dashboard.html')
    return HttpResponse("Unauthorized", status=401)


