# -*- coding: utf-8 -*-
"""
Created on Sat Oct 21 12:28:14 2023

@author: moura

"""

import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('covid-variants.csv');

paises = list(df['location'].unique());
variantes = list(df['variant'].unique());

df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

pais = st.sidebar.selectbox('Escolha o país', ['Todos'] + paises);
variante = st.sidebar.selectbox('Escolha a variante', ['Todas'] + variantes);

if(pais != 'Todos'):
    st.header('Mostrando resultados de ' + pais);
    df = df[df['location']== pais]
else:
    st.header('Mostrando resultados para todos os países ');
    
if(variante != 'Todas'):
    st.subheader('Mostrando resultados de ' + variante);
    df = df[df['location']== variante]
else:
    st.subheader('Mostrando resultados para todas as variantes ');

dfShow = df.groupby(by = ['date']).sum()


fig = px.line(dfShow, x=dfShow.index, y='num_sequences')
fig.update_layout(title='Casos diários COVID-19')
st.plotly_chart(fig, use_container_width=True)

