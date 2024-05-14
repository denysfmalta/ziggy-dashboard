import streamlit as st
import webbrowser

st.set_page_config(layout="wide", page_icon="⚡", page_title="Ziggy Dashboard")
st.write("<h1 style='text-align: right; color: #010866;'>ZIGGY ⚡ DASHBOARD </h1><br>", unsafe_allow_html=True)

st.markdown("<br><h5 style='text-align: left; color: #0d2833;'><br>Análise da discografia de David Bowie usando seu conjunto de dados do Spotify.<br>O conjunto contêm dados abarcados de cada álbum e música. <br> <br>É analisado aqui: a quantidade de álbums por década, qual o álbum com maior fator de dançabilidade, qual o tom dos álbums mais enérgicos e mais!<br><br><br><br><br><br><br><h5>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

btn = col2.button("Veja o dataset na íntegra")

if btn:
    webbrowser.open_new_tab("https://www.kaggle.com/datasets/arthurboari/david-bowie-spotify-data")