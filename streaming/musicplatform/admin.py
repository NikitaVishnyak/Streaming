from django.contrib import admin

from musicplatform.models import Artists, Countries, Songs, Albums, SongsArtists, Genres, Playlists, SongsPlaylists

# Register your models here.

admin.site.register(Artists)
admin.site.register(Countries)
admin.site.register(Songs)
admin.site.register(Albums)
admin.site.register(SongsArtists)
admin.site.register(Genres)
admin.site.register(Playlists)
admin.site.register(SongsPlaylists)