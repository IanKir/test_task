from django.contrib import admin

from .models import Breed, Dog


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    pass


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    pass
