from django.urls import path
from accounts import views

app_name = 'accounts'


urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('page/<username>', views.PageView.as_view(), name='user-page'),
    path('edit', views.EditProfileView.as_view(), name='user-edit'),
    path('add-to-watched/<movie_id>', views.AddToWatched.as_view(), name='add-to-watched'),
    path('add-to-fav/<movie_id>', views.AddToFav.as_view(), name='add-to-fav'),
    path('search', views.FindPeopleView.as_view(), name='find-people'),
]
