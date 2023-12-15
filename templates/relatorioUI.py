import streamlit as st
import pandas as pd
import random
from views import View

class RelatorioUI:
    @staticmethod
    def main():
        st.header("Relatório de apresentações em cidades")
        RelatorioUI.listar()

    @staticmethod
    def listar():
        usuario = View.banda_listar_id(st.session_state["usuario_id"])
        apresentacoes_usuario =[]
        for a in View.apresentacao_listar():
            if a.get_id_banda()==usuario.get_id():
                apresentacoes_usuario.append(a)
        cidade = []
        data =[]
        for a in apresentacoes_usuario:
            c=View.cidade_listar_id(a.get_id_cidade())
            cidade.append(c.get_nome())
            data.append(a.get_data())


        total_cidades = []
        total_anos = []
        
        anos = [2023,2024,2025]
        pedro=[]
    
        for a in anos:
            meses=[]
            for x in data:
                if x.year == a:
                    meses.append(x.month)
            pedro.append({"Ano": a, 'Meses': {'Janeiro': meses.count(1), 'Fevereiro': meses.count(2),
                                              'Março': meses.count(3), 'Abril': meses.count(4),
                                              'Maio': meses.count(5), 'Junho': meses.count(6),
                                              'Julho': meses.count(7), 'Agosto': meses.count(8),
                                              'Setembro': meses.count(9), 'Outubro': meses.count(10),
                                              'Novembro': meses.count(11), 'Dezembro': meses.count(12)}})
                   


        st.subheader('Todas as apresentações')
        op = st.selectbox('Anos',anos,index=0,placeholder='Selecione um ano')
        qtd=[]
        p=pedro[anos.index(op)]
        for m in p['Meses'].values():
            qtd.append(m)
        meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto'
                 ,"Setembro","Outubro","Novembro","Dezembro"]
        data_mes = pd.DataFrame({
            'Meses': pd.Categorical(meses, categories=meses, ordered=True),
            'Qtd de apresentações': qtd
        })
        st.bar_chart(data_mes, x='Meses', y='Qtd de apresentações') 
        for a in anos:
            cidades=[]
            for x in apresentacoes_usuario:
                if x.get_data().year== a:
                    c=View.cidade_listar_id(x.get_id_cidade())
                    cidades.append(c.get_nome())
            y=[]
            for c in View.cidade_listar():
                if c.get_nome() in cidades:
                    y.append({'Nome':c.get_nome(),'qtd':cidades.count(c.get_nome())})
            total_cidades.append({'Ano':a,'qtds':y})
        
        st.subheader('Apresentações por cidade')
        op = st.selectbox('Anos',anos,index=0,placeholder='Selecione um ano',key='1')
        qtd=[]
        c1=total_cidades[anos.index(op)]
        c2 = c1['qtds']
        nomes2=[]
        qtd2=[]
        for m in c2:
            nomes2.append(m['Nome'])
            qtd2.append(m['qtd'])
        data_mes = pd.DataFrame({
            'Nomes': nomes2,
            'Qtd de apresentações': qtd2
        })
        st.bar_chart(data_mes, x='Nomes', y='Qtd de apresentações') 




       