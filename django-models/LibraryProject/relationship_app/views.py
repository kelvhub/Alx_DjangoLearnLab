from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse
from .models import Book
from .forms import BookForm


def home_view(request):
    return render(request, 'relationship_app/home.html')


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


