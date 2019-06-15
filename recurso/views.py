from django.shortcuts import render
from .models import Recurso

# Create your views here.
def list_rec(req):
    recursos = Recurso.objects.all()
    print(recursos)
    return render(req, 'recursos.html', {'recursos': recursos})