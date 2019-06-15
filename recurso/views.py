from django.shortcuts import render
from .models import Recurso
from .forms import Pesquisa_rec_form
from django.db.models import Q

# Create your views here.
def list_rec_all(req):
    recursos = Recurso.objects.all()
    return render(req, 'recursos.html', {'recursos': recursos})

def pesquisar(req):
    form = Pesquisa_rec_form(req.POST, None)
    if form.is_valid():
        idt = form.cleaned_data['identificador']
        desc = form.cleaned_data['descricao']
        tip = form.cleaned_data['tipo']
        categ = form.cleaned_data['categoria']
        est = form.cleaned_data['estado']
        st = form.cleaned_data['setor']
        
        querry = "SELECT * FROM Recurso WHERE "

        if idt != "":
            querry += "identificador = \'" + str(idt) +"\'"
        
        if desc != "":
            querry += " AND descricao = \'" + str(desc) +"\'"
        
        if tip != "":
            querry += " AND tipo = \'" + str(tip) +"\'"

        if categ != "":
            querry += " AND ategoria = \'" + str(categ) +"\'"

        if est != "":
            querry += " AND estado = \'" + str(est) +"\'"
        
        if st != "":
            querry += " AND setor = \'" + str(st) +"\'"
        
        querry += ";"
        result = None
        #try:
        #    result = Recurso.objects.get(Q(identificador=idt) & Q(descricao=desc)
        #     & Q(tipo=tip) & Q(categoria=categ) & Q(estado= est & Q(setor=st)))
        #except:
        #    print("Não há recursos com esses valores")

        try:
            result = Recurso.objects.raw(querry)
        except:
            print("Não há recursos com esses valores")
        print(result)
    return render(req, 'pesquisar.html', {'form': form})

def getRecursosBD():
    return