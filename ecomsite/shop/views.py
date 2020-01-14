from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def index(request):
    product_objects = Product.objects.all() 

    # Search Code 
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains = item_name)
    
    # Paginator Code
    paginator = Paginator(product_objects, 4) # splits number of products into 4
    page = request.GET.get('page')      # get the current page
    product_objects = paginator.get_page(page)    # Here "page" will fetch the objects which are on the current page not all of the objs.

    return render(request, 'shop/index.html', {'product_objects': product_objects})


def detail(request, id):
    product_object = Product.objects.get(id = id)
    return render(request, 'shop/detail.html' , {'product_object' : product_object})

