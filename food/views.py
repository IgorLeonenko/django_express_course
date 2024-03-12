from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Item
from .forms import ItemForm

# function based views
def index(request):
    items = Item.objects.all()
    context = {
        "items": items,
    }
    return render(request, 'food/index.html', context)

# class based views
# class IndexClassView(ListView):
#     model = Item
#     template_name = 'food/index.html'
#     context_object_name = 'item_list'

# function based views
# def detail(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     context = {
#         "item": item,
#     }
#     return render(request, 'food/detail.html', context)

# class based views
class FoodDetailView(DetailView):
    model = Item
    template_name = 'food/detail.html'


# def create_item(request):
#     form = ItemForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#     return render(request, 'food/item-form.html', {'form': form})
# @login_required
class CreateItemView(CreateView):
    model = Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


@login_required
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

@login_required
def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    return render(request, 'food/item-delete.html', {'item': item})