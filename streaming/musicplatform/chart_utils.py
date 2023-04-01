import plotly.express as px
import pandas as pd
from django.db.models import Count
from .models import *

# Query to get the count of songs per genre
genre_count = Songs.objects.values('genre__name').annotate(count=Count('id'))

# Convert to pandas dataframe
genre_count_df = pd.DataFrame.from_records(genre_count)

# Plot pie chart with genre counts
fig1 = px.pie(genre_count_df, values='count', names='genre__name')

# Query to get the count of artists per country
artist_count = Artists.objects.values('country__name').annotate(count=Count('id'))

# Convert to pandas dataframe
artist_count_df = pd.DataFrame.from_records(artist_count)

# Plot bar chart with country counts
fig2 = px.bar(artist_count_df, x='country__name', y='count')

# You can then pass the plots to your template context and render them in your html page
