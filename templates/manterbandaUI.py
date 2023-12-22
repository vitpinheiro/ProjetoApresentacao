from views import View
import streamlit as st
import pandas as pd
import logging

class ManterBandaUI:
    def main():
        st.header('Cadastro de Bandas')
        tab1,tab2,tab3,tab4 = st.tabs(['Listar','Inserir','Atualizar','Excluir'])
        with tab1:
           ManterBandaUI.listar()
        with tab2:
           ManterBandaUI.inserir()
        with tab3:
           ManterBandaUI.atualizar()
        with tab4:
           ManterBandaUI.excluir() 
    def inserir():
        generos = View.genero_listar()
        id_genero = st.selectbox('Generos',generos,index=None,placeholder='Escolha uma gênero')
        nome = st.text_input('Informe o nome')
        fone  = st.text_input('Informe o telefone')
        email = st.text_input('Informe o email')
        senha = st.text_input('Informe a senha',type="password")
        if st.button('Inserir'):    
            try:
<<<<<<< HEAD
                id_genero = None if id_genero is None else id_genero.get_id()
                View.banda_inserir(id_genero,nome,fone,email,senha)
                st.success('Banda inserido com sucesso')
            except ValueError as erro: 
                st.error(erro)
=======
                View.banda_inserir(id_genero.get_id(),nome,fone,email,senha)
                st.success('Banda inserido com sucesso')
            except: st.error("erro ao cadastrar")
>>>>>>> aa144165d42653ebc70ad8f9335cd6be3f3c367a

    def listar():
        bandas = View.banda_listar()
        if len(bandas)==0:
            st.write('Nenhum banda cadastrada')
        else:
            dic=[]
            for b in bandas: dic.append(b.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df,hide_index=True)
    def atualizar():

        bandas=View.banda_listar()
        generos = View.genero_listar()
        op = st.selectbox('Bandas para atualizar',bandas,index=None,placeholder='Escolha uma banda para atualizar')
        genero_atual = View.genero_listar_id(op.get_id_genero() if op!=None else None)
        
        
        if genero_atual is not None:
            id_genero = st.selectbox('Gêneros', generos, index=generos.index(genero_atual))
        else:
            id_genero = st.selectbox('Gêneros',generos,index=None,placeholder='Escolha um gênero')
            
        id= op.get_id() if op!=None else None
        nome = st.text_input('Informe o novo nome',op.get_nome() if op!=None else None)
        fone  = st.text_input('Informe o novo telefone',op.get_fone() if op!=None else None)
        email = st.text_input('Informe o novo email',op.get_email() if op!=None else None)
        senha = st.text_input('Informe a nova senha',type="password")
        if st.button('Atualizar'):
            try:
                id_genero = None if id_genero is None else id_genero.get_id()
                View.banda_atualizar(id,id_genero.get_id(),nome,fone,email,senha)
                st.success('Banda atualizado com sucesso')
            except ValueError as erro:
                st.error(erro)
    
    def excluir():
        bandas= View.banda_listar()
        if len(bandas)==0:
            st.write('Nenhuma banda cadastrado')
        else:
            op = st.selectbox('Bandas',bandas,index=None,placeholder='Escolha uma banda',key='selection_banda_excluir')
            if st.button('excluir'):
                if op!=None:
                    View.banda_excluir(op.get_id())
                    st.success('Banda excluído com sucesso')
                else:
                    st.error('Selecione alguém para excluir')





