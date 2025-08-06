from django.urls import path, include
from .views import (
    BookListView, BookDetailView, BookCreateView,
    BookUpdateView, BookDeleteView, BookViewSet
)

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/', BookUpdateView.as_view(), name='book-update'),
    path('books/delete/', BookDeleteView.as_view(), name='book-delete'),
    path('', include(router.urls)),  # Include the router URLs
]
