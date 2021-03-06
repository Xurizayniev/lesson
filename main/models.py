from django.db import models

# Create your models here.

class BookModel(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
    