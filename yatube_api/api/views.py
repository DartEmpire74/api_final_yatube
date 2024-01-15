from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated, IsAuthenticatedOrReadOnly)

from posts.models import Comment, Follow, Group, Post
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer, FollowSerializer, GroupSerializer,
    PostSerializer)

User = get_user_model()


class PostViewSet(viewsets.ModelViewSet):
    """API-Endpoint для просмотра, создания или редактирования постов."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """API-Endpoint для просмотра групп."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    """API-Endpoint для подписки на других пользователей."""

    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        following_username = self.request.data.get('following')
        if not following_username:
            raise ValidationError({"following": ["Это обязательное поле!"]})

        following_user = get_object_or_404(User, username=following_username)

        if following_user == self.request.user:
            raise ValidationError(
                {"following": ["Нельзя подписаться на себя!"]})

        if Follow.objects.filter(
            user=self.request.user, following=following_user
        ).exists():
            raise ValidationError(
                {"following": ["Вы уже подписаны на этого пользователя!"]})

        serializer.save(user=self.request.user, following=following_user)


class CommentViewSet(viewsets.ModelViewSet):
    """API-Endpoint для просмотра, создания или редактирования комментариев."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return Comment.objects.filter(post_id=post.id)
