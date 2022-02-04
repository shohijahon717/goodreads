from django.urls import path
from .views import BooksView, BookDetailView

app_name = 'books'

urlpatterns = [
    path('', BooksView.as_view(), name='list'),
    path('<int:pk>', BookDetailView.as_view(), name='detail'),
]
