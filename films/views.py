from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView, RedirectView
from django.views.generic.edit import FormMixin
from films.imdbDB import search
from django.http import HttpResponseRedirect

from films.models import Film
from . import forms


class SearchView(FormMixin, ListView):
    template_name = 'films/search.html'
    form_class = forms.SearchForm
    success_url = '#'


    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        last_searched = Film.objects.order_by('-search_time')[:5]


        return render(request, self.template_name, {'form': form, 'list_of_films': last_searched})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        list_of_ids = []
        if form.is_valid():
            list_of_ids = form.send_query()

        list_of_films = []
        for imdbid in list_of_ids:
            try:
                film = Film.objects.get(imdbId=imdbid)
                film.search_time += 1
                film.save()
            except Film.DoesNotExist:
                film = Film.objects.create(
                    **search.get_info(str(imdbid))
                )
                film.search_time += 1
                film.save()

            list_of_films.append(film)

        return render(request, self.template_name, {'form': form, 'list_of_films': list_of_films})


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


class FilmViewRedirector(RedirectView):

    def get(self, request, *args, **kwargs):
        title = self.kwargs['movie_title']
        film = Film.objects.get(title=title)
        return HttpResponseRedirect(reverse_lazy('films:film-view', kwargs={'movie_id':film.imdbId}))
