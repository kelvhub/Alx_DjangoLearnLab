from rest_framework import viewsets, permissions, generics
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

class IsOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission: only owners can edit/delete"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filterset_fields = ["author__username"]
    search_fields = ["title", "content"]
    ordering_fields = ["created_at"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Get posts from users the current user follows
        following_users = self.request.user.following.all()
        return Post.objects.filter(author__in=following_users).order_by("-created_at")


@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    like, created = Like.objects.get_or_create(post=post, user=request.user)
    if created:
        # Create notification for post author (if not liking own post)
        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post,
            )
        return JsonResponse({"status": "liked"})
    return JsonResponse({"status": "already_liked"})

@login_required
def unlike_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    try:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        return JsonResponse({"status": "unliked"})
    except Like.DoesNotExist:
        return JsonResponse({"status": "not_liked"})