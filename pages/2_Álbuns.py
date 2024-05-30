import streamlit as st
import pandas as pd
from PIL import Image

# Importa o dataset
df_data = pd.read_csv("datasets/bowiedata.csv")

album_image_urls = {
    "David Bowie": "assets/albums/DavidBowie.jpeg",
    "Space Oddity (2019 Mix)": "assets/albums/SpaceOddity(2019Mix).jpeg",
    "The Man Who Sold the World (2015 Remaster)": "assets/albums/TheManWhoSoldtheWorld(2015Remaster).jpeg",
    "Hunky Dory (2015 Remaster)": "assets/albums/HunkyDory(2015Remaster).jpeg",
    "The Rise and Fall of Ziggy Stardust and the Spiders from Mars (2012 Remaster)": "assets/albums/TheRiseandFallofZiggyStardustan.jpeg",
    "Aladdin Sane (2013 Remaster)": "assets/albums/AladdinSane.jpeg",
    "Pinups (2015 Remaster)": "assets/albums/Pinups.jpeg",
    "Diamond Dogs (2016 Remaster)": "assets/albums/DiamondDogs.jpeg",
    "David Live (2005 Mix, Remastered Version)": "assets/albums/DavidLive.jpeg",
    "Young Americans (2016 Remaster)": "assets/albums/YoungAmericans.jpeg",
    "Live Nassau Coliseum '76": "assets/albums/LiveNassau.jpeg",
    "Station to Station (2016 Remaster)": "assets/albums/StationToStation.jpeg",
    '"Heroes" (2017 Remaster)': "assets/albums/Heroes.jpeg",
    "Low (2017 Remaster)": "assets/albums/Low.jpeg",
    "David Bowie narrates Prokofiev's Peter and the Wolf & The Young Person's Guide to the Orchestra": "assets/albums/PeterWolf.jpeg",
    "Lodger (2017 Remaster)": "assets/albums/Lodger.jpeg",
    "Scary Monsters (And Super Creeps) [2017 Remaster]": "assets/albums/ScaryMonsters.jpeg",
    "Montreal 1983": "assets/albums/Montreal1983.jpeg",
    "Let's Dance (2018 Remaster)": "assets/albums/LetsDance.jpeg",
    "Ziggy Stardust and the Spiders from Mars (The Motion Picture Soundtrack)": "assets/albums/ZiggyStardustMotion.jpeg",
    "Tonight (2018 Remaster)": "assets/albums/Tonight.jpeg",
    "Labyrinth (From The Original Soundtrack Of The Jim Henson Film)": "assets/albums/Labyrinth.jpeg",
    "Never Let Me Down (2018 Remaster)": "assets/albums/NeverLetMeDown.jpeg",
    "Peter & The Wolf": "assets/albums/Peter&TheWolf.jpeg",
    "David Bowie Narrates Peter And The Wolf": "assets/albums/PeterWolf.jpeg",
    "Japan 1992": "assets/albums/Japan1992.jpeg",
    "Black Tie White Noise": "assets/albums/BlackTie.jpeg",
    "Buddha of Suburbia": "assets/albums/BuddhaOfSuburbia.jpeg",
    "Live in Santa Monica '72": "assets/albums/LiveInSantaMonica.jpeg",
    "London Boy": "assets/albums/LondonBoy.jpeg",
    "1. Outside (The Nathan Adler Diaries: A Hyper Cycle)": "assets/albums/Outside.jpeg",
    "Earthling": "assets/albums/Earthling.jpeg",
    "The Deram Anthology 1966 - 1968": "assets/albums/TheDeramAnthology.jpeg",
    "Hours...": "assets/albums/Hours.jpeg",
    "Heathen": "assets/albums/Heathen.jpeg",
    "Reality": "assets/albums/Reality.jpeg",
    "Glass Spider (Live Montreal '87, 2018 Remaster)": "assets/albums/GlassSpider.jpeg",
    "VH1 Storytellers (Live)": "assets/albums/VH1Storytellers.jpeg",
    "A Reality Tour": "assets/albums/ARealityTour.jpeg",
    "The Next Day": "assets/albums/TheNextDay.jpeg",
    "Blackstar": "assets/albums/Blackstar.jpeg",
    "Live In Berlin (1978)": "assets/albums/LiveInBerlin.jpeg",
    "Cracked Actor (Live, Los Angeles '74)": "assets/albums/CrackedActor.jpeg",
    "Stage (2017) [Live]": "assets/albums/Stage.jpeg",
    "Welcome To The Blackout (Live London '78)": "assets/albums/WelcomeToTheBlackout.jpeg",
    "ライヴ・イン・モントリオール1983 (Live)": "assets/albums/KingBiscuit.jpeg",
    "Glastonbury 2000 (Live)": "assets/albums/Glastonbury.jpeg",
    "Dance": "assets/albums/Dance.jpeg",
    "Serious Moonlight (Live '83, 2018 Remaster)": "assets/albums/SeriousMoonlight.jpeg",
    "The 'Mercury' Demos (with John 'Hutch' Hutchinson)": "assets/albums/TheMercuryDemos.jpeg",
    "Conversation Piece": "assets/albums/ConversationPiece.jpeg",
    "Metrobolist (aka The Man Who Sold The World) [2020 Mix]": "assets/albums/Metrobolist.jpeg",
    "Liveandwell.com (2020 Remaster)": "assets/albums/Liveandwell.jpeg",
    "Ouvrez Le Chien (Live Dallas 95)": "assets/albums/OuvrezLeChien.jpeg",
    "ChangesNowBowie": "assets/albums/ChangesNowBowie.jpeg",
    "The Width Of A Circle": "assets/albums/TheWidthOfACircle.jpeg",
    "I'm Only Dancing (The Soul Tour 74) [Live]": "assets/albums/ImOnlyDancing.jpeg",
    "Look At The Moon! (Live Phoenix Festival 97)": "assets/albums/LookAtTheMoon.jpeg",
    "Something In The Air (Live Paris 99)": "assets/albums/SomethingInTheAir.jpeg",
    "At The Kit Kat Klub (Live New York 99)": "assets/albums/AtTheKittyKatClub.jpeg",
    "Brilliant Adventure (1992 – 2001)": "assets/albums/BrilliantAdventure.jpeg",
    "Toy (Toy:Box)": "assets/albums/Toy.jpeg",
    "Moonage Daydream – A Brett Morgen Film": "assets/albums/MoonageDaydream.jpeg"
}

# Seleciona os valores da coluna "ano de lançamento do álbum" e reserva na variável "years"
years = df_data["album_release_year"].unique()

# Cria a selectbox para selecionar o ano
year_selection = st.sidebar.selectbox("Ano", years)

# Filtra os álbums por ano de lançamento
album_by_year = df_data[df_data["album_release_year"] == year_selection]

# Separa o layout da página em quatro colunas
col1, col2, col3, col4 = st.columns(4)

col1_empty = True
col2_empty = True
col3_empty = True
col4_empty = True

for album_name in album_by_year["album_name"].unique():
    if album_name in album_image_urls:
        image = Image.open(album_image_urls[album_name])
        if col1_empty:
            with col1:
                st.image(image, caption=album_name, use_column_width="auto")
            col1_empty = False
        elif col2_empty:
            with col2:
                st.image(image, caption=album_name, use_column_width="auto")
            col2_empty = False
        elif col3_empty:
            with col3:
                st.image(image, caption=album_name, use_column_width="auto")
            col3_empty = False
        elif col4_empty:
            with col4:
                st.image(image, caption=album_name, use_column_width="auto")
            col4_empty = False