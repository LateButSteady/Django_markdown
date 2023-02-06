from django.shortcuts import render

from .models import Post

# Create your views here.
def index(request):
    return render(request, "index.html")

def page_md(request):
    posts = Post.objects.all()
    return render(request, 'page_md.html', {'posts': posts})

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'detail.html', {'post': post})