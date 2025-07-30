
from django.contrib import admin
from django.urls import path
# from category.views import CategoryView,CreateCategoryView
from category.views import CategoryListView, DetailCategoryView, CreateCategoryView, UpdateCategoryView, \
    DeleteCategoryView

urlpatterns = [
    path('', CategoryListView.as_view(), name='category.index'),
    path('details/<int:pk>', DetailCategoryView.as_view(), name='category.details'),
    path('create', CreateCategoryView.as_view(), name='category.create'),
    path('update/<int:pk>', UpdateCategoryView.as_view(), name='category.update'),
        path('delete/<int:pk>', DeleteCategoryView.as_view(), name='category.delete'),
]
