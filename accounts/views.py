from django.conf import settings
from django.contrib.auth import logout, login
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import FormView, DetailView, RedirectView, CreateView, TemplateView, ListView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import FormMixin

from accounts.forms import SighUpForm
from accounts.models import User
from films.models import Film
from hobby import urls


class SignUpView(FormView):
    def get(self, request, *args, **kwargs):
        form = SighUpForm()

        return render(request, 'accounts/signup.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = SighUpForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                name = form.cleaned_data['full_name']
                user = User.objects.create(
                    username=username,
                    password=password,
                    name=name)
                user.set_password(password)
                user.save()
                return HttpResponseRedirect(reverse_lazy('accounts:login'))

        return HttpResponseRedirect(reverse_lazy('home'))


class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        login(self.request, form.get_user())

        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class AddToWatched(RedirectView):

    def get(self, request, *args, **kwargs):
        movie_id = self.kwargs['movie_id']
        film = Film.objects.get(imdbId=movie_id)
        self.request.user.watched_films.add(film)
        self.request.user.save()
        return super(AddToWatched, self).get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('films:film-view', kwargs={'movie_id': self.kwargs['movie_id']})



class AddToFav(RedirectView):
    url = reverse_lazy('accounts:profile')

    def get(self, request, *args, **kwargs):
        movie_id = self.kwargs['movie_id']
        film = Film.objects.get(imdbId=movie_id)
        self.request.user.fav_list.add(film)
        self.request.user.save()
        return super(AddToFav, self).get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('films:film-view', kwargs={'movie_id': self.kwargs['movie_id']})



class RemoveFromWatched(RedirectView):

    def get(self, request, *args, **kwargs):
        movie_id = self.kwargs['movie_id']
        film = Film.objects.get(imdbId=movie_id)
        self.request.user.watched_films.remove(film)
        self.request.user.save()
        return super(RemoveFromWatched, self).get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('films:film-view', kwargs={'movie_id': self.kwargs['movie_id']})


class RemoveFromFavs(RedirectView):
    def get(self, request, *args, **kwargs):
        movie_id = self.kwargs['movie_id']
        film = Film.objects.get(imdbId=movie_id)
        self.request.user.fav_list.remove(film)
        self.request.user.save()
        return super(RemoveFromFavs, self).get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('films:film-view', kwargs={'movie_id': self.kwargs['movie_id']})


class ProfileView(DetailView):
    template_name = 'accounts/profile.html'

    def get_object(self, queryset=None):
        user = User.objects.get(username=self.request.user.username)
        return user


class PageView(DetailView):
    template_name = 'accounts/page.html'

    def get_object(self, queryset=None):
        user = User.objects.get(username=self.kwargs['username'])
        return user


class EditProfileView(FormMixin, DetailView):
    template_name = 'accounts/edit-profile.html'
    context_object_name = 'u'

    def get_context_data(self, **kwargs):
        # context = super(EditProfileView, self).get_context_data(**kwargs)
        context = dict()
        context[self.context_object_name] = self.get_object()
        return context

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, self.get_context_data())


    def get_object(self, queryset=None):
        user = User.objects.get(username=self.request.user.username)
        return user

    def post(self, request, *args, **kwargs):
        user = self.request.user

        fullname = self.request.POST['name']
        bio      = self.request.POST['bio']
        try:
            avatar   = self.request.FILES['avatar']
        except MultiValueDictKeyError:
            avatar = user.avatar


        user.avatar = avatar
        user.name = fullname
        user.bio = bio
        user.save()

        return HttpResponseRedirect(reverse_lazy('accounts:profile'))


class FindPeopleView(FormMixin, ListView):
    template_name = 'accounts/find_people.html'

    def post(self, request, *args, **kwargs):
        query = self.request.POST['query']
        results = User.objects.filter(name__contains=query)
        return render(request, self.template_name, {'results': results})


class AddToRequested(RedirectView):

    def get(self, request, *args, **kwargs):
        requested_friend_username = self.kwargs['username']
        requested_friend = User.objects.get(username=requested_friend_username)
        user = User.objects.get(username=self.request.user.username)
        requested_friend.requested_users.add(user)
        requested_friend.save()
        return super(AddToRequested, self).get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('accounts:user-page', kwargs={'username': self.kwargs['username']})


class NotificationView(FormMixin, ListView):
    template_name = 'accounts/notification-view.html'

    def get(self, request, *args, **kwargs):
        user = self.request.user
        results = user.requested_users.all()
        return render(request, self.template_name, {'results': results})


class AddToFriends(RedirectView):

    def get(self, request, *args, **kwargs):
        user = self.request.user
        friend_username = self.kwargs['username']
        friend = User.objects.get(username=friend_username)
        user.friends.add(friend)
        user.requested_users.remove(friend)
        user.save()
        return super(AddToFriends, self).get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('accounts:notification')


class Reject(RedirectView):

    def get(self, request, *args, **kwargs):
        user = self.request.user
        friend_username = self.kwargs['username']
        friend = User.objects.get(username=friend_username)
        user.requested_users.remove(friend)
        user.save()
        return super(Reject, self).get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('accounts:notification')


