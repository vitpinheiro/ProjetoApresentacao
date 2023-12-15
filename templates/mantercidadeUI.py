from views import View
import streamlit as st
import pandas as pd
class ManterCidadeUI:
    def main():
        st.header('Cadastro de Cidades')
        tab1,tab2,tab3,tab4 = st.tabs(['Listar','Inserir','Atualizar','Excluir'])
        with tab1:
            ManterCidadeUI.listar()
        with tab2:
            ManterCidadeUI.inserir()
        with tab3:
            ManterCidadeUI.atualizar()
        with tab4:
            ManterCidadeUI.excluir() 
    def inserir():
        nome = st.text_input('Informe o nome')
        if st.button('Inserir'):    
            View.cidade_inserir(nome)
            st.success('Cidade inserida com sucesso')
    def listar():
        cidades = View.cidade_listar()
        if len(cidades)==0:
            st.write('Nenhuma cidade cadastrado')
        else:
            dic=[]
            for c in cidades: dic.append(c.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df,hide_index=True)
    def atualizar():

        cidades = View.cidade_listar()
        op = st.selectbox('Cidades',cidades,index=None,placeholder='Escolha uma cidade')            
        id= op.get_id() if op!=None else None
        nome = st.text_input('Informe o novo nome',op.get_nome() if op!=None else None)
        if st.button('Atualizar'):    
            View.cidade_atualizar(id,nome)
            st.success('Cidade atualizada com sucesso')
    
    def excluir():
        cidades = View.cidade_listar()
        if len(cidades)==0:
            st.write('Nenhum cidade cadastrado')
        else:
            op = st.selectbox('Cidades',cidades,index=None,placeholder='Escolha uma cidade',key='selection_cidade_excluir')
            if st.button('excluir'):
                if op!=None:
                    View.cidade_excluir(op.get_id())
                    st.success('Cidade excluído com sucesso')
                else:
                    st.error('Selecione alguma cidade para excluir')






