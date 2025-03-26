import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth


senhas_criptografadas = stauth.Hasher(['123123', '123123', '3125433']).generate()

credenciais = {"usernames": {
    "sinteses@gmail.com": {"name": "Sinteses", "password": senhas_criptografadas[0]},
    "gui@gmail.com": {"name": "Gui", "password": senhas_criptografadas[1] },
    "anna@gmail.com": {"name": "Anna", "password": senhas_criptografadas[2] },
}}

authenticator = stauth.Authenticate(credenciais, 'credenciais_hashco', 'sadasfafshsakldjhaskjdha', cookie_expiry_days=30)

# login
def autenticar_usuario(authenticator):
    nome, authentication_status, username = authenticator.login()
    if authentication_status:
        return {'nome': nome, 'username': username}
    elif authentication_status == False:
        st.error("Combinação usuário e senha inválidas")
    else:
        st.error('Preencha o formulário para fazer login')



def logout(authenticator):
    authenticator.logout()


dados_usuario = autenticar_usuario(authenticator=authenticator)


if dados_usuario:
    @st.cache_data
    def carregar_dados():
        tabela = pd.read_excel("Base.xlsx")
        return tabela


    base = carregar_dados()

    st.title('Sinteses - Análise')
    st.write('Bem vindo, Fulano')
    st.table(base.head(10))

