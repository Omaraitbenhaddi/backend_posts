from unicodedata import name
from django.urls import path 
from posts.views import BlogHome,BlogPostCreate,BlogPostUpdate,BlogPostDelete,BlogPostDetail
from django.contrib.auth.decorators import login_required

app_name = "posts"



urlpatterns = [
    path('',BlogHome.as_view(), name='home'),
    path('create/',login_required(BlogPostCreate.as_view()), name='create'),
    path('edit/<str:slug>',login_required(BlogPostUpdate.as_view()), name='edit'),
    path('delete/<str:slug>',login_required(BlogPostDelete.as_view()), name='delete'),
    path('<str:slug>',BlogPostDetail.as_view(), name='post'),
]