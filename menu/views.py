from sqlite3 import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib.auth.models import User
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

def del_from_cart(request, item_id, quantity):
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

def cart_all(request):
    cart = Cart.objects.all()
    items = []
    for c in cart:
        items.append(c.item_id)
    return render(request, "menu/category.html", {
        "items":items,
        "header": "My Cart",
        "quantity": True
    })

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "menu/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, "menu/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "menu/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "menu/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        if request.user.is_authenticated:
            return redirect('index')
        return render(request, "menu/register.html")