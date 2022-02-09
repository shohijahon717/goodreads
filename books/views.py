
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Book


class BooksView(ListView):
    template_name = 'books/list.html'
    queryset = Book.objects.all()
    context_object_name = 'books'


# class BooksView(View):
#     def get(self, request):
#         books = Book.objects.all()
#         context = {
#             'books': books,
#
#         }
#         return render(request, 'books/list.html', context)

class BookDetailView(DetailView):
    template_name = 'books/detail.html'
    pk_url_kwarg = "pk"
    model = Book
    context_object_name = 'book'
# class BookDetailView(View):
#     def get(self, request, pk):
#         book = Book.objects.get(id=pk)
#         context = {
#             'book': book
#         }
#         return render(request, 'books/detail.html', context)


        

