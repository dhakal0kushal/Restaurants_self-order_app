from django.contrib import admin

from .models import Category, Item, Cart, CartItems

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Cart)
admin.site.register(CartItems)
