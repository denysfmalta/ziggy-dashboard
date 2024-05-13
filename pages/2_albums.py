import streamlit as st
import pandas as pd 
from PIL import Image

# Importa o dataset
df_data = pd.read_csv("datasets/bowiedata.csv")

album_image_urls={
"David Bowie": "albums/DavidBowie.jpeg",
"David Bowie (aka Space Oddity) [2015 Remaster]": "albums/SpaceOddity.jpeg",
"Space Oddity (2019 Mix)": "albums/SpaceOddity(2019Mix).jpeg",
"The Man Who Sold the World (2015 Remaster)": "albums/TheManWhoSoldtheWorld(2015Remaster).jpeg",
"Hunky Dory (2015 Remaster)": "albums/HunkyDory(2015Remaster).jpeg",
"The Rise and Fall of Ziggy Stardust and the Spiders from Mars (2012 Remaster)": "albums/TheRiseandFallofZiggyStardustan.jpeg",
"Aladdin Sane (2013 Remaster)": "albums/AladdinSane.jpeg",
"Pinups (2015 Remaster)": "albums/Pinups.jpeg",
"Diamond Dogs (2016 Remaster)":"",
"David Live (2005 Mix, Remastered Version)":"",
"Young Americans (2016 Remaster)":"",
"Live Nassau Coliseum '76":"",
"Station to Station (2016 Remaster)":"",
'"Heroes" (2017 Remaster)':"",
"Low (2017 Remaster)":"",
"David Bowie narrates Prokofiev's Peter and the Wolf & The Young Person's Guide to the Orchestra":"",
"Lodger (2017 Remaster)":"",
"Scary Monsters (And Super Creeps) [2017 Remaster]":"",
"Montreal 1983":"",
"Let's Dance (2018 Remaster)":"",
"Ziggy Stardust and the Spiders from Mars (The Motion Picture Soundtrack)":"",
"Tonight (2018 Remaster)":"",
"Labyrinth (From The Original Soundtrack Of The Jim Henson Film)":"",
"Never Let Me Down (2018 Remaster)":"",
"Never Let Me Down [(Remaster) [Japanese Version]]":"",
"Peter & The Wolf":"",
"David Bowie Narrates Peter And The Wolf":"",
"Japan 1992":"",
"Black Tie White Noise":"",
"Black Tie White Noise (Extras)":"",
"Buddha of Suburbia":"",
"Live in Santa Monica '72":"",
"London Boy":"",
"1. Outside (The Nathan Adler Diaries: A Hyper Cycle)":"",
"1. Outside (The Nathan Adler Diaries: A Hyper Cycle) [Expanded Edition]":"",
"Earthling":"",
"Earthling (Expanded Edition)":"",
"The Deram Anthology 1966 - 1968":"",
"Hours...":"",
"Hours... (Expanded Edition)":"",
"Heathen":"",
"Reality":"",
"Glass Spider (Live Montreal '87, 2018 Remaster)":"",
"VH1 Storytellers (Live)":"",
"A Reality Tour":"",
"The Next Day":"",
"Blackstar":"",
"Live In Berlin (1978)":"",
"Cracked Actor (Live, Los Angeles '74)":"",
"Stage (2017) [Live]":"",
"Welcome To The Blackout (Live London '78)":"",
"ライヴ・イン・モントリオール1983 (Live)":"",
"Glastonbury 2000 (Live)":"",
"Dance":"",
"Serious Moonlight (Live '83, 2018 Remaster)":"",
"The 'Mercury' Demos (with John 'Hutch' Hutchinson)":"",
"Space Oddity (2019 Mix)":"",
"Conversation Piece":"",
"Metrobolist (aka The Man Who Sold The World) [2020 Mix]":"",
"Liveandwell.com (2020 Remaster)":"",
"Ouvrez Le Chien (Live Dallas 95)":"",
"ChangesNowBowie":"",
"The Width Of A Circle":"",
"No Trendy Réchauffé (Live Birmingham 95)":"",
"I'm Only Dancing (The Soul Tour 74) [Live]":"",
"Look At The Moon! (Live Phoenix Festival 97)":"",
"Something In The Air (Live Paris 99)":"",
"At The Kit Kat Klub (Live New York 99)":"",
"Brilliant Adventure (1992 – 2001)":"",
"Toy (Toy:Box)":"",
"Moonage Daydream – A Brett Morgen Film":""
}

# Seleciona os valores da coluna "ano de lançamento do álbum" e reserva na variável "years" 
years = df_data["album_release_year"].unique()

# Cria a selectbox para selecionar o ano
year_selection = st.sidebar.selectbox("Year", years)

# Filtra os álbums por ano de lançamento
album_by_year = df_data[df_data["album_release_year"] == year_selection]


for album_name in album_by_year["album_name"].unique():
    st.write(album_name)
    if album_name in album_image_urls:
        image = Image.open(album_image_urls[album_name])
        st.image(image, caption=album_name, use_column_width=True)
    else:
        st.write("Image not avaiable")