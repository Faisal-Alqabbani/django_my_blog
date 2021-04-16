from django.urls import path
from .views import (PostListViews, DetailListViews,
                    CreatePostViews, UpdatePostViews, DeletePostViews, UserPostListViews)
from . import views

urlpatterns = [
    path('', PostListViews.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListViews.as_view(), name='user_posts'),
    path('post/new', CreatePostViews.as_view(), name='post_create'),
    path('post/<int:pk>', DetailListViews.as_view(), name='post_details'),
    path('post/<int:pk>/update', UpdatePostViews.as_view(), name='post_update'),
    path('post/<int:pk>/delete', DeletePostViews.as_view(), name='post_delete'),
    path('about/', views.about, name='blog-about')
]
