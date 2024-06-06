from django.urls import path
from .views import home, author_edit, authors_list, genre_edit, genres_list, book_edit, books_list, book_search, fetch_books

urlpatterns = [
    path('', home, name='home'),
    path('author/create/', author_edit, name='author_create'),
    path('author/edit/<int:author_id>/', author_edit, name='author_edit'),
    path('authors/', authors_list, name='authors_list'),
    path('genre/create/', genre_edit, name='genre_create'),
    path('genre/edit/<int:genre_id>/', genre_edit, name='genre_edit'),
    path('genres/', genres_list, name='genres_list'),
    path('book/create/', book_edit, name='book_create'),
    path('book/edit/<int:book_id>/', book_edit, name='book_edit'),
    path('books/', books_list, name='books_list'),
    path('search/', book_search, name='book_search'),
    path('fetch-books/', fetch_books, name='fetch_books'),
]
