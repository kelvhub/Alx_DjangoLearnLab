from django.urls import path
from .views import admin_view, librarian_view, member_view, home_view  


urlpatterns = [
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
    path('', home_view, name='home'),  # Default view can be set to admin_view or any other view
]