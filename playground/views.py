from django.shortcuts import render
from django.http import HttpResponse
from store.models import Product, Customer


def say_hello(request):
    # queryset = Product.objects.filter(last_update__year=2021)
    queryset = Customer.objects.filter(email__icontains='.com')
    return render(request, 'hello.html', {'customers': queryset})