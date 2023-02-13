from django.db import models


# Create your models here.

class Artists(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey('Countries', related_name='artists', on_delete=models.CASCADE, null=False)
    songs = models.ManyToManyField('Songs', through='SongsArtists', related_name='artists')

    def __str__(self):
        return self.name


class Countries(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Albums(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey('Artists', related_name='albums', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class Songs(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(default='1900-01-01')
    duration = models.CharField(default="00:00", max_length=20)
    album = models.ForeignKey('Albums', related_name='songs', on_delete=models.CASCADE, null=False)
    genre = models.ForeignKey('Genres', related_name='songs', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name


class SongsArtists(models.Model):
    song = models.ForeignKey('Songs', on_delete=models.CASCADE, null=False)
    artist = models.ForeignKey('Artists', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'Song: {self.song}; Artist: {self.artist}'


class Genres(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Playlists(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SongsPlaylists(models.Model):
    song = models.ForeignKey('Songs', on_delete=models.CASCADE, null=False)
    playlist = models.ForeignKey('Playlists', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'Song: {self.song}; Playlist: {self.playlist}'




