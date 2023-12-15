from views import View
import streamlit as st
import pandas as pd
from datetime import datetime,timedelta
import time
class ApresentacaoHorarioUI:
    @staticmethod
    def main():
        st.header('apresentacaor uma apresentação')
        tab1, tab2= st.tabs(["Disponíveis", "Solicitadas"])
        with tab1:
            ApresentacaoHorarioUI.disponiveis()
        with tab2:
            ApresentacaoHorarioUI.solicitadas()


    def disponiveis():
        apresentacoes = View.apresentacao_listar()
        hoje = datetime.today()
        semana = datetime.today() + timedelta(days=7)
        lista_disponivel = []
        for apresentacao in apresentacoes:
            if hoje<apresentacao.get_data()<semana and apresentacao.get_confirmado() == False:
                if  apresentacao.get_id_banda() == 0 and apresentacao.get_id_cidade() == 0:
                    lista_disponivel.append(apresentacao)


        if len(lista_disponivel)==0:
            st.write('Nenhuma apresentação disponível no momento')
        else:
            df = pd.DataFrame([x.to_json() for x in lista_disponivel])
            st.dataframe(df,hide_index=True)
            


            op1 = st.selectbox('Selecione um horario',lista_disponivel,index=None,placeholder="Escolha um horário entre os listados acima")
        
            cidades = View.cidade_listar()
            id_cidade = st.selectbox('Cidades',cidades,index=None,placeholder='Escolha uma cidade')
            if st.button('agendar'):
                if op1 and id_cidade:
                    for apresentacao in apresentacoes:
                        if apresentacao.get_data()==op1.get_data() and apresentacao.get_id()==op1.get_id() :
                            View.apresentacao_atualizar(apresentacao.get_id(), st.session_state["usuario_id"], id_cidade.get_id(), apresentacao.get_data(), False)
                            st.success('Apresentação solicitado com sucesso')
                            break
                else:
                    st.error('Selecione uma cidade e/ou um horário')
                    

    def solicitadas():
        apresentacoes = View.apresentacao_listar()

        lista_solicitacao = []
        hoje = datetime.today()
        semana = datetime.today() + timedelta(days=7)
        for apresentacao in apresentacoes:
            if hoje<apresentacao.get_data()<semana and apresentacao.get_confirmado() == False:
                    if apresentacao.get_id_banda() == st.session_state['usuario_id'] and  apresentacao.get_id_cidade() != 0:
                        lista_solicitacao.append({"Datas":apresentacao.get_data().strftime('%d/%m/%Y %H:%M'),'Cidade': View.cidade_listar_id(apresentacao.get_id_cidade()).get_nome()})

        if len(lista_solicitacao)==0:
            st.write('Nenhuma apresentação solicitada no momento')
        else:
            df= pd.DataFrame(lista_solicitacao)
            st.dataframe(df,hide_index=True)