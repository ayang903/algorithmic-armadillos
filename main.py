import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import statistics

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
anish_var.update_layout(
    xaxis_title="Source", yaxis_title="Score"
)
#anish_var.show()
st.plotly_chart(anish_var)

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

st.plotly
#Navy
ep_v_score = px.scatter(df, x = df['episodes'], y = df['score'], color = 'type', title = 'The Number of Episodes V. The Score')

navy_explaination = "Overall, there isn't much to conclude from the relationship between the score and number of episodes anime or manga has. All types tended to have higher scores as their number of episodes, part, movies, etc increased but there isn't a difinitive trend as many manga/anime with fewer episodes had the higher scores."
st.write(navy_explaination)


#Alexia
daf_themes = df['themes'].value_counts()
themedf = df['themes'].value_counts().head(10)
alexiavar1 = px.bar(themedf, title='Top Ten Themes of Anime')
st.plotly_chart()

musicdf = df[df['themes'] == "['Music']"]['status'].value_counts()
alexiavar2 = px.pie(df, values = musicdf.values, names=musicdf.index)

schooldf = df[df['themes'] == "['School']"]['status'].value_counts()
alexiavar3 = px.pie(df, values = schooldf.values, names=schooldf.index)

mechadf = df[df['themes'] == "['Mecha']"]['status'].value_counts()
alexiavar4 = px.pie(df, values = mechadf.values, names=mechadf.index)

historicaldf = df[df['themes'] == "['Historical']"]['status'].value_counts()
alexiavar5 = px.pie(df, values = historicaldf.values, names=historicaldf.index)

explanation = 'According to the above bar graph, the top four themes for anime are Music, School, Mecha, and Historical. The four pie charts visually show us about what percent of the anime with these themes are currently airing or have finished airing. As a result, it is shown the anime with the Historical and Mecha themes have finished airing, while there are still some anime airing with the Music and School themes. Thus, these pie charts show that anime with Music and School themes are more likely to be currently airing than those with Mecha and Historical themes.'
st.write(explanation)

#Izaac
score_v_scored = px.scatter(x = df['scored_by'], y = df['score'], title = 'Number of Scores vs. Score')
#This graph show a general exponetial curve that the more views a show has the higher it is rated. One can assume that this is because the better shows will be more popular
scores = px.histogram(df, x = df['score'])
#This graph shows the most common scores for shows. This graph shows a pretty perfect standard deviation with the average score of a show being about 6.6