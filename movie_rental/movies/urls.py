from django.urls import path
from .views import (
    MovieListView,
    MovieDetailView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
    UserPageView,
)

urlpatterns = [
    path('', MovieListView.as_view(), name='movie-list'),
    path('movie-detail/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('create-movie/', MovieCreateView.as_view(), name='create-movie'),
    path('update-movie/<int:pk>/', MovieUpdateView.as_view(), name='update-movie'),
    path('delete-movie/<int:pk>/', MovieDeleteView.as_view(), name='delete-movie'),
    path('user-page/', UserPageView.as_view(), name='user-page'),
]
