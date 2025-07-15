from django.urls import path
from .views import login_view, logout_view, register_view, home_view  # only import views that exist
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', home_view, name='home'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register_view, name='register'),


]
