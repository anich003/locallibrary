from django.shortcuts import render
# from django.http import HttpResponse
from catalog.models import Book, Author, BookInstance, Genre

def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    num_authors = Author.objects.count()

    num_math_books = Book.objects.filter(genre__name__icontains='Math').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_math_books': num_math_books,
    }

    return render(request, 'index.html', context=context)
