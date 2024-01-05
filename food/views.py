from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the Food App Homepage.</h1>")

def item(request):
    return HttpResponse("<h1>This is item view.</h1>")
