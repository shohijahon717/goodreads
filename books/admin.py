from django.contrib import admin
from .models import Author, BookAuthor, Book, BookReview
# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'email', 'bio',)
    list_filter = ('first_name', 'last_name', 'email', 'bio',)


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description', 'isbn',)
    list_filter = ('title', 'description', 'isbn',)
    list_display = ('title', 'description', 'isbn',)


class BookAuthorAdmin(admin.ModelAdmin):
    pass


class BookReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
admin.site.register(BookReview, BookReviewAdmin)

