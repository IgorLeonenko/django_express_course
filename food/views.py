from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

def index(request):
    items = Item.objects.all()
    context = {
        "items": items,
    }
    return render(request, 'food/index.html', context)


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        "item": item,
    }
    return render(request, 'food/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form': form})

def edit_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    context = {
        'form': form,
        'item': item
    }
    return render(request, 'food/item-form.html', context)

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item-delete.html', {'item': item})