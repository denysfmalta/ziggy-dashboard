import pandas as pd 
import streamlit as st 
import plotly.express as px
import webbrowser

st.set_page_config(layout="wide")

df_data = pd.read_csv('datasets/bowiedata.csv')

st.title("THE ZIGGY DASHBOARD ⚡")

st.markdown("Este dashboard analisa a discografia de David Bowie usando seu conjunto de dados do Spotify. O conjunto "
            "contêm dados abarcados de cada álbum, e não de músicas individuais. É analisado aqui: a quantidade de "
            "álbums por década, qual o álbum com maior fator de dançabilidade, qual o tom dos álbums mais enérgicos e "
            "mais!")

btn = st.button("Veja o dataset na íntegra")

st.session_state["data"] = df_data

if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/arthurboari/david-bowie-spotify-data")
