import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from models import session, Usuario

st.set_page_config(layout='wide')

lista_usuarios = session.query(Usuario).all()

credenciais = {"usernames": 
                {
                    usuario.email: 
                    {'name': usuario.nome, 
                    'password': usuario.senha} for usuario in lista_usuarios
                    }
                }

# Lendo as credenciais do admin do arquivo secrets.toml
admin_username = st.secrets["admin"]["username"]
admin_password = st.secrets["admin"]["password"]



authenticator = stauth.Authenticate(credenciais, 'credenciais_hashco', admin_password, cookie_expiry_days=30)

print(credenciais)
# login
def autenticar_usuario(authenticator):
    nome, authentication_status, username = authenticator.login()

    if authentication_status:
        return {'nome': nome, 'username': username}
    elif authentication_status == False:
        st.error("Combinação usuário e senha inválidas")
    else:
        st.error('Preencha o formulário para fazer login')

def logout():
    authenticator.logout()


dados_usuario = autenticar_usuario(authenticator=authenticator)


if dados_usuario:

    # Inicio
    # Dashboards
    # Indicadores
    email_usuario = dados_usuario['username']
    usuario = session.query(Usuario).filter_by(email=email_usuario).first()


    if usuario.admin:
        pg = st.navigation(
            {
                'Home': [st.Page('homepage.py', title='Sinteses - Analytc',)], # função ou arquivo
                'Dashboard': [st.Page('dashboard.py', title='Dashboard'), st.Page('indicadores.py', title='Indicadores')],
                'Conta': [st.Page(logout, title='Sair'), st.Page('criar_conta.py', title='Criar Conta')]
            }
        )
    else:
        pg = st.navigation(
            {
                'Home': [st.Page('homepage.py', title='Sinteses - Analtyc',)], # função ou arquivo
                'Dashboard': [st.Page('dashboard.py', title='Dashboard'), st.Page('indicadores.py', title='Indicadores')],
                'Conta': [st.Page(logout, title='Sair')]
            }
        )


    pg.run()
