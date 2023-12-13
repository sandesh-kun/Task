from django.contrib import admin
from .models import Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author__name')
    list_filter = ('published_date',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
