from django.contrib import admin

# Register your models here.
from .models import Product

tables = [Product]
admin.site.register(tables)