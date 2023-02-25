from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('playlists/', playlists, name='playlists'),
    path('playlists/<int:playlist_id>/', songs_in_playlist, name = 'songs_in_playlist'),
    path('genres/', genres, name='genres'),
    path('genres/<int:genre_id>/', songs_by_genre, name='songs_by_genre'),
    path('artists/', artists, name='artists'),
    path('artists/<int:artist_id>/', artists_content, name='artists_content'),
    path('albums/<int:album_id>/', songs_in_album, name='songs_in_album'),
    path('search/', search, name='search'),
]