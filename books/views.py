from django.shortcuts import render, redirect
from .forms import AuthorForm, GenreForm, BookForm, BookSearchForm
from .models import Author, Genre, Book
import requests
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    # Mostrar libros populares en la página de inicio
    response = requests.get('https://www.googleapis.com/books/v1/volumes?q=bestsellers')
    books = response.json()['items']
    return render(request, 'books/home.html', {'books': books})

# Vista para añadir o editar un autor
def author_edit(request, author_id=None):
    if author_id:
        author = Author.objects.get(pk=author_id)
    else:
        author = None

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('authors_list')
    else:
        form = AuthorForm(instance=author)

    return render(request, 'books/author_form.html', {'form': form})

# Vista para añadir o editar un género
def genre_edit(request, genre_id=None):
    if genre_id:
        genre = Genre.objects.get(pk=genre_id)
    else:
        genre = None

    if request.method == 'POST':
        form = GenreForm(request.POST, instance=genre)
        if form.is_valid():
            form.save()
            return redirect('genres_list')
    else:
        form = GenreForm(instance=genre)

    return render(request, 'books/genre_form.html', {'form': form})

def book_edit(request, book_id=None):
    if book_id:
        book = Book.objects.get(pk=book_id)
    else:
        book = None

    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm(instance=book)

    return render(request, 'books/book_form.html', {'form': form})

def book_search(request):
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Recuperar libros locales incluyendo portada y PDF
            local_books = Book.objects.filter(title__icontains=query)
            # Lista de libros locales ajustada para coincidir con la estructura esperada en la plantilla
            local_books = [
                {
                    'title': book.title,
                    'thumbnail': book.cover.url if book.cover else None,
                    'pdf': book.pdf.url if book.pdf else None,
                    'infoLink': None  # O alguna URL específica si la tienes
                }
                for book in local_books
            ]
            # Búsqueda en la API de Google Books
            response = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={query}')
            api_books = response.json().get('items', [])
            # Lista de libros de la API de Google Books
            api_books = [
                {
                    'title': item['volumeInfo']['title'],
                    'thumbnail': item['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in item['volumeInfo'] else None,
                    'infoLink': item['volumeInfo']['infoLink']
                }
                for item in api_books
            ]
            # Combinar resultados locales y de la API
            results = local_books + api_books
            return render(request, 'books/search_results.html', {'form': form, 'results': results})
    else:
        form = BookSearchForm()

    return render(request, 'books/book_search.html', {'form': form})


def fetch_books(request):
    # Ejemplo: buscar libros sobre "fiction"
    response = requests.get('https://www.googleapis.com/books/v1/volumes?q=fiction')
    books = response.json()['items']  # Ajusta esto según la estructura de datos de la API
    return render(request, 'books/books_list.html', {'books': books})

def authors_list(request):
    authors = Author.objects.all()
    return render(request, 'books/authors_list.html', {'authors': authors})

def author_edit(request, author_id=None):
    if author_id:
        author = Author.objects.get(pk=author_id)
    else:
        author = None

    if request.method == 'POST':
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('authors_list')  # Asegúrate de que 'authors_list' es el nombre correcto de la URL
    else:
        form = AuthorForm(instance=author)

    return render(request, 'books/author_form.html', {'form': form})

def genres_list(request):
    genres = Genre.objects.all()
    return render(request, 'books/genres_list.html', {'genres': genres})

def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})