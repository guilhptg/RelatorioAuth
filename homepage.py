import streamlit as st

# Containers
# Columns
# st.columns([1,2,1])

col1, col2 = st.columns([3, 4]) # divisão proporcional

with col1:
    st.title('Sinteses Analytcs')
    st.write(f'#### Bem vindo \nEsta é uma análise dos contratos de projetos referentes ao período de 2016 a 2019, realizada pela Sinteses Analytics')


    botao_dashboards = col1.button('Dashboard - Projetos')
    botao_indicadores = col1.button('Principais Indicadores')

    if botao_dashboards:
        st.switch_page('dashboard.py')
    elif botao_indicadores:
        st.switch_page('indicadores.py')      

with col2:
    container = st.container(border=True)
    container = st.image(r'images/S para fundo Escuro.png')