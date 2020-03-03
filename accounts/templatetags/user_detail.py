from django import template
from films.imdbDB import search
register = template.Library()


def list_of_movies(watched_films):
    films = watched_films.all()
    titles = []
    for film in films:
        titles.append(film.title)
    return ", \n".join(titles)


register.filter('list_of_movies', list_of_movies)
