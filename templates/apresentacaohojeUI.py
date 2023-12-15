from datetime import date
import streamlit as st
from views import View
from datetime import datetime
import pandas as pd
class ApresentacaoHojeUI:
    @staticmethod
    def main():
        st.header('Apresentações hoje')
        ApresentacaoHojeUI.listar()
    def listar():
        usuario = View.banda_listar_id(st.session_state["usuario_id"])
        apresentacoes_usuario =[]
        hoje = datetime.today()
        for a in View.apresentacao_listar():
            if a.get_data().date()==hoje.date() and a.get_id_banda()==usuario.get_id():
                apresentacoes_usuario.append(a)
        if len(apresentacoes_usuario)==0:
            st.write('Nenhuma apresentação cadastrada')
        else:
            dic=[]
            for a in apresentacoes_usuario: 
                dic.append(a.to_json())
            df = pd.DataFrame(dic)
            st.dataframe(df,hide_index=True)

        