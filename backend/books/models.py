from django.db import models
from authors.models import Author
from publishers.models import Publisher


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="books")
    publisher = models.ForeignKey(
        Publisher, on_delete=models.PROTECT, related_name="books"
    )
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    genre = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    pages = models.IntegerField()
    language = models.CharField(max_length=50)
    stock_quantity = models.IntegerField(default=0)
    cover_image = models.URLField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
