import streamlit as st
from views import View
import time
class AbrirContaUI:
    @staticmethod
    def main():
        st.header('Abrir conta')
        AbrirContaUI.abrir()
    def abrir():
        generos = View.genero_listar()
        id_genero = st.selectbox('Generos',generos,index=None,placeholder='Escolha uma gênero')
        nome = st.text_input('Informe o nome')
        fone  = st.text_input('Informe o telefone')
        email = st.text_input('Informe o email')
        senha = st.text_input('Informe a senha',type="password")
        if st.button('cadastrar'):
            View.banda_inserir(id_genero.get_id(),nome,fone,email,senha)
            st.success('Banda inserido com sucesso')
           