"""
Search & access to imdb DataBase directly.
"""
from imdb import IMDb


def search(query: str):
    imdb = IMDb()
    response = imdb.search_movie_advanced(query, sort='votes', results=10)
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


def get_info(movie_id: str):
    ia = IMDb()
    movie = ia.get_movie(movie_id)
    title = movie.get("title")
    year = movie.get("year")
    cast_people = movie.get('cast')[0:5]
    cast_names = []
    for c in cast_people:
        cast_names.append(c.get('name'))
    cast = " ".join(cast_names)
    countries = " ".join(movie.get('countries'))
    try:
        box_office = movie.get("box office")['Budget']
    except TypeError:
        box_office = 0
    rating = movie.get('rating')
    votes = movie.get('votes')
    cover_url = movie.get("cover url")
    writer_people = movie.get('writer')
    write_names = []
    for w in writer_people:
        write_names.append(w.get('name'))
    writer = " ".join(write_names)

    director_people = movie.get('director')
    director_names = []
    for d in director_people:
        director_names.append(d.get('name'))
    director = " ".join(director_names)

    top_250_films = 0 if str(movie.get('top 250 films')) == 'None' else movie.get('top 250 films')
    synopsis = movie.get('synopsis')[0][:500] + "..."

    info = dict(
        title=title,
        imdbId=movie_id,
        year=year,
        cast=cast,
        countries=countries,
        box_office=box_office,
        rating=rating,
        votes=votes,
        cover_url=cover_url,
        writer=writer,
        director=director,
        top_250_films=top_250_films,
        synopsis=synopsis
    )
    return info
