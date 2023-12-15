import streamlit as st
from views import View
class CancelarApresentacaoUI:
    @staticmethod
    def main():
        st.header('Cancelar apresentações')
        CancelarApresentacaoUI.cancelar()
    def cancelar():
        usuario = View.banda_listar_id(st.session_state["usuario_id"])
        apresentacoes_usuario=[]
        for x in View.apresentacao_listar():
            if usuario.get_id()==x.get_id_banda():
                apresentacoes_usuario.append(x)
        op = st.selectbox('Apresentações',apresentacoes_usuario,index=None,placeholder='Escolha uma apresentação')
        if st.button('cancelar'):
            View.apresentacao_excluir(op.get_id())
            st.success('Apresentação cancelada com sucesso')
