import streamlit as st
from views import View
class CancelarApresentacaoUI:
    @staticmethod
    def main():
        st.header('Cancelar apresentações')
        CancelarApresentacaoUI.cancelar()
    def cancelar():
        usuario=st.session_state["usuario_id"]
        apresentacoes_usuario = View.apresentacoes_pendentes_todas(usuario)
        op = st.selectbox('Apresentações',apresentacoes_usuario,index=None,placeholder='Escolha uma apresentação')
        if st.button('cancelar'):
            if op!=None:
                View.apresentacao_excluir(op.get_id())
                st.success('Apresentação cancelada com sucesso')
                
            else:
                st.error('Selecione uma apresentação')

