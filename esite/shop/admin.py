from django.contrib import admin
from .models import Product
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created', 'updated')
    search_fields = ('name', 'description')
    list_filter = ('created', 'updated')

admin.site.register(Product, ProductAdmin)