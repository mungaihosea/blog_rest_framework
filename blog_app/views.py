from django.shortcuts import render, get_object_or_404
from .models import Post

def list_view(request):
    context = {}
    context["posts"] = Post.objects.all()
    return render(request, 'list_view.html', context)

def detail_view(request, id):
    post = get_object_or_404(Post, id = id)
    context = {'post': post}
    return render(request, 'detail_view.html', context)

