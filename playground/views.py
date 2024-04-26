from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Collection, Order


def say_hello(request):
    # queryset = Product.objects.filter(last_update__year=2021)
    # queryset = Customer.objects.filter(email__icontains='.com')
    # queryset = Collection.objects.filter(featured_product__isnull=True)
    # queryset = Product.objects.filter(inventory__lt=10)
    queryset = Order.objects.filter(customer_id=1)
    return render(request, 'hello.html', {'orders': queryset})