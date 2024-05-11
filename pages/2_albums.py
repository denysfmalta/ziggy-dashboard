import streamlit as st
import pandas as pd 

df_data = pd.read_csv("datasets/bowiedata.csv")

years = df_data["album_release_year"].unique()

year_selector = st.sidebar.selectbox("Year", years)

album_by_year = df_data[df_data["album_release_year"] == year_selector]

st.write(album_by_year["album_name"].unique())
