from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
# Create your views here.

from .models import Post

def posts_create(request):
    return HttpResponse("<h1>create</h1>")

def posts_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title":instance.title,
        "instance":instance
    }

    return render(request,"post_detail.html",context)

def posts_list(request):
    queryset = Post.objects.all()
    context={
        "title":"fuck ",
        "object_list":queryset
    }
    return render(request,"index.html",context)




def posts_update(request):
    return HttpResponse("<h1>update</h1>")

def posts_delete(request):
    return HttpResponse("<h1>delete</h1>")
