"""
Search & access to imdb DataBase directly.
"""
from imdb import IMDb


def search(query:str):
    imdb = IMDb()
    response = imdb.search_movie_advanced(query, results=7)
    results = []
    for movie in response:
        m = (movie.getID(), movie['title'])
        results.append(m)

    print("RESULTS :", results)
    return results


def get_title(movie_id: int, list_of_ids:list):
    print("____Starting new Thread", movie_id)
    imdb = IMDb()
    response = imdb.get_movie(movie_id)
    title = response['title']
    list_of_ids.append(title)
    print("____I GOT IT!", title)


def get_poster(movie_id: int):
    imdb = IMDb()
    response = imdb.get_movie(movie_id)
    img_url = response.get_fullsizeURL()
    return img_url
