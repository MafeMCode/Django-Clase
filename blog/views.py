from django.shortcuts import render

# Create your views here.

def principal(request):
    return render(request, 'blog/principal.html')

def listados(request):
    return render(request, 'blog/listados.html')