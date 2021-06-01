from django.shortcuts import render
from django.http import JsonResponse
from .models import *

# Create your views here.
def store(request):
    products = Product.objects.all()
    contex = {"products":products}
    return render(request, 'store/store.html', contex)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    contex = {'items':items, 'order':order}
    return render(request, 'store/cart.html', contex)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    contex = {'items':items, 'order':order}
    return render(request, 'store/checkout.html', contex)


def updateItem(request):
    return JsonResponse('item was added', safe=False)
