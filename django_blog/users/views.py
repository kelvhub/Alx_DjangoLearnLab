from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistraterForm, UserUpdateForm 
from django.contrib.auth import login
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegistraterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('post-list')
    else:
        form = UserRegistraterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'form': form})
