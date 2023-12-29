import streamlit as st
import pandas as pd
import random
from views import View

class RelatorioUI:
    @staticmethod
    def main():
        if st.session_state["usuario_id"]==0:
            st.header("Relatório")
            tab1,tab2,tab3,tab4 = st.tabs(["Apresentações","Cidades","Bandas","Gêneros"])
            with tab1:
                RelatorioUI.listar_meses()
            with tab2:
                RelatorioUI.listar_cidade()
            with tab3:
                RelatorioUI.listar_banda()
            with tab4:
                RelatorioUI.listar_genero()
        else:
            st.header("Relatório de apresentações")
            tab1,tab2 = st.tabs(["Meses","Cidades"])
            with tab1:
                RelatorioUI.listar_meses()
            with tab2:
                RelatorioUI.listar_cidade()
    @staticmethod
    def listar_meses():
        
                   
        
        st.subheader('Todas as apresentações')
        anos = ["Todas",2023,2024,2025]
        op = st.selectbox('Anos',anos,index=0,placeholder='Selecione um ano')
        datas = View.relatorio_meses(st.session_state["usuario_id"],op)
        meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto'
                 ,"Setembro","Outubro","Novembro","Dezembro"]
        data_mes = pd.DataFrame({
            'Mes': pd.Categorical(meses, categories=meses, ordered=True),
            'Qtd de apresentações': datas
        })
        st.bar_chart(data_mes, x='Mes', y='Qtd de apresentações')
    def listar_cidade():

        st.subheader('Apresentações por cidade')
        anos = ['Todas',2023,2024,2025]

        op = st.selectbox('Anos',anos,index=0,placeholder='Selecione um ano',key='selection_cidade')

        cidades_total=View.relatorio_cidades(st.session_state["usuario_id"],op)
        
       

        data_mes = pd.DataFrame({
            'Nome': cidades_total[0],
            'Qtd de apresentações': cidades_total[1]
        })
        st.bar_chart(data_mes, x='Nome', y='Qtd de apresentações')

    def listar_banda():
        st.subheader('Quantidade de apresentações por banda')
        bandas_total=View.relatorio_bandas()

        data_banda = pd.DataFrame({
            'Nome': bandas_total[0],
            'Qtd de apresentações': bandas_total[1]
    })
                
        st.bar_chart(data_banda, x='Nome', y='Qtd de apresentações')

    def listar_genero():
        st.subheader('Quantidade de gêneros')
        genero_total=View.relatorio_generos()
       

        data_genero = pd.DataFrame({
            'Nome': genero_total[0],
            'Qtd de bandas': genero_total[1]
        })
        st.bar_chart(data_genero, x='Nome', y='Qtd de bandas')
        
        