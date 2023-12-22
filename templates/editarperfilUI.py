import streamlit as st
from views import View
import time
class EditarPerfilUI:
    @staticmethod
    def main():
        st.header('Editar Perfil')
        EditarPerfilUI.editar()
    def editar():
        if st.session_state["usuario_id"]!=0:
            usuario = View.banda_listar_id(st.session_state["usuario_id"])
            genero_atual = View.genero_listar_id(usuario.get_id_genero())
            generos = View.genero_listar()
            id_genero = st.selectbox('Generos',generos,index= generos.index(genero_atual),placeholder='Escolha uma gênero',)
            nome = st.text_input('Informe o nome',usuario.get_nome())
            fone  = st.text_input('Informe o telefone',usuario.get_fone())
            email = st.text_input('Informe o email',usuario.get_email())
            senha = st.text_input('Informe a senha',type="password")
            if st.button('confirmar'):
                try:
                    View.banda_atualizar(st.session_state["usuario_id"],id_genero.get_id(),nome,fone,email,senha)
                    st.success('Perfil atualizado com sucesso')
                    time.sleep(1)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                    time.sleep(1)
                    st.rerun()
        else:
            email = st.text_input('Informe o novo email')
            fone = st.text_input('Informe o novo fone')
            senha = st.text_input('Informe a nova senha')
            if st.button('confirmar'):
                try:
                    View.banda_atualizar(0,0,"admin",fone,email,senha)
                    st.success('Perfil atualizado com sucesso')
                    time.sleep(1)
                    st.rerun()
                except ValueError as erro:
                    st.error(erro)
                    time.sleep(1)
                    st.rerun()

                    