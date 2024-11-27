from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def principal(request):
    posts = Post.objects.all()
    autores = Post.objects.values_list('autor', flat=True).distinct()
    return render(request, 'blog/principal.html', {'posts':posts, 'autores':autores})

def detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detalle.html', {'post':post})