from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def posts_create(request):
    return HttpResponse("<h1>create</h1>")

def posts_detail(request):
    return HttpResponse("<h1>detail</h1>")

def posts_list(request):
    return HttpResponse("<h1>list</h1>")


def posts_update(request):
    return HttpResponse("<h1>update</h1>")

def posts_delete(request):
    return HttpResponse("<h1>delete</h1>")
