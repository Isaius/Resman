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

        result = getRecursosBD2(idt, desc, tip, categ, est, st)
        print(result)
        if result != None:
            print("Gerando pagina de pesquisa")
            return render(req, 'recursos.html', {'recursos': result})

    print("Gerando pagina vazia")
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
            print("Deu certo!!")
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

def getRecursosBD2(idt=None, desc=None, tip=None, categ=None, est=None, st=None):
    result = Recurso.objects.all()
    recursos_selecionados = []

    if result is not None:
        for r in result:
            # COM TUDO
            if ((idt != "" and idt == r.identificador) and (desc != "" and desc == r.descricao)  and (tip != "" and tip == r.tipo) and 
                (categ != "" and categ == r.categoria) and (est != "" and est == r.estado) and (st != "" and st == r.setor)):
                recursos_selecionados.append(r)
                continue
            # SEM SETOR
            if ((idt != "" and idt == r.identificador) and (desc != "" and desc == r.descricao)  and (tip != "" and tip == r.tipo) and 
                (categ != "" and categ == r.categoria) and (est != "" and est == r.estado) and (st == "")):
                recursos_selecionados.append(r)
                continue
            # SEM SETOR, SEM ESTADO
            if ((idt != "" and idt == r.identificador) and (desc != "" and desc == r.descricao)  and (tip != "" and tip == r.tipo) and 
                (categ != "" and categ == r.categoria) and (est == "") and (st == "")):
                recursos_selecionados.append(r)
                continue
            # SEM SETOR, SEM ESTADO, SEM CATEGORIA
            if ((idt != "" and idt == r.identificador) and (desc != "" and desc == r.descricao)  and (tip != "" and tip == r.tipo) and 
                (categ == "") and (est == "") and (st == "")):
                recursos_selecionados.append(r)
                continue
            # SEM SETOR, SEM ESTADO, SEM CATEGORIA, SEM TIPO
            if ((idt != "" and idt == r.identificador) and (desc != "" and desc == r.descricao)  and (tip == "") and 
                (categ == "") and (est == "") and (st == "")):
                recursos_selecionados.append(r)
                continue
            # SEM SETOR, SEM ESTADO, SEM CATEGORIA, SEM TIPO, SEM DESCRICAO
            if ((idt != "" and idt == r.identificador) and (desc == "")  and (tip == "") and 
                (categ == "") and (est == "") and (st == "")):
                recursos_selecionados.append(r)
                continue
            
            # SEM ID
            if ((idt == "") and (desc != "" and desc == r.descricao)  and (tip != "" and tip == r.tipo) and 
                (categ != "" and categ == r.categoria) and (est != "" and est == r.estado) and (st != "" and st == r.setor)):
                recursos_selecionados.append(r)
                continue

            if ((idt == "") and (desc != "" and desc == r.descricao)  and (tip != "" and tip == r.tipo) and 
                (categ != "" and categ == r.categoria) and (est != "" and est == r.estado) and (st == "")):
                recursos_selecionados.append(r)
                continue

            if ((idt == "") and (desc != "" and desc == r.descricao)  and (tip != "" and tip == r.tipo) and 
                (categ != "" and categ == r.categoria) and (est == "") and (st == "")):
                recursos_selecionados.append(r)
                continue

            if ((idt == "") and (desc != "" and desc == r.descricao)  and (tip != "" and tip == r.tipo) and 
                (categ == "") and (est == "") and (st == "")):
                recursos_selecionados.append(r)
                continue

            if ((idt == "") and (desc != "" and desc == r.descricao)  and (tip == "") and 
                (categ == "") and (est == "") and (st == "")):
                recursos_selecionados.append(r)
                continue
            
            # SEM ID SEM DESC
            if ((idt == "") and (desc == "")  and (tip != "" and tip == r.tipo) and 
                (categ != "" and categ == r.categoria) and (est != "" and est == r.estado) and (st != "" and st == r.setor)):
                recursos_selecionados.append(r)
                continue
            # SEM ID, SEM DESC, SEM SETOR
            if ((idt == "") and (desc == "")  and (tip != "" and tip == r.tipo) and 
                (categ != "" and categ == r.categoria) and (est != "" and est == r.estado) and (st == "")):
                recursos_selecionados.append(r)
                continue
            # SEM ID, SEM DESC, SEM ESTADO, SEM SETOR
            if ((idt == "") and (desc == "")  and (tip != "" and tip == r.tipo) and 
                (categ != "" and categ == r.categoria) and (est == "") and (st == "")):
                recursos_selecionados.append(r)
                continue
             # SEM ID, SEM DESC, SEM ESTADO, SEM SETOR, SEM CATEGORIA
            if ((idt == "") and (desc == "")  and (tip != "" and tip == r.tipo) and 
                (categ == "") and (est == "") and (st == "")):
                recursos_selecionados.append(r)
                continue

            # SEM ID SEM DESC SEM TIPO
            if ((idt == "") and (desc == "")  and (tip == "") and (categ != "" and categ == r.categoria) and 
                (est != "" and est == r.estado) and (st != "" and st == r.setor)):
                recursos_selecionados.append(r)
                continue
            if ((idt == "") and (desc == "")  and (tip == "") and (categ != "" and categ == r.categoria) and 
                (est != "" and est == r.estado) and (st == "")):
                recursos_selecionados.append(r)
                continue
            if ((idt == "") and (desc == "")  and (tip == "") and (categ != "" and categ == r.categoria) and 
                (est == "") and (st == "")):
                recursos_selecionados.append(r)
                continue
            
            # SEM ID SEM DESC SEM TIPO SEM CATEGORIA
            if ((idt == "") and (desc == "")  and (tip == "") and (categ == "") and 
                (est != "" and est == r.estado) and (st != "" and st == r.setor)):
                recursos_selecionados.append(r)
                continue
            if ((idt == "") and (desc == "")  and (tip == "") and (categ == "") and 
                (est != "" and est == r.estado) and (st == "")):
                recursos_selecionados.append(r)
                continue
            
            # SEM ID SEM DESC SEM TIPO SEM CATEGORIA SEM ESTADO
            if ((idt == "") and (desc == "")  and (tip == "") and (categ == "") and 
                (est == "") and (st != "" and st == r.setor)):
                recursos_selecionados.append(r)
                continue
            
            # SEM ID SEM DESC SEM TIPO SEM CATEGORIA SEM ESTADO SEM STATUS
            # SO RETORNA NONE, IMPOSSIVEL PESQUISAR
            
    return recursos_selecionados