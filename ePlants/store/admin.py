from django.contrib import admin

from .models.category import Category
from .models.customer import Customer
from .models.products import Products

# Register your models here.
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Products)