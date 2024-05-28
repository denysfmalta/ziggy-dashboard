import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go


# Importa o dataset
df_data = pd.read_csv("datasets/bowiedata.csv")
albums_per_year = df_data.groupby('album_release_year').album_id.nunique().reset_index()
albums_per_year.columns = ['album_release_year', 'album_count']
analises = {"Álbuns por ano", "Músicas por tom", "Dançabilidade"}
selecao = st.sidebar.selectbox("Selecione", analises)


if selecao == "Álbuns por ano":


    fig = px.line(albums_per_year, x='album_release_year', y='album_count',
             title='Quantidade de álbuns por ano',
             labels={'album_release_year': 'Ano de lançamento', 'album_count': 'Quantidade de álbuns'},
             template='plotly_white')

    st.plotly_chart(fig)

if selecao == "Músicas por tom":
    musicas_por_tom = df_data.groupby('key_name').track_id.nunique().reset_index()
    musicas_por_tom.columns = ['key_name', 'track_count']
    fig = px.pie(musicas_por_tom, names='key_name', values='track_count',
                 title='Distribuição de músicas por tom',
                 labels={'key_name': 'Tom', 'track_count': 'Quantidade de Músicas'},
                 template='plotly_white')
    st.plotly_chart(fig)

if selecao == "Dançabilidade":
    album_avg = df_data.groupby('album_name').mean().reset_index()
    fig = px.bar(album_avg, x='album_name', y='danceability', title='Valor médio do fator de dançabilidade de cada álbum')
    st.plotly_chart(fig)
