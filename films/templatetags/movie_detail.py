from django import template
from films.imdbDB import search
register = template.Library()


def get_poster(movie_id):
    """Return the Poster url of the given imdbID"""
    return search.get_poster(movie_id)



register.filter('get_poster', get_poster)
