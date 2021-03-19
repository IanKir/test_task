from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import View

from .models import Breed, Dog
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView


class BreedSearchView(ListView):
    model = Breed
    template_name = 'dogs/search_results.html'

    def get_queryset(self):
        question = self.request.GET.get('q')
        object_list = Breed.objects.filter(
            Q(name__icontains=question) | Q(description__icontains=question)
        )
        return object_list


class BaseSearchView(View):
    """
    Note:
        __search works only with PostgreSQL
    """
    template_name = 'dogs/search_results.html'

    def get(self, request):
        question = request.GET.get('q')
        dogs = Dog.objects.filter(nickname__search=question)
        breeds = Breed.objects.filter(
            Q(name__search=question) | Q(description__search=question),
        )
        context = {
            'dogs': dogs,
            'breeds': breeds,
        }
        return render(request, self.template_name, context)


class BreedCreateView(CreateView):
    model = Breed
    template_name = 'dogs/breed_create.html'
    fields = '__all__'
    success_url = reverse_lazy('breed-list')


class BreedListView(ListView):
    model = Breed


class BreedDetailView(DetailView):
    model = Breed


class BreedUpdateView(UpdateView):
    model = Breed
    template_name = 'dogs/breed_update.html'
    fields = '__all__'
    success_url = reverse_lazy('breed-list')


class BreedDeleteView(DeleteView):
    model = Breed
    template_name = 'dogs/breed_delete.html'
    success_url = reverse_lazy('breed-list')


class DogCreateView(CreateView):
    model = Dog
    template_name = 'dogs/dog_create.html'
    fields = '__all__'
    success_url = reverse_lazy('dog-list')


class DogListView(ListView):
    model = Dog


class DogDetailView(DetailView):
    model = Dog


class DogUpdateView(UpdateView):
    model = Dog
    template_name = 'dogs/dog_update.html'
    fields = '__all__'
    success_url = reverse_lazy('dog-list')


class DogDeleteView(DeleteView):
    model = Dog
    template_name = 'dogs/dog_delete.html'
    success_url = reverse_lazy('dog-list')
