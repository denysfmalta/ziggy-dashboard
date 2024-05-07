import pandas as pd 
import streamlit as st 
import plotly.express as px

st.title('My App') 
st.header('Data Visualization Section')  
st.subheader('Subsection: Pie Chart Analysis')

data = pd.read_csv("bowiedata.csv")

st.dataframe(data)