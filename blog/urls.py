from django.urls import path
from .views import (
    PostListCreate, PostDetail,
    CommentListCreate, CommentDetail
)

urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list'),
    path('posts/<slug:slug>/', PostDetail.as_view(), name='post-detail'),
    path('posts/<slug:post_slug>/comments/', CommentListCreate.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]