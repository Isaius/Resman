from django.contrib import admin
from django.urls import path
from .views import list_rec

urlpatterns = [
    path('list/', list_rec),
]
