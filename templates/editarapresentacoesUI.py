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
        usuario = View.banda_listar_id(st.session_state["usuario_id"])
        apresentacoes_usuario=[]
        for x in View.apresentacao_listar():
            if usuario.get_id()==x.get_id_banda():
                apresentacoes_usuario.append(x)
    
        hoje = datetime.today()
        semana = datetime.today() + timedelta(days=7)
        lista_disponivel = []
        for apresentacao in View.apresentacao_listar():
            if hoje<apresentacao.get_data()<semana and apresentacao.get_confirmado() == False:
                if  apresentacao.get_id_banda() == 0 and apresentacao.get_id_cidade() == 0:
                    lista_disponivel.append(apresentacao.get_data())

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
                View.apresentacao_atualizar(op.get_id(),usuario.get_id(), id_cidade.get_id(),datetime.strptime(data,"%d/%m/%Y %H:%M"), False)
                st.success('Perfil atualizado com sucesso')
                time.sleep(1)
            except ValueError as erro:
                st.error(erro)
                time.sleep(1)
    
                    