import pandas as pd
import plotly.express as px


df = pd.read_csv('most_subscribed_youtube_channels.csv')


df['subscribers'] = df['subscribers'].str.replace(',', '', regex=False).astype(int)

df['started'] = pd.to_numeric(df['started'], errors='coerce')

fig = px.histogram(df, x='subscribers', title='Subscriber Count')
fig.show()

fig = px.pie(df, values='subscribers', names='category', title='YouTube Categories')
fig.show()

fig = px.box(df, y='started', title='Years Started')
fig.show()
