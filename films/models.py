from django.db import models


class Film(models.Model):
    title = models.CharField(max_length=100)
    year  = models.IntegerField()
    imdbId = models.CharField(max_length=100)

    def __str__(self):
        return self.title