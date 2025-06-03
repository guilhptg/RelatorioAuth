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
    st.write('### Total Projetos por mes (R$)')
    fig_area = px.area(
        base_mensal, 
        x='Data Chegada', 
        y='Valor Negociado', 
        )

    fig_area.update_traces(
        line=dict(color='purple'),  # Cor da linha
        fillcolor='rgba(128, 0, 128, 0.3)'  # Roxo com transparência
    )
    # Grafico pronto
    st.plotly_chart(fig_area)

    col_left, col_mid, col_rigth = st.columns([3, 1])
    st.write('### Comparação Valor Orçado (R$)')

    base_mensal['Ano'] = base_mensal['Data Chegada'].dt.year
    lista_anos = list(base_mensal['Ano'].unique())
    
    ano_selecionado = col_rigth.selectbox('Ano', lista_anos)

    base_mensal = base_mensal[base_mensal['Ano'] == ano_selecionado]
    total_pago = base_mensal['Valor Negociado'].sum()
    total_desconto = base_mensal['Desconto Concedido'].sum()

    # Métricas
    col_left, col_rigth = st.columns([1, 1])
    col_left.metric('Total Pago', f'{total_pago:,.2f}')
    col_rigth.metric('Total Desconto', f'{total_desconto:,.2f}')

    # Grafico de Barras 
    import plotly.graph_objects as go

    grafico_barra = go.Figure(data=[   
        go.Bar(name='Valor Orçado', x=base_mensal['Data Chegada'], y=base_mensal['Valor Orçado'], text=base_mensal['Valor Orçado']),
        go.Bar(name='Valor Pago', x=base_mensal['Data Chegada'], y=base_mensal['Valor Negociado'], text=base_mensal['Valor Negociado']),
    ]
    )
    
    grafico_barra.update_layout(barmode="group")


    st.plotly_chart(grafico_barra)
    # st.table(base.head(10))