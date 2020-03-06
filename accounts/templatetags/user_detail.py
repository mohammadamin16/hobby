from django import template
from films.imdbDB import search
register = template.Library()


def list_of_movies(watched_films):
    films = watched_films.all()
    titles = []
    for film in films:
        titles.append(film.title)
    if len(titles) == 0:
        return ''
    else:
        return titles


def titles_of_movies(watched_films):
    films = watched_films.all()
    titles = []
    for film in films:
        titles.append(film.title)
    return ", \n".join(titles)


def last_movie(watched_list):
    try:
        return watched_list.last().title
    except:
        return "Nothing!"


def alert_info(text):
    ALERT = """
    <div class="alert alert-info alert-dismissible fade show">
    <button type="button" class="close" data-dismiss="alert">&times;</button>
    {}
    </div>
    """.format(text)
    return ALERT


register.filter('list_of_movies', list_of_movies)
register.filter('titles_of_movies', titles_of_movies)
register.filter('last_movie', last_movie)
register.filter('alert_info', alert_info)
