from django.contrib import admin

from musicplatform.models import *

class SongsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'duration', 'album', 'genre')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'date', 'duration', 'genre')

class ArtistsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    list_display_links = ('id', 'name', 'country')
    search_fields = ('name', 'country')

class CountriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class AlbumsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'artist')
    list_display_links = ('id', 'name', 'artist')
    search_fields = ('name', 'date', 'artist')

class GenresAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class PlaylistsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class SongsArtistsAdmin(admin.ModelAdmin):
    list_display = ('id', 'song', 'artist')
    list_display_links = ('id', 'song', 'artist')
    search_fields = ('song', 'artist')

class SongsPlaylistsAdmin(admin.ModelAdmin):
    list_display = ('id', 'song', 'playlist')
    list_display_links = ('id', 'song', 'playlist')
    search_fields = ('song', 'playlist')

admin.site.register(Artists, ArtistsAdmin)
admin.site.register(Countries, CountriesAdmin)
admin.site.register(Songs, SongsAdmin)
admin.site.register(Albums, AlbumsAdmin)
admin.site.register(SongsArtists, SongsArtistsAdmin)
admin.site.register(Genres, GenresAdmin)
admin.site.register(Playlists, PlaylistsAdmin)
admin.site.register(SongsPlaylists, SongsPlaylistsAdmin)