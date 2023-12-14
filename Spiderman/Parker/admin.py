from django.contrib import admin
from .models import Brand, Category, Product, Review
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price')
    search_fields = ['name']
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'text', 'rating')
    search_fields = ['product__name', 'user__username']
    
    
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)