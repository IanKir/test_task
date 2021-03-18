from django.db.models import Q
from django.urls import reverse_lazy

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
