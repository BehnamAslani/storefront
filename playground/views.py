from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Collection


def say_hello(request):
    # queryset = Product.objects.filter(last_update__year=2021)
    # queryset = Customer.objects.filter(email__icontains='.com')
    queryset = Collection.objects.filter(featured_product__isnull=True)
    return render(request, 'hello.html', {'collections': queryset})