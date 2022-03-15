from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from .models import Book, BookReview
from .forms import BookCreateForm, BookReviewForm


# class BooksView(ListView):
#     template_name = 'books/list.html'
#     queryset = Book.objects.all()
#     context_object_name = 'books'
#     paginate_by = 2


class BooksView(View):
    def get(self, request):
        books = Book.objects.all().order_by('id')
        search_query = request.GET.get('q', '')
        if search_query:
            books = books.distinct().filter(Q(title__icontains=search_query) |
                                            Q(description__icontains=search_query))

        page_size = request.GET.get('page_size', 2)
        paginator = Paginator(books, page_size)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        context = {
            'page_obj': page_obj,
            'search_query': search_query
        }
        return render(request, 'books/list.html', context)


# class BookDetailView(DetailView):
#     template_name = 'books/detail.html'
#     pk_url_kwarg = "pk"
#     model = Book
#     context_object_name = 'book'
class BookDetailView(View):
    def get(self, request, id):
        review_form = BookReviewForm()
        book = Book.objects.get(id=id)
        context = {
            'book': book,
            'review_form': review_form,
        }
        return render(request, 'books/detail.html', context)


class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForm(request.POST)
        if review_form.is_valid():
            BookReview.objects.create(
                user=request.user,
                book=book,
                stars_given=review_form.cleaned_data[
                    'stars_given'
                ],
                comment=review_form.cleaned_data['comment'],
            )
            return redirect(reverse('books:detail', kwargs={'id': book.id}))
        context = {
            'book': book,
            'review_form': review_form,
        }
        return render(request, 'books/detail.html', context)


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










