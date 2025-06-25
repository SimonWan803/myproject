from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .models import Author, Publisher, Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Standard admin configuration
    list_display = ('title', 'author', 'publication_date', 'genre', 'price')
    list_filter = ('genre', 'author')
    search_fields = ('title', 'author__name', 'isbn')

    # Add custom view to urls
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('combined-view/', self.admin_site.admin_view(self.combined_view), name='combined-view'),
        ]
        return custom_urls + urls

    # Custom view logic
    def combined_view(self, request):
        books = Book.objects.select_related('author').prefetch_related('publishers').all()
        context = {
            'books': books,
            'opts': self.model._meta,
            **self.admin_site.each_context(request),
        }
        return render(request, 'admin/combined_view.html', context)