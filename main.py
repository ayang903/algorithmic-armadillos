import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import statistics

st.title("Anime EDA")
st.markdown("Here is our EDA on Anime!")

anish_bio = 'My name is Anish and I am a rising junior in high school. My prior experience in coding consists of a little experimentation in Python but nothing advanced. I hope to learn and advance within the field in the coming years.'
st.write(anish_bio)

amelia_bio = 'My name is Amelia, and this coming school year I will be a Junior in highschool. Prior to this course, I have little coding experience. However, I wish to continue to deepen my understanding of the subject.'
st.write(amelia_bio)

alexia_bio = 'My name is Alexia, and I will be going into my freshman year of college this Fall in 2023. My prior experience with coding includes the course of AP Computer Science Principles my junior year of high school, a Summer Immersion Program hosted by Girls Who Code, and a Self-Paced Program also hosted by Girls Who Code. The Self-Paced Program included courses on web development, web design, and presenting information on an event through a Python-based algorithm.'
st.write(alexia_bio)

izaac_bio = 'My name is Izaac, I am going to be a highschool senior this fall semester and I have taken mutiple computer programing cources before. I have taken AP Computer Science in highschool, a HTMl programming cource at the University of Alaska Fairbanks, and I am going to be taking AP Computer Science A at highschool this year.'
st.write(izaac_bio)

navy_bio = "My name is Navy, I'm a rising senior, and I have taken a few computer science courses including AP Comp. Sci. Principles. I know some Java, Javascript, and C, as well as Python which we used for this project."
st.write(navy_bio)


ds_context = ""




df = pd.read_csv('https://raw.githubusercontent.com/ayang903/algorithmic-armadillos/main/anime.csv')

st.dataframe(df)
columns_drop = ['broadcast_day', 'broadcast_time', 'background', 'trailer_url', 'title_english']
df.drop(columns_drop, axis=1, inplace=True)
df.dropna(subset = ['score', 'source'], inplace=True)

#Anish
grouped_df = df.groupby('source')['score'].mean()

grouped_df = grouped_df.sort_values(ascending=False)

anish_var = px.bar(x = grouped_df.index,
                   y = grouped_df.values,
                   color = grouped_df.values, color_continuous_scale=px.colors.sequential.Burgyl)

# anish_var.update_layout (
#     title ='Average Score by Source Content',
#     xaxis_title = "Source Content Type",
#     yaxis_title = "Average Score"

# )
# anish_var.update_layout(yaxes_range = [0,10])
# anish_var.update_layout(
#     yaxis = dict(
#         tickmode = 'linear',
#         tick0 = 0,
#         dtick = 0.5
#     )
# )
anish_var.update_layout (
    title ='Average Score by Source Content',
    xaxis_title = "Source Content Type",
    yaxis_title = "Average Score",
    yaxis = dict(
        range = [0,10],
        tickmode = 'linear',
        tick0 = 0,
        dtick = 0.5
    )
)
st.plotly_chart(anish_var)
anish_exp = "This bar chart shows the average ratings of anime content based on where the anime was derived from. Typically anime derived from web novels have the highest rating along with light novels, manga, standard novels, and web manga. Anime derived from music, radio, picture books, and original anime content tend to be lower rated. However, it is important to remember that all content types have a wide variety of ratings, and there are high and low ratings for anime from nearly every source material."
st.write(anish_exp)

#Amelia

grouped_df = df.groupby('type')['score'].mean()
grouped_df = grouped_df.sort_values(ascending=False)

colorscale = 'tropic'

ameliaVar = px.bar(
    x = grouped_df.index, 
    y = grouped_df.values, 
    color = grouped_df.values, 
    color_continuous_scale = colorscale)

ameliaVar.update_layout(
    title='Average Score by Media Type',
    xaxis_title='Media Type',
    yaxis_title='Average Score'
)

ameliaVar.update_yaxes(range=[5.5, 7])

st.plotly_chart(ameliaVar)
amelia_explanation = 'From the data shown, "tv" recieved the highest score out of the media types. TV was found to receive an average score of 6.92. The category with the next highest score with an average score of 6.51 was "movie". "Special" was found to be third in the average score received with a 6.47. In fourth, "ova", which had an average score of 6.35. Coming in fifth was "ona". Its average score was 6.18. Lastly, "music", which received an average score of 5.94. From this data one could assume that "tv" is the best (score wise) type of anime/manga media. Likewise, one could come to the conclusion that "music" is the worst (score wise) type of anime/manga media. This information can be valuable for understanding audience preferences and guiding decision-making in the entertainment industry.'
st.write(amelia_explanation)

#Navy
ep_v_score = px.scatter(df, x = df['episodes'], y = df['score'], color = 'type', title = 'The Number of Episodes V. The Score')
types_pie = px.pie(df, values ='anime_id', names = 'type', title='Types of Different Anime and Manga')
score_v_rating = px.histogram(df, x = 'score', nbins = 10, color = "rating", title = "Scores of Manga/Anime")

navy_exp1 = "Overall, there isn't much to conclude from the relationship between the score and number of parts an anime or manga has. All types tended to have higher scores as their number of episodes, parts, movies, etc increased but there isn't a definitive trend as many manga/anime with fewer episodes had the higher scores."
navy_exp2 = "From this pie chart we can conclude that the dataset has a good balance of anime and manga of the tv, ona, special, ova, movie, and music variety. TV was the most prevalent type with 26.6% and music was the least prevalent type with 12.9% being the total data."
navy_exp3 = "This histogram shows the range of scores of different anime/manga with 10 different bins. It also seperates the different ratings within each of these bins. Most anime and manga have scores from 6 to 7 noninclusive. Some specific ratings such as g have most of their scores between the scores of 5 to 6 noninclusive."
#ep_v_score.update_layout(df, title = 'The Number of Episodes V. The Score', xaxis_title = 'Number of Episodes', yaxis_title = 'Score')

option = st.selectbox('Choose a Graph', ("Episodes V. Score", "Types Chart", "Score V. Rating"))
if option == "Episodes V. Score":
  st.plotly_chart(ep_v_score)
  st.write(navy_exp1)
elif option == "Types Chart":
  st.plotly_chart(types_pie)
  st.write(navy_exp2)
else:
  st.plotly_chart(score_v_rating)
  st.write(navy_exp3)


#Alexia
daf_themes = df['themes'].value_counts()
themedf = df['themes'].value_counts().head(10)

# alexiavar1 = px.bar(themedf, title='Top Ten Themes of Anime',x=themedf.index, y=themedf.values, color=themedf.index, color_continuous_scale=px.colors.sequential.Turbo)
alexiavar1 = px.bar(themedf, title='Top Ten Themes of Anime',x=themedf.index, y=themedf.values, color=themedf.index)
st.plotly_chart(alexiavar1)

#try a select box here!
option = st.selectbox(
    'Choose a theme',
    ('[]', "['Music']", "['School']", "['Mecha']", "['Historical']"))

general_df = df[df['themes'] == option]['status'].value_counts()
if option == '[]':
  alexiavar2 = px.pie(df, values = general_df.values, names=general_df.index, title=option, color_discrete_sequence=px.colors.sequential.Burg)
elif option == "['Music']":
  alexiavar2 = px.pie(df, values = general_df.values, names=general_df.index, title=option, color_discrete_sequence=px.colors.sequential.Agsunset_r)
elif option == "['School']":
  alexiavar2 = px.pie(df, values = general_df.values, names=general_df.index, title=option, color_discrete_sequence=px.colors.sequential.Tealgrn)
elif option == "['Mecha']":
  alexiavar2 = px.pie(df, values = general_df.values, names=general_df.index, title=option, color_discrete_sequence=px.colors.sequential.Purples_r)
else:
  alexiavar2 = px.pie(df, values = general_df.values, names=general_df.index, title=option, color_discrete_sequence=px.colors.sequential.Viridis)


st.plotly_chart(alexiavar2)


# schooldf = df[df['themes'] == "['School']"]['status'].value_counts()
# alexiavar3 = px.pie(df, values = schooldf.values, names=schooldf.index, title='School', color_discrete_sequence=px.colors.sequential.Agsunset_r)
# st.plotly_chart(alexiavar3)

# mechadf = df[df['themes'] == "['Mecha']"]['status'].value_counts()
# alexiavar4 = px.pie(df, values = mechadf.values, names=mechadf.index, title='Mecha', color_discrete_sequence=px.colors.sequential.Tealgrn)
# st.plotly_chart(alexiavar4)

# historicaldf = df[df['themes'] == "['Historical']"]['status'].value_counts()
# alexiavar5 = px.pie(df, values = historicaldf.values, names=historicaldf.index, title='Historical', color_discrete_sequence=px.colors.sequential.Purples_r)
# st.plotly_chart(alexiavar5)

explanation_alexia = 'According to the above bar graph, the top five themes for anime are [], Music, School, Mecha, and Historical. The five pie charts visually show us about what percent of the anime with these themes are currently airing or have finished airing. As a result, it is shown the anime with the Historical and Mecha themes have finished airing, while there are still some anime airing with the [], Music and School themes. Thus, these pie charts show that anime with no specific theme and Music and School themes are more likely to be currently airing than those with Mecha and Historical themes.'
st.write(explanation_alexia)

#Izaac
score_v_scored = px.scatter(df, x = 'scored_by', y = 'score', title = 'Number of Scores vs. Score', labels={"scored_by": "Number of Scores", 'score': 'Average Score'}, color='type', color_continuous_scale = 'viridis')
st.plotly_chart(score_v_scored)
st.write('This graph show a general exponetial curve that depicts that the more scores a show has the higher it is rated. One can assume that this is because the better shows will be more popular, thus giving them more scores. This graph also indicates that TV and Movies are scored a lot more often than other types of media, and are usually scored higher.')

scores = px.histogram(df, x = df['score'], labels={'score': 'Average Score'})
st.plotly_chart(scores)
st.write('This graph shows the most common scores for shows. This graph shows a pretty perfect standard deviation with the average score being about 6.6.')

# 1st. Talk about conclusions from your graphs/hypothesis
# 2nd. What you learned this week
# 3rd. Most interesting part of this week
st.markdown("""---""")
st.header("Conclusion")


amelia_con = "My hypothesis was that tv shows would have the highest rating because they generally contain more content. My graph proved my hypothesis correct. This week, I learned how to use and understand Python. Additionally, I learned how to use data libraries in Python to visualize data. These data libraries add so much depth to these visualizations. Learning about all the ways these principles are used in real-life was the most interesting part of this week."
st.write (amelia_con)

navy_con = "Navy: For my first graph, my hypothesis was that the more parts an anime or manga had, the higher it's score would be. I thought this because if an anime or manga had higher production then it must be heavily enjoyed. My graph showed that there was a bit of a positive correlation between the number of parts and the score but it was very vague so the answer is inconclusive. My second graph was more to see the different types of anime and manga in the dataset and I'd conclude there's a good range of the six types they've included. My third my third graph was to see the range of scores across all of the media in the dataset and most of their scores were between 6 and 7.\nThis week at  camp I learned how to use the different libraries for data science such as numpy and plotly. I'd never really gone into too many python data visualising libraries before and now I can say that I can make a pretty cool plot.\nThe most interesting part of this week would be when we were able to put all of our graphs together."
st.write(navy_con)

alexia_con = 'My graphs proved that the theme of an anime can indeed have an effect on the airing status of said anime. Since my hypothesis stated that the theme or themes of an anime can affect its airing status, then my hypothesis was proven by the bar and pie graphs.\n I learned from AI Camp that python could be used to display graphs and the analyses made on those graphs on a website for all to see and interact with.\n The most interesting part of this week was how many various packages and modules could be imported into and used so cohesively in just one python file.'
st.write(alexia_con)

anish_con = "For my graph comparing average scores of anime based on their source content, my hypothesis was that anime coming from manga would have the highest score since manga is the most common source of content for anime. Although manga sourced anime did have high scores, the highest went to web novels and light novels. The biggest takeaways I have from this week are the vast uses that modules like Pandas have in terms of using and managing data sets, as well as the different modules that allow you to express that data like Plotly, Matplotlib, and Seaborn."
st.write(anish_con)

izaac_con = 'My hypotosis for the first graph I did was that the more reviews a show has, the better it is rated. I hypothosized this because if more people watch a show, then its probably a better show than onw with less views. This hypothosis turned out to be true with a visible curve in the graph representing the increase in score for the number of people that scored it. What I learned from this week is how to clean a dataset and how to turn that data set into visually appealing graphs. What I think most interesting part of this week was, was learning how machine learning works as well as other high level concepts.'
st.write(izaac_con)