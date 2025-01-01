# movies/views.py
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView, DetailView, DeleteView
from django.http import HttpResponse
from .models import Movie
from .forms import MovieForm
from django.urls import reverse_lazy

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'movies'

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'

class MovieCreateView(View):
    template_name = 'movies/create_movie.html'

    def get(self, request):
        form = MovieForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movie-list')
        return render(request, self.template_name, {'form': form})

class MovieUpdateView(View):
    template_name = 'movies/update_movie.html'

    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        form = MovieForm(instance=movie)
        return render(request, self.template_name, {'form': form, 'movie': movie})

    def post(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie-list')
        return render(request, self.template_name, {'form': form, 'movie': movie})

class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'movies/movie_confirm_delete.html'
    success_url = reverse_lazy('movie-list')

class UserPageView(View):
    def get(self, request):
        return render(request, 'movies/user_page.html')
