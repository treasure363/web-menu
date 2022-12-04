from django.contrib import admin
from .models import Item, Category, Table, Cart

# Register your models here.
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Table)
admin.site.register(Cart)
