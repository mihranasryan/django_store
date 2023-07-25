from django.shortcuts import render

from products.models import ProductCategory, Product

# Create your views here.
#views = вьюхи = функции

def index(request):
    context = {
        'title': 'store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'store - Каталог',
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'products/products.html', context)

