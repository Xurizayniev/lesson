from django.urls import path
from .views import HomeView, CreatebookView, UpdateBook, BookDetailView
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreatebookView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateBook.as_view(), name='update'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='detail'),
]