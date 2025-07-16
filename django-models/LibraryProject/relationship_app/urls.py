from django.urls import path
from .views import admin_view, librarian_view, member_view, home_view  
from .import views

urlpatterns = [
    path('books/add/', views.add_book, name='add_book'),
    path('books/<int:pk>/edit/', views.change_book, name='edit_book'),
    path('books/<int:pk>/delete/', views.delete_book, name='delete_book'),
]