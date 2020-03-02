from django import template
from films.imdbDB import search
register = template.Library()


def get_title(id_of_movie):
    """Returns & Find the Title of the movie by a ID"""
    response = search.get_title(id_of_movie)
    return response


register.filter('get_title', get_title)