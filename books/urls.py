from django.urls import path
from .views import BooksView, BookDetailView, BookCreateView, AddReviewView

app_name = 'books'

urlpatterns = [
    path('', BooksView.as_view(), name='list'),
    path('<int:id>', BookDetailView.as_view(), name='detail'),
    path('create/', BookCreateView.as_view(), name="create"),
    path('<int:id>/reviews/', AddReviewView.as_view(), name='reviews')
]
