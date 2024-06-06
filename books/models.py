from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    publish_date = models.DateField()
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)
    pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)
    infoLink = models.URLField(blank=True, null=True)  # Asegúrate de que este campo está aquí

    def __str__(self):
        return self.title