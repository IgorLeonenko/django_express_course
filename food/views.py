from django.shortcuts import render
from django.http import HttpResponse
from .models import Item

def index(request):
    items = Item.objects.all()
    return HttpResponse(items)

def item(request):
    return HttpResponse("<h1>This is item view.</h1>")
