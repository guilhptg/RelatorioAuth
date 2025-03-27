import streamlit as st
from data_loader import carregar_dados


base = carregar_dados()

# st.title('Sinteses - Indicadores')

# Criar indicadores - PD

base_emandamento = base[base["Status"] == "Em andamento"]
base_fechados = base[base["Status"].isin(["Em andamento", "Finalizado"])]


def criar_card(icon, num_card, text, column_card):
    container = column_card.container(border=True)
    col_left, col_rigth = container.columns([1, 2.5])
    col_left.image(f'images/{icon}')
    col_rigth.write(num_card)
    col_rigth.write(text)


col_left, col_mid, col_rigth = st.columns([1, 1, 1])


criar_card(icon='oportunidades.png', num_card=f"{base['Código Projeto'].count():,}", text='Oportunidades', column_card=col_left)
criar_card(icon='projetos_fechados.png', num_card=f'{base_fechados["Status"].count():,}', text='Projetos Fechados', column_card=col_mid)
criar_card(icon='em_andamento.png', num_card=f'{base_emandamento["Status"].count():,}', text='Em andamento', column_card=col_rigth)

criar_card(icon='total_orcado.png', num_card=f'R$ {base_fechados["Valor Orçado"].sum():,.2f}', text='Total Orçado', column_card=col_left)
criar_card(icon='total_pago.png', num_card=f'R$ {base_fechados["Valor Negociado"].sum():,.2f}', text='Total Pago', column_card=col_mid)
criar_card(icon='desconto.png', num_card=f'{base_fechados["Desconto Concedido"].sum():,.2f}', text='Total Desconto', column_card=col_rigth)


# Grafico de Indicadores
import plotly.express as px

base_status = base.groupby('Status', as_index=False).count()
base_status = base_status.rename(columns={'Código Projeto': 'Quantidade'})
base_status = base_status.sort_values(by='Quantidade', ascending=False)

grafico = px.funnel(base_status, x=base_status['Quantidade'], y=base_status["Status"], color_discrete_sequence=['green'])

st.plotly_chart(grafico)

# st.table(base.head(20))