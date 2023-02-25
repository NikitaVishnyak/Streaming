from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

def index(request):
    songs = Songs.objects.order_by('?')
    context = {
        'songs': songs,
        'title': 'SoundWave'
    }
    return render(request, 'musicplatform/index.html', context=context)
def playlists(request):
    playlists = Playlists.objects.all()
    playlists_data = []
    for playlist in playlists:
        songs = SongsPlaylists.objects.filter(playlist=playlist).select_related('song')
        playlists_data.append({'playlist': playlist, 'songs': songs})
    context = {
        'playlists_data': playlists_data,
        'title': 'SoundWave',
    }
    return render(request, 'musicplatform/playlists.html', context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def genres(request):
    genres = Genres.objects.order_by('name')
    context = {
        'genres': genres,
        'title': 'SoundWave'
    }
    return render(request, 'musicplatform/genres.html', context=context)

def songs_by_genre(request, genre_id):
    songs = Songs.objects.filter(genre_id=genre_id)
    genre = Genres.objects.filter(id=genre_id)
    context = {
        'songs': songs,
        'genre': genre,
        'title': 'SoundWave',
    }

    return render(request, 'musicplatform/songs_by_genre.html', context=context)

def artists(request):
    artists = Artists.objects.order_by('name')
    context = {
        'artists': artists,
        'title': 'SoundWave',
    }
    return render(request, 'musicplatform/artists.html', context=context)


def artists_content(request, artist_id):
    artist = Artists.objects.filter(id=artist_id)
    albums = Albums.objects.filter(artist=artist_id)
    a = Artists.objects.get(pk=artist_id)
    songs = a.songs.all()


    context = {
        'albums': albums,
        'title': 'SoundWave',
        'artist': artist,

        'songs': songs,

    }

    return render(request, 'musicplatform/artists_content.html', context=context)

def songs_in_album(request, album_id):
    songs = Songs.objects.filter(album_id=album_id)
    album = Albums.objects.filter(id=album_id)
    context = {
        'songs': songs,
        'album': album,
        'title': 'SoundWave',
    }

    return render(request, 'musicplatform/album.html', context=context)

def search(request):
    query = request.GET.get('query')

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

def songs_in_playlist(request, playlist_id):
    playlist = Playlists.objects.filter(id=playlist_id)

    p = Playlists.objects.get(pk=playlist_id)
    songs = p.songs.all()

    context = {
        'title': 'SoundWave',
        'playlist': playlist,

        'songs': songs,
    }

    return render(request, 'musicplatform/songs_in_playlist.html', context=context)