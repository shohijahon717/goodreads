from django.urls import path
from .views import BooksView, BookDetailView, BookCreateView

app_name = 'books'

urlpatterns = [
    path('', BooksView.as_view(), name='list'),
    path('<int:pk>', BookDetailView.as_view(), name='detail'),
    path('create/', BookCreateView.as_view(), name="create"),
]
