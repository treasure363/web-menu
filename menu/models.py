from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100, blank = True, default = "")
    description = models.CharField(max_length=150, blank = True, default = "")
    image = models.ImageField(upload_to='item', blank=True, null=True)
    ratings = models.DecimalField(blank = True, default = 0.0, max_digits = 5, decimal_places = 2)
    price = models.DecimalField(blank = True, default = 0.0, max_digits = 5, decimal_places = 2)
    ordered = models.IntegerField(blank = True, default = 0)
    vegan = models.BooleanField(blank = True, default = False)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='category', blank = True)

    def __str__(self):
        return f'{self.name} @{self.price} of {self.category_id.name}'

    def __repr__(self):
        return f'Item(name={self.name}, description={self.description}, price={self.price}, prdered={self.ordered}, vegan={self.vegan})'

class Category(models.Model):
    name = models.CharField(max_length=100, blank = True, default = "")
    description = models.CharField(max_length=100, blank = True, default = "")
    image = models.ImageField(upload_to='category', blank=True, null=True)
    # item_id = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='category', blank = True)
    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'Category(name={self.name}, description={self.description})'

class Table(models.Model):   #change name to Customer
    table = models.OneToOneField(User, on_delete=models.CASCADE)
    order = models.BooleanField(blank = True, default = False)
    amount = models.DecimalField(blank = True, default = 0.0, max_digits = 5, decimal_places = 2)

    def __str__(self):
        return f'{self.table.username}'

class Cart(models.Model):
    table = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='quantity')
    quantity = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.quantity} - {self.item_id.name}'