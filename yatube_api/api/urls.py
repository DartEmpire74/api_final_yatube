from django.urls import include, path
from rest_framework import routers

from .views import (
    CommentViewSet, FollowViewSet, GroupViewSet,
    PostViewSet)

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='follow')
router.register(
    r'posts/(?P<post_id>[^/.]+)/comments',
    CommentViewSet, basename='post-comments'
)

v1_urls = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]

urlpatterns = [
    path('v1/', include(v1_urls)),
]
