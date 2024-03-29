from django.urls import path

from .views import HomeView, PlaylistsView, SongsInPlaylistView, GenresView, SongsByGenreView, ArtistsView, \
    ArtistsContentView, SongsInAlbumView, search, RegisterUser, LoginUser, logout_user, AdminEditView, AddSong, \
    SongUpdateView, SongDeleteView, diagrams

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('playlists/', PlaylistsView.as_view(), name='playlists'),
    path('playlists/<int:playlist_id>/', SongsInPlaylistView.as_view(), name = 'songs_in_playlist'),
    path('genres/', GenresView.as_view(), name='genres'),
    path('genres/<int:genre_id>/', SongsByGenreView.as_view(), name='songs_by_genre'),
    path('artists/', ArtistsView.as_view(), name='artists'),
    path('artists/<int:artist_id>/', ArtistsContentView.as_view(), name='artists_content'),
    path('albums/<int:album_id>/', SongsInAlbumView.as_view(), name='songs_in_album'),
    path('search/', search, name='search'),
    path('register/', RegisterUser.as_view(), name='sign_up'),
    path('login/', LoginUser.as_view(), name='sign_in'),
    path('logout/', logout_user, name='logout'),
    path('admin-edit/', AdminEditView.as_view(), name='admin_edit'),
    path('add-song/', AddSong.as_view(), name='add_song'),
    path('update-song/<int:song_id>/', SongUpdateView.as_view(), name='update_song'),
    path('delete-song/<int:song_id>/', SongDeleteView.as_view(), name='song_delete_confirm'),
    path('diagrams/', diagrams, name='diagrams'),
]