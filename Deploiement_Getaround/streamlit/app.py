import streamlit as st
import pandas as pd
import plotly.express as px 
import numpy as np
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
import plotly.offline as py
import plotly.tools as tls
from plotly.subplots import make_subplots
import io
pd.options.mode.chained_assignment = None

### Config
st.set_page_config(
    page_title="Getaround",
    layout="wide"
)

### Import dataset
@st.cache(allow_output_mutation=True)
def load_data():
  df = pd.read_excel("get_around_delay_analysis.xlsx")
  return df

df = load_data()


### App
# set title
st.title("GETAROUND")
st.markdown("<p class = 'big-font'> Bienvenue dans l'application GETAROUND : , \
    lVous pouvez louer des voitures à des particuliers pour quelques heures ou quelques jours. </p>", unsafe_allow_html = True)

st.subheader("Jetez un oeil au données :point_down: ")

st.subheader('Données')
st.write(df) 

### Some cleaning
df["delay"]=df["delay_at_checkout_in_minutes"].apply(lambda x : "After time/Late" if x>0 else "In advance/On time")

with st.expander("⏯️ Video de présentation Getaround!"):
    st.video("https://www.youtube.com/watch?v=3LyzwpGSfzE")

    
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Nombre de vehicule", value=df['car_id'].nunique())

with col2:
    st.metric(label="Nombre de location", value=df['rental_id'].nunique())


st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")
st.markdown("")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Proportion de type")
    fig = px.pie(df, names="checkin_type", color_discrete_sequence=["blue", "green", "red"])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Taux d'annulation")
    fig = px.pie(df, names="state", color_discrete_sequence=["orange", "purple"])
    st.plotly_chart(fig, use_container_width=True)

with col3:
    st.subheader("Retards")
    fig = px.pie(df, names="delay", color_discrete_sequence=["yellow", "pink"])
    st.plotly_chart(fig, use_container_width=True)


show_graphs = st.checkbox("Afficher les graphiques")

if show_graphs:
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Restitution des véhicules à temps")
        fig = px.histogram(df, x="delay", color="checkin_type", barmode="group",
                           width=800, height=600, histnorm="percent", text_auto=True)
        fig.update_traces(textposition="outside", textfont_size=15)
        fig.update_layout(margin=dict(l=50, r=50, b=50, t=50, pad=4),
                          yaxis={"visible": False},
                          xaxis={"visible": True},
                          colorway=["purple", "green", "blue"])  # Change the color sequence
        fig.update_xaxes(tickfont_size=15)
        st.plotly_chart(fig)

    st.subheader("Taux d'annulation")
    fig = px.histogram(df, x="state", color="checkin_type", barmode="group",
                       width=800, height=600, histnorm="percent", text_auto=True)
    fig.update_traces(textposition="outside", textfont_size=15)
    fig.update_layout(margin=dict(l=50, r=50, b=50, t=50, pad=4),
                      yaxis={"visible": False},
                      xaxis={"visible": True},
                      colorway=["blue", "red", "yellow"])  # Change the color sequence
    fig.update_xaxes(tickfont_size=15)
    st.plotly_chart(fig)
