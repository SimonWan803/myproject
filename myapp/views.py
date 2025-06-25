from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Publisher, Book

def home(request):
    return HttpResponse("Welcome to my site!")

def view_data(request):
    context = {
        'authors': Author.objects.all(),
        'publishers': Publisher.objects.all(),
        'books': Book.objects.all()
    }
    return render(request, 'data_view.html', context)

def combined_table(request):
    books = Book.objects.select_related('author').prefetch_related('publishers').all()
    return render(request, 'combined_table.html', {'books': books})