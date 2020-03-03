from django.contrib import admin

from films.models import  People
from films.models import  Film

admin.site.register(Film)
admin.site.register(People)