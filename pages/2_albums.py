import streamlit as st
import pandas as pd 
from PIL import Image

# Importa o dataset
df_data = pd.read_csv("datasets/bowiedata.csv")

album_image_urls={
"David Bowie": "albums/DavidBowie.jpeg",
"David Bowie (aka Space Oddity) [2015 Remaster]": "albums/SpaceOddity.jpeg"
}



# Seleciona os valores da coluna "ano de lançamento do álbum" e reserva na variável "years" 
years = df_data["album_release_year"].unique()

# Cria a selectbox para selecionar o ano
year_selection = st.sidebar.selectbox("Year", years)


album_by_year = df_data[df_data["album_release_year"] == year_selection]

for album_name in album_by_year["album_name"].unique():
    st.write(album_name)
    if album_name in album_image_urls:
        image = Image.open(album_image_urls[album_name])
        st.image(image, caption=album_name, use_column_width=True)
    else:
        st.write("Image not avaiable")