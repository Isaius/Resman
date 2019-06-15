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
        
        print(idt)
        print(desc)
        print(tip)
        print(categ)
        print(est)
        print(st)

        result = getRecursosBD(idt, desc, tip, categ, est, st)
        print(result)
        if result != None:
            rst = {'recursos': result}
            print(rst['recursos'])
            return render(req, 'recursos.html', {'rst': rst})

    return render(req, 'pesquisar.html', {'form': form})

def getRecursosBD(idt=None, desc=None, tip=None, categ=None, est=None, st=None):
    result = None

    # COM ID
    if idt != "" and desc != ""  and tip != "" and categ != "" and est != "" and st != "":
        try:
            result = Recurso.objects.get(Q(identificador=idt) & Q(descricao=desc)
                                                    & Q(tipo=tip) & Q(categoria=categ) & Q(estado= est) & Q(setor=st))
            return result
        except:
            return None

    if idt != "" and desc != ""  and tip != "" and categ != "" and est != "" and st == "":
        try:
            result = Recurso.objects.get(Q(identificador=idt) & Q(descricao=desc)
                                                    & Q(tipo=tip) & Q(categoria=categ) & Q(estado= est))
            return result
        except:
            return None
    if idt != "" and desc != ""  and tip != "" and categ != "" and est == "" and st == "":
        try:
            result = Recurso.objects.get(Q(identificador=idt) & Q(descricao=desc)
                                                    & Q(tipo=tip) & Q(categoria=categ))
            return result
        except:
            return None
    if idt != "" and desc != ""  and tip != "" and categ == "" and est == "" and st == "":
        try:
            result = Recurso.objects.get(Q(identificador=idt) & Q(descricao=desc)
                                                    & Q(tipo=tip))
            return result
        except:
            return None
    if idt != "" and desc != ""  and tip == "" and categ == "" and est == "" and st == "":
        try:
            result = Recurso.objects.get(Q(identificador=idt) & Q(descricao=desc))
            return result
        except:
            return None
    if idt != "" and desc == ""  and tip == "" and categ == "" and est == "" and st == "":
        try:
            result = Recurso.objects.get(Q(identificador=idt))
            return result
        except:
            return None
    
    # SEM ID
    if idt == "" and desc != ""  and tip != "" and categ != "" and est != "" and st != "":
        try:
            result = Recurso.objects.get(Q(descricao=desc)
                                                    & Q(tipo=tip) & Q(categoria=categ) & Q(estado= est) & Q(setor=st))
            return result
        except:
            return None
    if idt == "" and desc != ""  and tip != "" and categ != "" and est != "" and st == "":
        try:
            result = Recurso.objects.get(Q(descricao=desc) & Q(tipo=tip) & Q(categoria=categ) & Q(estado= est))
            return result
        except:
            return None
    if idt == "" and desc != ""  and tip != "" and categ != "" and est == "" and st == "":
        try:
            result = Recurso.objects.get(Q(descricao=desc) & Q(tipo=tip) & Q(categoria=categ))
            return result
        except:
            return None
    if idt == "" and desc != ""  and tip != "" and categ == "" and est == "" and st == "":
        try:
            result = Recurso.objects.get(Q(descricao=desc) & Q(tipo=tip))
            return result
        except:
            return None
    if idt == "" and desc != ""  and tip == "" and categ == "" and est == "" and st == "":
        try:
            result = Recurso.objects.get(Q(descricao=desc))
            return result
        except:
            return None
    
    # SEM ID SEM DESC
    if idt == "" and desc == ""  and tip != "" and categ != "" and est != "" and st != "":
        try:
            result = Recurso.objects.get(Q(tipo=tip) & Q(categoria=categ) & Q(estado= est) & Q(setor=st))
            return result
        except:
            return None
    if idt == "" and desc == ""  and tip != "" and categ != "" and est != "" and st == "":
        try:
            result = Recurso.objects.get(Q(tipo=tip) & Q(categoria=categ) & Q(estado= est))
            return result
        except:
            return None
    if idt == "" and desc == ""  and tip != "" and categ != "" and est == "" and st == "":
        try:
            result = Recurso.objects.get(Q(tipo=tip) & Q(categoria=categ))
            return result
        except:
            return None
    if idt == "" and desc == ""  and tip != "" and categ == "" and est == "" and st == "":
        try:
            result = Recurso.objects.get(Q(tipo=tip))
            return result
        except:
            return None

    # SEM ID SEM DESC SEM TIPO
    if idt == "" and desc == ""  and tip == "" and categ != "" and est != "" and st != "":
        try:
            result = Recurso.objects.get(Q(categoria=categ) & Q(estado= est) & Q(setor=st))
            return result
        except:
            return None
    if idt == "" and desc == ""  and tip == "" and categ != "" and est != "" and st == "":
        try:
            result = Recurso.objects.get(Q(categoria=categ) & Q(estado= est))
            return result
        except:
            return None
    if idt == "" and desc == ""  and tip == "" and categ != "" and est == "" and st == "":
        try:
            print("Ta chegando aqui!")
            result = Recurso.objects.get(Q(categoria=categ))
            print(result)
            return result
        except:
            print("Excecao recurso da categoria " + categ + " nao encontrado.")
            return None
    
    # SEM ID SEM DESC SEM TIPO SEM CATEGORIA
    if idt == "" and desc == ""  and tip == "" and categ == "" and est != "" and st != "":
        try:
            result = Recurso.objects.get( Q(estado= est) & Q(setor=st))
            return result
        except:
            return None
    if idt == "" and desc == ""  and tip == "" and categ == "" and est != "" and st == "":
        try:
            result = Recurso.objects.get(Q(estado= est))
            return result
        except:
            return None
    
    # SEM ID SEM DESC SEM TIPO SEM CATEGORIA SEM ESTADO
    if idt == "" and desc == ""  and tip == "" and categ == "" and est == "" and st != "":
        try:
            result = Recurso.objects.get( Q(estado= est) & Q(setor=st))
            return result
        except:
            return None
    
    # SEM ID SEM DESC SEM TIPO SEM CATEGORIA SEM ESTADO SEM STATUS
    # SO RETORNA NONE, IMPOSSIVEL PESQUISAR
    
    return None