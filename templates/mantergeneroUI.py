from views import View
import streamlit as st
import pandas as pd
class ManterGeneroUI:
    def main():
        st.header('Cadastro de generos')
        tab1,tab2,tab3,tab4 = st.tabs(['Listar','Inserir','Atualizar','Excluir'])
        with tab1:
            ManterGeneroUI.listar()
        with tab2:
            ManterGeneroUI.inserir()
        with tab3:
            ManterGeneroUI.atualizar()
        with tab4:
            ManterGeneroUI.excluir() 
    def inserir():
        nome = st.text_input('Informe o nome')
        if st.button('Inserir'):    
            View.genero_inserir(nome)
            st.success('Gênero inserido com sucesso')
            

    def listar():
        generos = View.genero_listar()
        if len(generos)==0:
            st.write('Nenhum gênero cadastrado')
        else:
            dic=[]
            for g in generos: dic.append(g.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df,hide_index=True)
    def atualizar():

        generos = View.genero_listar()
        op = st.selectbox('Gêneros',generos,index=None,placeholder='Escolha um gênero')            
        id= op.get_id() if op!=None else None
        nome = st.text_input('Informe o novo nome',op.get_nome() if op!=None else None)
        if st.button('Atualizar'):    
            View.genero_atualizar(id,nome)
            st.success('Gênero atualizado com sucesso')
            

    
    def excluir():
        generos = View.genero_listar()
        if len(generos)==0:
            st.write('Nenhum gênero cadastrado')
        else:
            op = st.selectbox('Gêneros',generos,index=None,placeholder='Escolha um gênero',key='selection_genero_excluir')
            if st.button('excluir'):
                if op!=None:
                    View.genero_excluir(op.get_id())
                    st.success('Gênero excluído com sucesso')
                    

                else:
                    st.error('Selecione algum gênero excluir')
                    







