from django import template
from films.imdbDB import search
register = template.Library()


def list_of_movies(watched_films):
    films = watched_films.all()
    titles = []
    for film in films:
        titles.append(film.title)
    return ", \n".join(titles)


def alert_info(text):
    ALERT = """
    <div class="alert alert-info alert-dismissible fade show">
    <button type="button" class="close" data-dismiss="alert">&times;</button>
    {}
    </div>
    """.format(text)
    return ALERT


register.filter('list_of_movies', list_of_movies)
register.filter('alert_info', alert_info)
