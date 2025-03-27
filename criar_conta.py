import streamlit as st
from models import session, Usuario
import streamlit_authenticator as stauth



st.title('Sinteses - Criar Conta')

form = st.form('form_criar_conta')

nome_usuario = form.text_input('Nome usuário')
email_usuario = form.text_input('E-mail usuário')
senha_usuario = form.text_input('Senha do usuário', type='password')
admin_usuario = form.checkbox('Admin')
botao_submit = form.form_submit_button('Enviar')

if botao_submit:
    lista_usuarios_existentes = session.query(Usuario).filter_by(email=email_usuario).all()
    if len(lista_usuarios_existentes) > 0:
        st.write('Já existe um usuário com esse email cadastrado')

    elif len(email_usuario) < 5 or len(senha_usuario) < 3:
        st.write('Preencha o e-mail corretamente')

    else:
        senha_criptografada = stauth.Hasher([senha_usuario]).generate()[0]
        usuario = Usuario(nome=nome_usuario, email=email_usuario, senha=senha_criptografada, admin=admin_usuario)
        session.add(usuario)
        session.commit()
        print('Commited')
        st.write(f'Usuário {usuario.email}  \nCriado com sucesso')
        st.switch_page('homepage.py')