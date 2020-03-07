from django.contrib import admin

from films.models import  People
from films.models import  Film, Suggest

admin.site.register(Film)
admin.site.register(Suggest)
admin.site.register(People)