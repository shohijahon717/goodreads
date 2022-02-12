from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView

from .models import Book
from .forms import BookCreateForm


# class BooksView(ListView):
#     template_name = 'books/list.html'
#     queryset = Book.objects.all()
#     context_object_name = 'books'
#     paginate_by = 2


class BooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        page_size = request.GET.get('page_size', 2)
        paginator = Paginator(books, page_size)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        context = {
            'page_obj': page_obj,
        }
        return render(request, 'books/list.html', context)


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


class BookCreateView(View):
    #
    def get(self, request):
        form = BookCreateForm()

        context = {
            'form': form,
        }
        return render(request, 'books/create.html', context)

    def post(self, request):
        form = BookCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.info(request, "Kitob muvaffaqiyatli qo'shildi")
            return redirect('books:list')
        context = {
            'form': form,
        }
        return render(request, 'books/create.html', context)










