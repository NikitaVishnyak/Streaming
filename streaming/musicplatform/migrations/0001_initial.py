# Generated by Django 4.1.6 on 2023-02-08 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Countries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Playlists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('duration', models.CharField(default='00:00', max_length=20)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='musicplatform.albums')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='musicplatform.genres')),
            ],
        ),
        migrations.CreateModel(
            name='SongsPlaylists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicplatform.playlists')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicplatform.songs')),
            ],
        ),
        migrations.CreateModel(
            name='SongsArtists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicplatform.artists')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicplatform.songs')),
            ],
        ),
        migrations.AddField(
            model_name='artists',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artists', to='musicplatform.countries'),
        ),
        migrations.AddField(
            model_name='artists',
            name='songs',
            field=models.ManyToManyField(related_name='artists', through='musicplatform.SongsArtists', to='musicplatform.songs'),
        ),
        migrations.AddField(
            model_name='albums',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='musicplatform.artists'),
        ),
    ]