import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt  # <--- This is the missing piece!

df = pd.read_csv("movies_cleaned.csv")

st.title("🎬 Movie Explorer App")
genres_list = sorted(list(set([g for sublist in df['genres'].str.split('|') for g in sublist])))

selected_genre = st.selectbox("Select a Genre:", genres_list)

filtered_df = df[df['genres'].str.contains(selected_genre, case=False, na=False)]
st.subheader(f"Movies belonging to the '{selected_genre}' genre")
st.dataframe(filtered_df[['Title', 'Year', 'genres']], use_container_width=True)

st.subheader("Total Movies per Genre")
exploded_genres = df['genres'].str.split('|').explode()
genre_counts = exploded_genres.value_counts()
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(genre_counts.index, genre_counts.values, color='skyblue')
plt.xticks(rotation=90)
plt.ylabel("Number of Movies")
st.pyplot(fig)
