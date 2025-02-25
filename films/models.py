from django.db import models

from accounts.models import Comment


class Film(models.Model):
    title = models.CharField(max_length=100)
    imdbId = models.CharField(primary_key=True, max_length=100)
    year  = models.IntegerField()
    # cast = models.ManyToManyField('People',related_name='cast')
    cast = models.CharField(max_length=200)
    countries = models.CharField(max_length=100)
    box_office = models.CharField(max_length=100,default=0)
    rating = models.FloatField()
    votes = models.IntegerField()
    cover_url = models.URLField()
    fullsize_poster = models.URLField()
    # kind = models.CharField(max_length=100)
    # writer = models.ManyToManyField('People', related_name='writer')
    writer = models.CharField(max_length=200)
    # director = models.ManyToManyField('People', related_name='director')
    director = models.CharField(max_length=200)
    top_250_films = models.IntegerField()
    # production_companies = models.CharField(max_length=150)
    synopsis = models.TextField()

    search_time = models.IntegerField(default=0)

    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return self.title


class People(models.Model):
    name = models.CharField(max_length=100)
    imdbId = models.CharField(max_length=100, primary_key=True)



class Suggest(models.Model):
    suggester = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    film = models.ForeignKey('films.Film', on_delete=models.CASCADE)
    text = models.CharField(max_length=500)




