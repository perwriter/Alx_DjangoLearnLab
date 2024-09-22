from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, UserFeed, LikePostView, UnlikePostView
from django.urls import path, include

router = DefaultRouter()

router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

custom_urls = [
    path('feed/', UserFeed.as_view(), name='user-feed'),
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]

urlpatterns = [
    path('', include(router.urls)),
] + custom_urls
