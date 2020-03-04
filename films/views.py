from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, DetailView, RedirectView
from django.views.generic.edit import FormMixin

from accounts.forms import CommentForm
from accounts.models import Comment
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


class FilmView(FormMixin, DetailView):
    template_name = 'films/film_view.html'
    model = Film
    context_object_name = 'film'
    form_class = CommentForm


    def get_context_data(self, **kwargs):
        context = super(FilmView, self).get_context_data(**kwargs)
        context['form'] = self.form_class(initial=self.initial)
        movie_id = self.kwargs['movie_id']
        comments = Film.objects.get(imdbId=movie_id).comments.all()
        context['comments'] = comments
        return context


    def get_object(self, queryset=None):
        movie_id = self.kwargs['movie_id']
        try:
            film = Film.objects.get(imdbId=movie_id)
        except Film.DoesNotExist:
            film = Film.objects.create(
                **search.get_info(str(movie_id))
            )
        return film

    def post(self, request, *args, **kwargs):
        movie_id = self.kwargs['movie_id']
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = Comment.objects.create(
                text=form.cleaned_data['text'],
                writer=request.user
            )
            comment.save()
            film = Film.objects.get(imdbId=movie_id)
            film.comments.add(comment)
            return HttpResponseRedirect(reverse_lazy('films:film-view', kwargs={'movie_id':movie_id}))


class FilmViewRedirector(RedirectView):

    def get(self, request, *args, **kwargs):
        title = self.kwargs['movie_title']
        film = Film.objects.get(title=title)
        return HttpResponseRedirect(reverse_lazy('films:film-view', kwargs={'movie_id':film.imdbId}))
