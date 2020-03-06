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
    path('remove-from-watched/<movie_id>', views.RemoveFromWatched.as_view(), name='remove-from-watched'),
    path('remove-from-favs/<movie_id>', views.RemoveFromFavs.as_view(), name='remove-from-favs'),
    path('add-to-fav/<movie_id>', views.AddToFav.as_view(), name='add-to-fav'),
    path('search', views.FindPeopleView.as_view(), name='find-people'),
    path('add-to-requested/<username>', views.AddToRequested.as_view(), name='add-to-requested'),
    path('notification', views.NotificationView.as_view(), name='notification'),
    path('add-to-friends/<username>', views.AddToFriends.as_view(), name='add-to-friends'),
    path('reject/<username>', views.Reject.as_view(), name='reject'),
]
