from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    stock_quantity = models.PositiveIntegerField()
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title

