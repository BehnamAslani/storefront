from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer, Collection, Order, OrderItems
from django.db import connection
from django.db.models import F

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
    # product = Product.objects.latest('unit_price')
    # queryset = Product.objects.all()[5:10]
    # queryset = Product.objects.values_list('title','collection__title') # returns tuple
    # queryset = Product.objects.values('title','collection__title') # returns dict
    # queryset = OrderItems.objects.values_list('product__title').order_by('product__title').distinct() # my slution for (directory 4, video 11) mosh exercise
    # queryset = Product.objects.filter(id__in=OrderItems.objects.values('product_id').distinct()).order_by('title')

    # deferring fields
    # queryset = Product.objects.only('id', 'title') # when we have does not define a field in only and we call it in template , its gonna take long time for call it and bunch of more query for calling it
    # queryset = Product.objects.defer('description') # if we definde << description >> and we call it << description >> in the tempalete , its gonna take long time for call it and bunch of more query for calling it
    print(queryset.query)
    # print(connection.queries)


    return render(request, 'hello.html', {'products': queryset})