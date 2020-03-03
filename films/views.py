from django.shortcuts import render
from django.views.generic import FormView, ListView, DetailView
from django.views.generic.edit import FormMixin
from films.imdbDB import search
import threading

from films.models import Film
from . import forms


class SearchView(FormMixin, ListView):
    template_name = 'films/search.html'
    form_class = forms.SearchForm
    success_url = '#'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        list_of_movies = []
        if form.is_valid():
            list_of_movies = form.send_query()

        return render(request, self.template_name, {'form': form, 'list_of_movies': list_of_movies})


class FilmView(DetailView):
    template_name = 'films/film_view.html'
    model = Film
    context_object_name = 'film'


    def get_object(self, queryset=None):
        movie_id = self.kwargs['movie_id']
        try:
            film = Film.objects.get(imdbId=movie_id)
        except Film.DoesNotExist:
            film = Film.objects.create(
                **search.get_info(str(movie_id))
            )
        return film
