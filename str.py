import numpy as np
import pandas as pd
import streamlit as st

with st.container():
    st.title("Cristiano Ronaldo's Life")
    st.sidebar.header('Escolha o tópico que você deseja')
    st.caption('Conheça mais sobre o jogador mais completo do futebol!')
    st.write('Já viu ele em ação?[Clique AQUI.](https://www.youtube.com/watch?v=FPk7iIH4v4Y)')

def carregar_dados():
    tabela =  pd.read_csv('cr7-dados.csv')
    return tabela

with st.container():
    st.write('---')
    qntd_anos = st.selectbox('Qual período você deseja ver?', ["2A","4A", "6A", "8A", "10A",])
    num_anos =int(qntd_anos.replace('A', ''))
    dados = carregar_dados()
    dados = dados[-num_anos:]
    if st.button('Exibir Gráfico'):
        st.header('GRÁFICO DE GOLS POR ANO')
        st.area_chart(dados, x='ANO', y='G',)

with st.container():
    if st.sidebar.button('Biografia'):
        st.markdown("<a href='https://www.ebiografia.com/cristiano_ronaldo/' target='_blank'>Clique aqui</a>", unsafe_allow_html=True)

