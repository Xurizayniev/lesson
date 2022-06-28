from django.db import models

# Create your models here.

class BookModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    class Meta:
        verbose_name = 'book'
        verbose_name_prural = 'books'