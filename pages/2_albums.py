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
"Diamond Dogs (2016 Remaster)":"albums/DiamondDogs.jpeg",
"David Live (2005 Mix, Remastered Version)":"albums/DavidLive.jpeg",
"Young Americans (2016 Remaster)":"albums/YoungAmericans.jpeg",
"Live Nassau Coliseum '76":"albums/LiveNassau.jpeg",
"Station to Station (2016 Remaster)":"albums/StationToStation.jpeg",
'"Heroes" (2017 Remaster)':"albums/Heroes.jpeg",
"Low (2017 Remaster)":"albums/Low.jpeg",
"David Bowie narrates Prokofiev's Peter and the Wolf & The Young Person's Guide to the Orchestra":"albums/PeterWolf.jpeg",
"Lodger (2017 Remaster)":"albums/Lodger.jpeg",
"Scary Monsters (And Super Creeps) [2017 Remaster]":"albums/ScaryMonsters.jpeg",
"Montreal 1983":"albums/Montreal1983.jpeg",
"Let's Dance (2018 Remaster)":"albums/LetsDance.jpeg",
"Ziggy Stardust and the Spiders from Mars (The Motion Picture Soundtrack)":"albums/ZiggyStardustMotion.jpeg",
"Tonight (2018 Remaster)":"albums/Tonight.jpeg",
"Labyrinth (From The Original Soundtrack Of The Jim Henson Film)":"albums/Labyrinth.jpeg",
"Never Let Me Down (2018 Remaster)":"albums/NeverLetMeDown.jpeg",
"Never Let Me Down [(Remaster) [Japanese Version]]":"albums/NeverLetMeDownJAP.jpeg",
"Peter & The Wolf":"albums/Peter&TheWolf.jpeg",
"David Bowie Narrates Peter And The Wolf":"albums/PeterWolf.jpeg",
"Japan 1992":"albums/Japan1992.jpeg",
"Black Tie White Noise":"albums/BlackTie.jpeg",
"Black Tie White Noise (Extras)":"albums/BlackTieEXTRAS.jpeg",
"Buddha of Suburbia":"albums/BuddhaOfSuburbia.jpeg",
"Live in Santa Monica '72":"albums/LiveInSantaMonica.jpeg",
"London Boy":"albums/LondonBoy.jpeg",
"1. Outside (The Nathan Adler Diaries: A Hyper Cycle)":"albums/Outside.jpeg",
"1. Outside (The Nathan Adler Diaries: A Hyper Cycle) [Expanded Edition]":"albums/OutsideEXPANDED.jpeg",
"Earthling":"albums/Earthling.jpeg",
"Earthling (Expanded Edition)":"albums/EarthlingEXPANDED.jpeg",
"The Deram Anthology 1966 - 1968":"albums/TheDeramAnthology.jpeg",
"Hours...":"albums/Hours.jpeg",
"Hours... (Expanded Edition)":"albums/HoursEXPANDED.jpeg",
"Heathen":"albums/Heathen.jpeg",
"Reality":"albums/Reality.jpeg",
"Glass Spider (Live Montreal '87, 2018 Remaster)":"albums/GlassSpider.jpeg",
"VH1 Storytellers (Live)":"albums/VH1Storytellers.jpeg",
"A Reality Tour":"albums/ARealityTour.jpeg",
"The Next Day":"albums/TheNextDay.jpeg",
"Blackstar":"albums/Blackstar.jpeg",
"Live In Berlin (1978)":"albums/LiveInBerlin.jpeg",
"Cracked Actor (Live, Los Angeles '74)":"albums/CrackedActor.jpeg",
"Stage (2017) [Live]":"albums/Stage.jpeg",
"Welcome To The Blackout (Live London '78)":"albums/WelcomeToTheBlackout.jpeg",
"ライヴ・イン・モントリオール1983 (Live)":"albums/",
"Glastonbury 2000 (Live)":"albums/Glastonbury.jpeg",
"Dance":"albums/Dance.jpeg",
"Serious Moonlight (Live '83, 2018 Remaster)":"albums/SeriousMoonlight.jpeg",
"The 'Mercury' Demos (with John 'Hutch' Hutchinson)":"albums/TheMercuryDemos.jpeg",
"Space Oddity (2019 Mix)":"albums/SpaceOddity(2019Mix).jpeg",
"Conversation Piece":"albums/ConversationPiece.jpeg",
"Metrobolist (aka The Man Who Sold The World) [2020 Mix]":"albums/Metrobolist.jpeg",
"Liveandwell.com (2020 Remaster)":"albums/Liveandwell.jpeg",
"Ouvrez Le Chien (Live Dallas 95)":"albums/OuvrezLeChien.jpeg",
"ChangesNowBowie":"albums/ChangesNowBowie.jpeg",
"The Width Of A Circle":"albums/TheWidthOfACircle.jpeg",
"I'm Only Dancing (The Soul Tour 74) [Live]":"albums/ImOnlyDancing.jpeg",
"Look At The Moon! (Live Phoenix Festival 97)":"albums/LookAtTheMoon.jpeg",
"Something In The Air (Live Paris 99)":"albums/SomethingInTheAir.jpeg",
"At The Kit Kat Klub (Live New York 99)":"albums/AtTheKittyKatClub.jpeg",
"Brilliant Adventure (1992 – 2001)":"albums/BrilliantAdventure.jpeg",
"Toy (Toy:Box)":"albums/Toy.jpeg",
"Moonage Daydream – A Brett Morgen Film":"albums/MoonageDaydream.jpeg"
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