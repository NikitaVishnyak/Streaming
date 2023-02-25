from django.db import models
from django.urls import reverse


# Create your models here.

class Artists(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey('Countries', related_name='artists', on_delete=models.CASCADE, null=False)
    songs = models.ManyToManyField('Songs', through='SongsArtists', related_name='artists')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('artists_content', kwargs={'artist_id': self.pk})

    class Meta:
        verbose_name_plural = 'Artists'

class Countries(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'


class Albums(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey('Artists', related_name='albums', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('songs_in_album', kwargs={'album_id': self.pk})

    class Meta:
        verbose_name_plural = 'Albums'


class Songs(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(default='1900-01-01')
    duration = models.CharField(default="00:00", max_length=20)
    album = models.ForeignKey('Albums', related_name='songs', on_delete=models.CASCADE, null=False)
    genre = models.ForeignKey('Genres', related_name='songs', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Songs'


class SongsArtists(models.Model):
    song = models.ForeignKey('Songs', on_delete=models.CASCADE, null=False)
    artist = models.ForeignKey('Artists', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'Song: {self.song}; Artist: {self.artist}'

    class Meta:
        verbose_name_plural = 'Songs artists'


class Genres(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('songs_by_genre', kwargs={'genre_id': self.pk})

    class Meta:
        verbose_name_plural = 'Genres'


class Playlists(models.Model):
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField('Songs', through='SongsPlaylists', related_name='playlists')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('songs_in_playlist', kwargs={'playlist_id': self.pk})

    class Meta:
        verbose_name_plural = 'Playlists'


class SongsPlaylists(models.Model):
    song = models.ForeignKey('Songs', on_delete=models.CASCADE, null=False)
    playlist = models.ForeignKey('Playlists', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'Song: {self.song}; Playlist: {self.playlist}'

    class Meta:
        verbose_name_plural = 'Songs playlists'