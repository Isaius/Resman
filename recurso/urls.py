from django.contrib import admin
from django.urls import path
from .views import list_rec_all
from .views import pesquisar

urlpatterns = [
    path('list/', list_rec_all, name="resources_list_all"),
    path('pesquisar/', pesquisar, name="pesquisar_recursos"),
]
