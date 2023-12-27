from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from .models import Book


def book_list(request: HttpRequest) -> HttpResponse:
    Book.objects.create(
        name='Book 1',
        author='Author 1',
        pages=300,
        price=19.99,
        publisher='Publisher 1',
        publication_date='2024-01-01'
    )
    books = Book.objects.all()
    return render(request, 'app/book_list.html', {'books': books})
