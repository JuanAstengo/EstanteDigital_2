from django import forms
from .models import Author, Genre, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'bio']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'summary', 'isbn', 'publish_date', 'cover', 'pdf']

class BookSearchForm(forms.Form):
    query = forms.CharField(label='Buscar')

