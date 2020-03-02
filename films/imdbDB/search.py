"""
Search & access to imdb DataBase directly.
"""
from imdb import IMDb


def search(query: str):
    imdb = IMDb()
    response = imdb.search_movie_advanced(query, results=10)
    results = []
    for movie in response:
        m = (movie.getID(), movie['title'])
        results.append(m)

    return results


def get_title(movie_id: int):
    imdb = IMDb()
    response = imdb.get_movie(movie_id)
    title = response['title']
    return title


def get_poster(movie_id: int):
    imdb = IMDb()
    response = imdb.get_movie(movie_id)
    img_url = response.get_fullsizeURL()
    return img_url
