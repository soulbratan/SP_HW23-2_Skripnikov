from django.urls import path
from .views import (
    BlogPostListView,
    BlogPostDetailView,
    BlogPostCreateView,
    BlogPostUpdateView,
    BlogPostDeleteView
)

app_name = 'blog'

urlpatterns = [
    path('blogs/', BlogPostListView.as_view(), name='post_list'),
    path('blogs/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('blogs/create/', BlogPostCreateView.as_view(), name='post_create'),
    path('blogs/<int:pk>/update/', BlogPostUpdateView.as_view(), name='post_update'),
    path('blogs/<int:pk>/delete/', BlogPostDeleteView.as_view(), name='post_delete'),
]