
from django.contrib import admin
from django.urls import path
from posts.views import index,details
urlpatterns = [
    path('', index, name='posts.index'),
    path('details/<int:id>', details, name='posts.details'),
]
