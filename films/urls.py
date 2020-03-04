from django.urls import path
from films import views

app_name = 'films'


urlpatterns = [
    path('search', views.SearchView.as_view(), name='search'),
    path('film-view/<movie_id>', views.FilmView.as_view(), name='film-view'),
    path('film-view/find-film/<movie_title>', views.FilmViewRedirector.as_view(), name='film-redirector'),
]
