
from django.contrib import admin
from django.urls import path
from posts.views import index,details,delete_post,create_post,update_post

urlpatterns = [
    path('', index, name='posts.index'),
    path('details/<int:id>', details, name='posts.details'),
    path('delete/<int:id>', delete_post, name='posts.delete'),
    path('create/', create_post, name='posts.create'),
    path('update/<int:id>', update_post, name='posts.update'),
]
