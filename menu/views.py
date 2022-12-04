from django.shortcuts import render, redirect

from .models import Category

# Create your views here.

def index(request):
    return redirect(request.path + 'menu/')

def menu(request):
    user = request.user 
    categories = list(Category.objects.all())
    return render(request, "menu/index.html", {
        "categories" : categories
    })

def category(request, category):
    return render(request, "menu/category.html", {
        "items":list(Category.objects.get(name=category).category.all()),
        "header": category
    })

def item(request):
    pass