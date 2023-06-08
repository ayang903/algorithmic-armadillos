import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

st.title("Anime EDA")
st.markdown("Here is our EDA on Anime!")

df = pd.read_csv('https://raw.githubusercontent.com/ayang903/algorithmic-armadillos/main/anime.csv')

st.dataframe(df)
columns_drop = ['broadcast_day', 'broadcast_time', 'background', 'trailer_url', 'title_english']
df.drop(columns_drop, axis=1, inplace=True)
df.dropna(subset = ['score', 'source'], inplace=True)

#Anish
score_dict = {}
for i in df['source'].unique():
  source = df[df['source'] == i]
  avg_score = statistics.mean(source['score'])
  score_dict[i] = avg_score
sorted_score_dict = sorted(score_dict.items(), key = lambda x:x[1], reverse = True)
final_dict = dict(sorted_score_dict)
final_dict

import plotly.express as px
anish_var = px.bar(x = final_dict.keys(),
             y = final_dict.values(),
             title="Anime Source Content Effect on Scores")
anish_var.update_layout(yaxis_range=[0,10])
anish_var.update_layout(
    yaxis = dict(
        tickmode = 'linear',
        tick0 = 0,
        dtick = 0.5
    )
)
fig.update_layout(
    xaxis_title="Source", yaxis_title="Score"
)
fig.show()


#Amelia

grouped_df = df.groupby('type')['score'].mean()

grouped_df = grouped_df.sort_values(ascending=False)

ameliaVar = px.bar(
    x = grouped_df.index,
    y = grouped_df.values,
    color = grouped_df.values,
)

ameliaVar.update_layout (
    title ='Average Score by Media Type',
    xaxis_title = "Media Type",
    yaxis_title = "Average Score"

)

ameliaVar.update_yaxes(range = [ 5.5, 7])


#Navy
ep_v_score = px.scatter(df, x = df['episodes'], y = df['score'], color = 'type', title = 'The Number of Episodes V. The Score')


#Alexia
daf_themes = df['themes'].value_counts()
themedf = df['themes'].value_counts().head(10)
alexiavar1 = px.bar(themedf, title='Top Ten Themes of Anime')

musicdf = df[df['themes'] == "['Music']"]['status'].value_counts()
alexiavar2 = px.pie(df, values = musicdf.values, names=musicdf.index)

schooldf = df[df['themes'] == "['School']"]['status'].value_counts()
alexiavar3 = px.pie(df, values = schooldf.values, names=schooldf.index)

mechadf = df[df['themes'] == "['Mecha']"]['status'].value_counts()
alexiavar4 = px.pie(df, values = mechadf.values, names=mechadf.index)

historicaldf = df[df['themes'] == "['Historical']"]['status'].value_counts()
alexiavar5 = px.pie(df, values = historicaldf.values, names=historicaldf.index)

#Izaac
score_v_scored = px.scatter(x = df['scored_by'], y = df['score'], title = 'Number of Scores vs. Score')
#This graph show a general exponetial curve that the more views a show has the higher it is rated. One can assume that this is because the better shows will be more popular
scores = px.histogram(df, x = df['score'])
#This graph shows the most common scores for shows. This graph shows a pretty perfect standard deviation with the average score of a show being about 6.6