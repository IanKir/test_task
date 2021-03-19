from django.urls import path
from . import views

urlpatterns = [
    path('breeds/search/', views.BreedSearchView.as_view(), name='breed-search'),
    path('breeds/create/', views.BreedCreateView.as_view(), name='breed-create'),
    path('breeds/', views.BreedListView.as_view(), name='breed-list'),
    path('breeds/<slug:slug>/', views.BreedDetailView.as_view(), name='breed-detail'),
    path('breeds/<slug:slug>/update/', views.BreedUpdateView.as_view(), name='breed-update'),
    path('breeds/<slug:slug>/delete/', views.BreedDeleteView.as_view(), name='breed-delete'),

    path('dogs/create/', views.DogCreateView.as_view(), name='dog-create'),
    path('dogs/', views.DogListView.as_view(), name='dog-list'),
    path('dogs/<slug:slug>/', views.DogDetailView.as_view(), name='dog-detail'),
    path('dogs/<slug:slug>/update/', views.DogUpdateView.as_view(), name='dog-update'),
    path('dogs/<slug:slug>/delete/', views.DogDeleteView.as_view(), name='dog-delete'),
]
