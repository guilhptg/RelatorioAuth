import streamlit as st
import pandas as pd
import plotly.express as px
from data_loader import carregar_dados


base = carregar_dados()
# st.title('Sinteses - Dashboard')

# Columns
col_left, col_mid, col_rigth = st.columns([1, 1, 1])


# First Row

setor = col_left.selectbox('Setor', list(base["Setor"].unique()))
status = col_mid.selectbox('Status', list(base['Status'].unique()))


base = base[(base['Status'] == status) & (base['Setor'] == setor)]
base_mensal = base.groupby(base['Data Chegada'].dt.to_period("M")).sum(numeric_only=True).reset_index()
base_mensal['Data Chegada'] = base_mensal['Data Chegada'].dt.to_timestamp()
# time stamp


container = st.container(border=True)
with container:

    # Grafico de área
    st.title('Total Projetos por mes (R$)')
    fig_area = px.area(base_mensal, x='Data Chegada', y='Valor Negociado')
    st.plotly_chart(fig_area)


    st.table(base.head(20))