
from django.contrib import admin
from django.urls import path
from contactus.views import index as contactus_index
urlpatterns = [
    path('', contactus_index, name='contactus_index'),
]
