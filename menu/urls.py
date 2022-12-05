from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("menu/", views.menu, name = "menu"),
    path("menu/<str:category>", views.category, name = "category"),
    path("menu/<str:category>/<str:item>", views.item, name = "item"),
    path("cart/", views.cart, name="cart"),
    path("cart/all/", views.cart_all, name="cartall"),
    path("cart/add/<int:item_id>/<int:quantity>", views.add_to_cart, name="add"),
    path("login/", views.login_view, name = "login"),
    path("logout/", views.logout_view, name = "logout"),
    path("register", views.register, name="register"),
]
