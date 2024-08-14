from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# for class based views (inbuilt one)
# from django.views.generic.list import ListView
from django.views.generic import DetailView, ListView, CreateView
# Create your views here.

# class based views
# this is an alternative to below written func based index view and it is list view cause index is returning itemlist
class IndexClassView(ListView):
    model= Item
    template_name= 'base.html'
    context_object_name = 'item_list'

def index(request):
    item_list = Item.objects.all()
    return render(request, 'base.html',context={
        'item_list': item_list
    })
    
class DetailClassView(DetailView):
    model = Item
    template_name = 'detail.html'
    context_object_name = 'item'
    
def detail(request, pk):
    item = Item.objects.get(id = pk)
    return render(request, 'detail.html', context={'item': item})

# thsi is a class based view for create item
class CreateItemView(CreateView):
    model= Item
    fields = ['item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'item-form.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user    # to get the current logged in user
        return super().form_valid(form)
    

def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = ItemForm()
    
    return render(request, 'item-form.html', context={ 'form': form })


def update_item(request, id):
    item = Item.objects.get(id = id)
    
    if request.method == 'POST':
        form = ItemForm(request.POST, instance= item)
        
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = ItemForm(instance= item)
        
    return render(request, 'item-form.html', context={ 'form': form, 'item':item })

def delete_item(request, id):
    item = Item.objects.get(id = id)

    if request.method == "POST":
        
        item.delete()
        return redirect('core:index')
    
    return render(request, 'item-delete.html', context= { 'item': item })
        
        