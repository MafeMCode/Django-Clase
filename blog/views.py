from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Post, Autor
from .forms import *

# Create your views here.


def post_new(request):
    if request.method == "POST":  
        form = post_form(request.POST) 
        if form.is_valid():    
            ftitulo = form.cleaned_data["titulo"]  
            fcuerpo = form.cleaned_data["cuerpo"]  
            fpublicado = form.cleaned_data["fpublicado"]
            fautor = Autor.objects.get(id=1)
            Post.objects.create(titulo=ftitulo, cuerpo=fcuerpo, autor=fautor, fpublicacion=fpublicado)  
            return render(request, 'blog/post_new_added.html', {"form":post_form()})
    else:
        form = post_form()
        
    return render(request, 'blog/post_new.html', {"form":form})

def post_new_model(request):
    return render(request, 'blog/post_new.html', {"form":post_form_model()})

def post_edit(request, pk):
    post = get_object_or_404(Post,pk=pk)
    if request.method == "POST":
        form = post_form(request.POST)
        if form.is_valid():
            post.titulo = form.cleaned_data["titulo"]
            post.cuerpo = form.cleaned_data["cuerpo"]  
            post.fpublicacion = form.cleaned_data["fpublicado"]
            post.autor = form.cleaned_data["autor"]
            post.save()
            return render(request, 'blog/post_edit.html', {"form":form})
    else:
        form = post_form(initial=post.__dict__) 
    return render(request, 'blog/post_new.html', {"form":form})
    
def principal(request):
    posts = Post.objects.all()
    autores = Autor.objects.all().distinct()
    return render(request, 'blog/principal.html', {'posts':posts, 'autores':autores})

def autores(request):
    autores = Autor.objects.all().distinct()
    return render(request, 'blog/autores.html', {'autores':autores})

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post':post})

def detalle_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    post = Post.objects.filter(pk=autor.pk) 
    return render(request, 'blog/detalle_autor.html', {'autor':autor, 'posts':post})

def autor_new(request):
    if request.method == "POST":  
        form = post_form_Model_Artista(request.POST)
        if form.is_valid():    
            fnombre = form.cleaned_data["nombre"]
            fapellidos = form.cleaned_data["apellidos"]
            femail = form.cleaned_data["email"]
            fdni = form.cleaned_data["dni"]
            fbio = form.cleaned_data["bio"]
            Autor.objects.create(nombre=fnombre, apellidos=fapellidos, email=femail, dni=fdni, bio=fbio)  
            return render(request, 'blog/autores.html')
    else:
        form = post_form_Model_Artista()
        
    return render(request, 'blog/autor_new.html', {"form":form})

def autor_edit(request, pk):
    autor = get_object_or_404(Autor,pk=pk)
    if request.method == "POST":
        form = post_form_Model_Artista(request.POST, instance=autor)
        if form.is_valid():
            autor.nombre = form.cleaned_data["nombre"]
            autor.apellidos = form.cleaned_data["apellidos"]
            autor.email = form.cleaned_data["email"]
            autor.dni = form.cleaned_data["dni"]
            autor.bio = form.cleaned_data["bio"]
            form.save()
            return redirect('autores')
    else:
        form = post_form_Model_Artista(initial=autor.__dict__) 
    return render(request, 'blog/autor_edit.html', {"autor":autor, "form":form})