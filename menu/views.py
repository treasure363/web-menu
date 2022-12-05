from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Category, Item, Cart

# Create your views here.

def index(request):
    return redirect(request.path + 'menu/')

def menu(request):
    categories = list(Category.objects.all())
    return render(request, "menu/index.html", {
        "categories" : categories
    })

def category(request, category):
    return render(request, "menu/category.html", {
        "items":list(Category.objects.get(name=category).category.all()),
        "header": category
    })

def item(request, category, item):
    return render(request, "menu/item.html", {
        "item": Item.objects.get(name=item)
    })

def add_to_cart(request, item_id, quantity):
    if quantity==0:
        return HttpResponse()
    item = Item.objects.get(pk=item_id)
    if Cart.objects.filter(item_id=item).exists():
        cart = Cart.objects.get(item_id=item)
        cart.quantity = quantity
        cart.save()
    else:
        cart = Cart(table = request.user, item_id=item, quantity=quantity)
        cart.save()
    return HttpResponse()

def cart(request):
    cart = Cart.objects.filter(table=request.user)
    items = []
    for c in cart:
        items.append(c.item_id)
    return render(request, "menu/category.html", {
        "items":items,
        "header": "My Cart",
        "quantity": True
    })

