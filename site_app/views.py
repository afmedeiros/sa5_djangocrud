from django.shortcuts import render, redirect
from .models import CadastroDB
from django.contrib import messages
dados = []
context = {}


# Create your views here.
def cadastro(request):
    global dados
    nome = ""
    datadenascimento = ""
    email = ""
    pais = ""
    mensagem = ""
    var = "1"

    if request.POST:
        nome = request.POST.get("nome")
        datadenascimento = request.POST.get("datadenascimento")
        email = request.POST.get("email")
        pais = request.POST.get("pais")
        dados.append({"nome":nome,
                    "datadenascimento":datadenascimento,
                    "email":email,
                    "pais":pais})
        if (nome=="") or (datadenascimento=="") or (email=="") or (pais=="") :
            mensagem = "Erro no registro. Verifique o preenchimento !"
            var = ""
        else: 
            CadastroDB.objects.create(nome=nome,datadenascimento=datadenascimento,email=email,pais=pais)
            mensagem = "Cadastro realizado com sucesso"

    cadastrados = CadastroDB.objects.all()
    inverso = cadastrados[::-1]
    cadastrados = inverso[:1]      
        
    return render(request, "site_app/global/cadastro.html", context={"cadastrados":cadastrados, "var":var, "dados":dados,"nome":nome,"datadenascimento":datadenascimento,"email":email,"pais":pais, "mensagem":mensagem})


def deletar(request, id):

    cadastrado = CadastroDB.objects.get(id=id)


    return render(request, "site_app/global/deletar.html", context={"cadastrado":cadastrado})

def confirma(request, id):

    confirmado = ""
    cadastrado = CadastroDB.objects.get(id=id)
    cadastrado.delete()
    messages.success(request, "Usuário deletado com sucesso!")

    return redirect(delete)

def atualizar(request, id):

    cadastrado = CadastroDB.objects.get(id=id)
    
    return render(request, "site_app/global/atualizar.html", context={"cadastrado":cadastrado})

def update(request, id):

        nome = request.POST.get("nome")
        datadenascimento = request.POST.get("datadenascimento")
        email = request.POST.get("email")
        pais = request.POST.get("pais")
        cadastrado = CadastroDB.objects.get(id=id)
        cadastrado.nome = nome
        cadastrado.datadenascimento = datadenascimento
        cadastrado.email = email
        cadastrado.pais = pais
        cadastrado.save()
        messages.success(request, "Cadastro atualizado!")
    
        return redirect(atualiza)


def delete(request):
    
    cadastrados = CadastroDB.objects.all()
            
    return render(request, "site_app/global/delete.html", context={"cadastrados":cadastrados})

def home(request):
    
    cadastrados = CadastroDB.objects.all()
    inverso = cadastrados[::-1]
    cadastrados = inverso[:10]
    
    for i,row in enumerate(dados):
        row["id"] = i

        
    return render(request, "site_app/global/home.html", context={"cadastrados":cadastrados})

def pesquisar(request):
    
    cadastrados = CadastroDB.objects.all()
           
    return render(request, "site_app/global/pesquisar.html", context={"cadastrados":cadastrados})

def pesquisa(request):
    
    nome = request.POST.get("nome")
    cadastrados = CadastroDB.objects.filter(nome__icontains=nome)
        
           
    return render(request, "site_app/global/pesquisar.html", context={"cadastrados":cadastrados})

def delpesquisa(request):
    
    nome = request.POST.get("nome")
    cadastrados = CadastroDB.objects.filter(nome__icontains=nome)
        
           
    return render(request, "site_app/global/delete.html", context={"cadastrados":cadastrados})

def delatualiza(request):
    
    nome = request.POST.get("nome")
    cadastrados = CadastroDB.objects.filter(nome__icontains=nome)
        
           
    return render(request, "site_app/global/atualiza.html", context={"cadastrados":cadastrados})


def atualiza(request):
    
    cadastrados = CadastroDB.objects.all()
    
        
    return render(request, "site_app/global/atualiza.html", context={"cadastrados":cadastrados})



    if id:
        # import ipdb; ipdb.set_trace()
        dados = [dados[id - 1]]
    return render(request, "site_app/global/precos.html", context={"dados":dados})