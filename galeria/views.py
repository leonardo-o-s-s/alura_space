from django.shortcuts import render

# O views é responsavel por mostrar coisas na tela

def index(request):
    return render(request,"galeria/index.html")