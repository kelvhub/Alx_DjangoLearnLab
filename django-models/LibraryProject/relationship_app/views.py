from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponse


def home_view(request):    return render(request, 'relationship_app/home.html')

def role_check(role):
    def check(user):
        return hasattr(user, 'profile') and user.profile.role == role
    return check

@login_required
@user_passes_test(role_check('Admin'))
def admin_view(request):
    return render(request, 'relationship_app/admin_dashboard.html')

@login_required
@user_passes_test(role_check('Librarian'))
def librarian_view(request):
    return render(request, 'relationship_app/librarian_dashboard.html') 

@login_required
@user_passes_test(role_check('Member'))
def member_view(request):
    return render(request, 'relationship_app/member_dashboard.html')    


