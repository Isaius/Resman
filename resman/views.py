from django import http
from django.shortcuts import render

def index(req):
    return render(req, 'index.html', {})

def pesquisar(req):
    return render(req, 'pesquisar.html', {})