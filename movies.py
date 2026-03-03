import streamlit as st
import pandas as pd

df = pd.read_csv("movies_cleaned.csv")

st.title("🎬 Movie Explorer App")
genres_list = sorted(list(set([g for sublist in df['genres'].str.split('|') for g in sublist])))

selected_genre = st.selectbox("Select a Genre:", genres_list)

filtered_df = df[df['genres'].str.contains(selected_genre, case=False, na=False)]
st.subheader(f"Movies belonging to the '{selected_genre}' genre")
st.dataframe(filtered_df[['Title', 'Year', 'genres']], use_container_width=True)
