from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def first(request):
    return HttpResponse("Hey! It's your first view!!")


def hello(request):
    return render(request, 'hello.html')
