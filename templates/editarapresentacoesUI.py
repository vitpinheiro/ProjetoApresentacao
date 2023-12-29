import streamlit as st
from views import View
import time
from datetime import datetime,timedelta

class EditarApresentacoesUI:
    @staticmethod
    def main():
        st.header('Editar Apresentação')
        EditarApresentacoesUI.editar()
    def editar():
        usuario=st.session_state["usuario_id"]
        apresentacoes_usuario = View.apresentacoes_pendentes_todas(usuario)

        cidades= View.cidade_listar()
        op = st.selectbox('Apresentações',apresentacoes_usuario,index=None,placeholder='Escolha uma apresentação')
        cidade_atual = View.cidade_listar_id(op.get_id_cidade() if op!=None else None)
        if cidade_atual  is not None:
            id_cidade = st.selectbox('Cidades',cidades, index = cidades.index(cidade_atual),key='select_cidade_index')
        else:
            id_cidade = st.selectbox('Cidades',cidades,index=None,placeholder='Escolha uma cidade',key='select_cidade_index')        
        data = st.text_input('Informe a nova data da apresentação',op.get_data().strftime("%d/%m/%Y %H:%M") if op!=None else None)
        if st.button('confirmar'):
            try:
                View.apresentacao_atualizar(op.get_id(),usuario, id_cidade.get_id(),data, op.get_confirmado())
                st.success('Apresentação atualizada com sucesso')
              

            except ValueError as erro:
                st.error(erro)
               

    
                    