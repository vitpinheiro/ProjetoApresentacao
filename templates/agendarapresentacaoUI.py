from views import View
import streamlit as st
import pandas as pd
from datetime import datetime,timedelta
import time
class ApresentacaoHorarioUI:
    @staticmethod
    def main():
        st.header('Agendar uma apresentação')
        tab1, tab2= st.tabs(["Disponíveis", "Solicitadas"])
        with tab1:
            ApresentacaoHorarioUI.agendar()
        with tab2:
            ApresentacaoHorarioUI.solicitadas()


    def agendar():
        cidades = View.cidade_listar()
        id_cidade = st.selectbox('Cidades',cidades,index=None,placeholder='Escolha uma cidade')
        data = st.text_input('Informe a data da apresentação')
        if st.button('Inserir'):    
            try:
                id_cidade= None if id_cidade is None else id_cidade.get_id()
                View.apresentacao_inserir(st.session_state["usuario_id"],id_cidade,data,False)
                st.success('Apresentação solicitada com sucesso')
            except ValueError as erro:
                st.error(erro)   
    def solicitadas():
        apresentacoes_solicitadas = View.apresentacoes_solicitadas(st.session_state["usuario_id"])
        if len(apresentacoes_solicitadas)==0:
            st.write('Nenhuma apresentação solicitada no momento')
        else:
            df= pd.DataFrame(apresentacoes_solicitadas)
            st.dataframe(df,hide_index=True)