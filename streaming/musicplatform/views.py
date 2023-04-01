from datetime import datetime
from turtledemo.chaos import plot

from django.contrib.auth import logout, login
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import *
from .utils import *
from .forms import *

class HomeView(DataMixin, ListView):
    model = Songs
    template_name = 'musicplatform/index.html'
    context_object_name = 'songs'
    ordering = ['?']


class PlaylistsView(DataMixin, ListView):
    model = Playlists
    template_name = 'musicplatform/playlists.html'
    context_object_name = 'playlists_data'


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


class GenresView(DataMixin, ListView):
    model = Genres
    template_name = 'musicplatform/genres.html'
    context_object_name = 'genres_data'
    ordering = ['name']


class SongsByGenreView(DataMixin, ListView):
    template_name = 'musicplatform/songs_by_genre.html'
    context_object_name = 'songs'

    def get_queryset(self):
        genre_id = self.kwargs['genre_id']
        genre = Genres.objects.get(id=genre_id)
        return Songs.objects.filter(genre=genre)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        genre_id = self.kwargs['genre_id']
        context['genre'] = Genres.objects.get(id=genre_id)
        return context

class ArtistsView(DataMixin, ListView):
    model = Artists
    template_name = 'musicplatform/artists.html'
    context_object_name = 'artists'
    ordering = ['name']


class ArtistsContentView(DataMixin, ListView):
    model = Songs
    template_name = 'musicplatform/artists_content.html'
    context_object_name = 'song_list'

    def get_queryset(self):
        artist = Artists.objects.get(pk=self.kwargs['artist_id'])
        return artist.songs.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        artist = Artists.objects.get(pk=self.kwargs['artist_id'])
        context['artist'] = artist
        context['album_list'] = artist.albums.all()
        return context


class SongsInAlbumView(DataMixin, ListView):
    template_name = 'musicplatform/album.html'
    context_object_name = 'songs'

    def get_queryset(self):
        album_id = self.kwargs['album_id']
        album = Albums.objects.get(id=album_id)
        return Songs.objects.filter(album=album)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        album_id = self.kwargs['album_id']
        context['album'] = Albums.objects.get(id=album_id)
        return context

def search(request):
    query = request.GET.get('q')

    songs_result = Songs.objects.filter(name__icontains=query) | \
                 Songs.objects.filter(date__icontains=query)
    playlists_result = Playlists.objects.filter(name__icontains=query)
    artists_result = Artists.objects.filter(name__icontains=query) | \
                   Artists.objects.filter(country__name__icontains=query)
    genres_result = Genres.objects.filter(name__icontains=query)

    context = {
        'query': query,
        'songs_result': songs_result,
        'playlists_result': playlists_result,
        'artists_result': artists_result,
        'genres_result': genres_result,
    }

    if request.method == 'POST' and query != '':
        context['data'] = [*songs_result, *playlists_result, *artists_result, *genres_result]

    return render(request, 'musicplatform/search.html', context)

class SongsInPlaylistView(DataMixin, ListView):
    template_name = 'musicplatform/songs_in_playlist.html'
    context_object_name = 'songs'

    def get_queryset(self):
        playlist_id = self.kwargs['playlist_id']
        playlist = Playlists.objects.get(id=playlist_id)
        return SongsPlaylists.objects.filter(playlist=playlist)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        playlist_id = self.kwargs['playlist_id']
        context['playlist'] = Playlists.objects.get(id=playlist_id)
        return context

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'musicplatform/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'musicplatform/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')

def add_data(request):
    return HttpResponse("Add")


def is_admin_or_superuser(user):
    return user.is_authenticated and (user.is_superuser or user.is_staff)

@method_decorator(user_passes_test(is_admin_or_superuser), name='dispatch')
class AdminEditView(DataMixin, ListView):
    model = Songs
    template_name = 'musicplatform/admin_edit.html'
    context_object_name = 'songs'
    ordering = ['-id']




@method_decorator(user_passes_test(is_admin_or_superuser), name='dispatch')
class AddSong(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddSongForm
    template_name = 'musicplatform/addsong.html'
    success_url = reverse_lazy('admin_edit')
    login_url = reverse_lazy('home')
    raise_exception = True




@method_decorator(user_passes_test(is_admin_or_superuser), name='dispatch')
class SongUpdateView(DataMixin, UpdateView):
    model = Songs
    fields = ['name', 'date', 'duration', 'album', 'genre']
    template_name = 'musicplatform/edit_song.html'
    success_url = reverse_lazy('admin_edit')
    pk_url_kwarg = 'song_id'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        date = form.cleaned_data['date']
        if len(name) > 100:
            form.add_error('name', 'Name cannot be longer than 100 characters.')
            return super().form_invalid(form)
        elif Songs.objects.filter(name=name).exclude(pk=self.object.pk).exists():
            form.add_error('name', 'Name must be unique.')
            return super().form_invalid(form)
        elif date > date.today():
            form.add_error('date', 'The date cannot be in the future.')
            return super().form_invalid(form)
        duration = form.cleaned_data['duration']


        try:
            duration_time = datetime.strptime(duration, '%M:%S').time()
        except ValueError:
            form.add_error('duration', 'Incorrect duration.')
            return super().form_invalid(form)
        if duration_time <= datetime.strptime('00:00', '%M:%S').time():
            form.add_error('duration', 'Duration must be greater than 0.')
            return super().form_invalid(form)
        return super().form_valid(form)


@method_decorator(user_passes_test(is_admin_or_superuser), name='dispatch')
class SongDeleteView(DataMixin, DeleteView):
    model = Songs
    template_name = 'musicplatform/song_delete_confirm.html'
    success_url = reverse_lazy('admin_edit')
    pk_url_kwarg = 'song_id'


from django.shortcuts import render
import plotly.graph_objs as go
from .models import Songs, Artists
import pandas as pd
from django.db.models import Count

@user_passes_test(lambda u: u.is_staff or u.is_superuser)
def diagrams(request):
    # Query to get the count of songs per genre
    genre_count = Songs.objects.values('genre__name').annotate(count=Count('id'))

    # Convert to pandas dataframe
    genre_count_df = pd.DataFrame.from_records(genre_count)

    # Plot pie chart with genre counts
    fig1 = go.Figure(data=[go.Pie(labels=genre_count_df['genre__name'], values=genre_count_df['count'])])

    # Query to get the count of artists per country
    artist_count = Artists.objects.values('country__name').annotate(count=Count('id'))

    # Convert to pandas dataframe
    artist_count_df = pd.DataFrame.from_records(artist_count)

    # Plot bar chart with country counts
    fig2 = go.Figure(data=[go.Bar(x=artist_count_df['country__name'], y=artist_count_df['count'])])

    context = {
        'piechart': fig1.to_html(full_html=False),
        'barchart': fig2.to_html(full_html=False),
        'title': 'SoundWave',
    }

    return render(request, 'musicplatform/diagrams.html', context)
