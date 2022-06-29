from django.shortcuts import render
from django.views.generic import *
from .models import *
from .forms import *
# Create your views here.

class HomeView(ListView):
    model = BookModel
    queryset = BookModel.objects.all()
    template_name = 'main/index.html'
    context_object_name = ''

    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            qs = BookModel.objects.all().filter(name__icontains=q)
        else:
            qs = BookModel.objects.all()
        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        q = self.request.GET.get('q')
        if q:
            context['q'] = q
        return context

class CreatebookView(CreateView):
    success_url = '/'
    model = BookModel
    template_name = 'main/form.html'
    fields = ['name', 'price']


class UpdateBook(UpdateView):
    model = BookModel
    template_name = 'main/update.html'
    fields = ['name', 'price']
    success_url = '/'

class BookDetailView(DetailView):
    model = BookModel
    template_name = 'main/detail.html'