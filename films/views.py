from django.shortcuts import render
from django.views.generic import FormView, ListView
from django.views.generic.edit import FormMixin
from films.imdbDB import search
import threading

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
        print("before Id")
        if form.is_valid():
            list_of_movies = form.send_query()
        print("After IDs")

        # threads_list = []
        list_of_titles = []
        for movie in list_of_movies:
            list_of_titles.append(movie[1])
        # for movie_id in list_of_ids:
        #     t = threading.Thread(target=search.get_title, args=(movie_id, list_of_titles))
        #     threads_list.append(t)
        # print("Before Starting Threads")
        # for x in threads_list:
        #     x.start()
        # print("After Starting Threads")
        # for x in threads_list:
        #     x.join()
        # print("FINISH")
        return render(request, self.template_name, {'form': form, 'list_of_titles': list_of_titles})
