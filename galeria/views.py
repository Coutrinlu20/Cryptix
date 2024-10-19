from django.shortcuts import render



def index(request):
    dados = {
        1:{"nome": " Nebuloso de Carina",
        "legenda": "webbtelecope.org / NASA / James Webb"},
        2:{"nome": "Galáxia NGC 1079",
        "legenda": "nassa.org / NASA / Hunnle"}
   }
    return render(request,'galeria/index.html', {"cards": dados})


def imagem(request):
    return render(request, 'galeria/imagem.html')
