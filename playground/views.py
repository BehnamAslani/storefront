from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Collection, Order, OrderItems
from django.db import connection


def say_hello(request):
    # queryset = Product.objects.filter(last_update__year=2021)
    # queryset = Customer.objects.filter(email__icontains='.com')
    # queryset = Collection.objects.filter(featured_product__isnull=True)
    # queryset = Product.objects.filter(inventory__lt=10)
    # queryset = Order.objects.filter(customer_id=1)
    # queryset = OrderItems.objects.filter(product__collection__id=3)
    # queryset = Product.objects.order_by('unit_price','-title').reverse()
    # product = Product.objects.order_by('unit_price')[0]
    # product = Product.objects.earliest('title')
    product = Product.objects.latest('unit_price')
    # print(queryset.query)


    return render(request, 'hello.html', {'product': product})