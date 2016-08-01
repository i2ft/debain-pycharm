from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

from .forms import Postfrom

from .models import Post

def posts_create(request):
    form = Postfrom(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print form.cleaned_data.get("title")
        instance.save()

    context={
        "form":form,
    }
    return render(request,"post_form.html",context)

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




def posts_update(request,id=None):
    instance = get_object_or_404(Post, id=id)
    form = Postfrom(request.POST or None,instance=instance)

    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        messages.success(request,"<a href ='#'>Item</a> Saved",extra_tags='html_safe')


        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form":form
    }

    return render(request, "post_form.html", context)



def posts_delete(request):
    return HttpResponse("<h1>delete</h1>")
