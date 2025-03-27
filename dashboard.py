import streamlit as st
from data_loader import carregar_dados

base = carregar_dados()
# st.title('Sinteses - Dashboard')

# Columns
col_left, col_mid, col_rigth = st.columns([1, 1, 1])


# First Row

col_left._selectbox()


st.table(base.head(20))