from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedView

router = DefaultRouter()
router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = [
    path("", include(router.urls)),
     path("<int:pk>/like/", views.like_post, name="like_post"),
    path("<int:pk>/unlike/", views.unlike_post, name="unlike_post"),
    path("feed/", FeedView.as_view(), name="user-feed"),
]
