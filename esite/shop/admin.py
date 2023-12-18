from django.contrib import admin
from .models import Product, Comment
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created', 'updated')
    search_fields = ('name', 'description')
    list_filter = ('created', 'updated')

admin.site.register(Product, ProductAdmin)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'created_at')
    search_fields = ('author', 'content')
    list_filter = ('created_at',)
    raw_id_fields = ('product',) 

admin.site.register(Comment, CommentAdmin)