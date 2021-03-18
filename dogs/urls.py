from django.urls import path
from . import views

urlpatterns = [
    path('breeds/search/', views.BreedSearchView.as_view(), name='breed-search'),
    path('breeds/create/', views.BreedCreateView.as_view(), name='breed-create'),
    path('breeds/', views.BreedListView.as_view(), name='breed-list'),
    path('breeds/<slug:slug>/', views.BreedDetailView.as_view(), name='breed-detail'),
    path('breeds/<slug:slug>/update/', views.BreedUpdateView.as_view(), name='breed-update'),
    path('breeds/<slug:slug>/delete/', views.BreedDeleteView.as_view(), name='breed-delete'),
]
