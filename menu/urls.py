from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("menu/", views.menu, name = "menu"),
    path("menu/<str:category>", views.category, name = "category"),
    path("menu/<str:category>/<str:item>", views.item, name = "item"),
    path("cart/add/<int:item_id>/<int:quantity>", views.add_to_cart, name="add"),
    # path("order/", views.order, name = "order"),
    # path("login/", views.login, name = "login"),
]
