from views import View
import streamlit as st
import pandas as pd
from datetime import datetime
class ManterApresentacaoUI:
    def main():
        st.header('Cadastro de Apresentações')
        tab1,tab2,tab3,tab4 = st.tabs(['Listar','Inserir','Atualizar','Excluir'])
        with tab1:
           ManterApresentacaoUI.listar()
        with tab2:
           ManterApresentacaoUI.inserir()
        with tab3:
           ManterApresentacaoUI.atualizar()
        with tab4:
           ManterApresentacaoUI.excluir() 
    def inserir():
        cidades = View.cidade_listar()
        bandas =  View.banda_listar()
        id_cidade = st.selectbox('Cidades',cidades,index=None,placeholder='Escolha uma cidade')
        id_banda = st.selectbox('Bandas',bandas,index=None,placeholder='Escolha uma banda')
        data = st.text_input('Informe a data da apresentação')
        if st.button('Inserir'):    
            View.apresentacao_inserir(id_cidade.get_id(),id_banda.get_id(),datetime.strptime(data,"%d/%m/%Y %H:%M"),False)
            st.success('Apresentação inserida com sucesso')
    def listar():
        apresentacoes = View.apresentacao_listar()
        if len(apresentacoes)==0:
            st.write('Nenhuma apresentação cadastrada')
        else:
            dic=[]
            for a in apresentacoes: 
                dic.append(a.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df,hide_index=True)
    def atualizar():

        apresentacoes = View.apresentacao_listar()
        bandas= View.banda_listar()
        cidades= View.cidade_listar()
        op = st.selectbox('Apresentações',apresentacoes,index=None,placeholder='Escolha uma apresentação')
        banda_atual = View.banda_listar_id(op.get_id_banda() if op!=None else None)
        cidade_atual = View.cidade_listar_id(op.get_id_cidade() if op!=None else None)
        

        if banda_atual is not None:
            id_banda = st.selectbox('Bandas',bandas ,index=bandas.index(banda_atual),key='select_banda_index')
        else:
            id_banda = st.selectbox('Bandas',bandas,index=None,placeholder='Escolha uma banda',key='select_banda_None')
        
        if cidade_atual  is not None:
            id_cidade = st.selectbox('Cidades',cidades, cidades.index(cidade_atual),key='select_cidade_index')
        else:
            id_cidade = st.selectbox('Cidades',cidades,index=None,placeholder='Escolha uma cidade',key='select_cidade_index')
            
        id= op.get_id() if op!=None else None
        data = st.text_input('Informe a nova data da apresentação',op.get_data().strftime("%d/%m/%Y %H:%M") if op!=None else None)
        if st.button('Atualizar'):    
            View.apresentacao_atualizar(id,id_banda.get_id(),id_cidade.get_id(),datetime.strptime(data,"%d/%m/%Y %H:%M"),False)
            st.success('Apresentação atualizada com sucesso')
    
    def excluir():
        apresentacoes = View.apresentacao_listar()
        if len(apresentacoes)==0:
            st.write('Nenhuma apresentação cadastrado')
        else:
            op = st.selectbox('Apresentações',apresentacoes,index=None,placeholder='Escolha uma apresentação',key="selection_apresentacao_excluir")
            if st.button('excluir'):
                if op!=None:
                    View.apresentacao_excluir(op.get_id())
                    st.success('Apresentação excluído com sucesso')
                else:
                    st.error('Selecione alguém para excluir')





