from django.shortcuts import render, get_object_or_404
from .models import Post, Autor

# Create your views here.

def principal(request):
    posts = Post.objects.all()
    autores = Autor.objects.all().distinct()
    return render(request, 'blog/principal.html', {'posts':posts, 'autores':autores})

def detalle_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post':post})

def detalle_autor(request, pk):
    posts = Post.objects.all()
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'blog/detalle_autor.html', {'autor':autor, 'posts':posts})