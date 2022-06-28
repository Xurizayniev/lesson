from django import forms
from .models import BookModel

class CreateBookForm(forms.ModelForm):
    
    class Meta:
        model = BookModel
        fields = ['name', 'price']