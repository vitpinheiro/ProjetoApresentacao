from views import View
import streamlit as st
import pandas as pd
import time
from datetime import datetime

class ConfirmarAgendamentoUI:
    @staticmethod
    def main():
        st.header('Confirmar agendamento')
        ConfirmarAgendamentoUI.confimar()
    def confimar():
        lista_solicitacao = []
        for apresentacao in View.apresentacao_listar():
            hoje= datetime.today()
            if apresentacao.get_data()> hoje  and apresentacao.get_id_banda!=0 and apresentacao.get_id_cidade()!=0 and apresentacao.get_confirmado()==False:
                lista_solicitacao.append(apresentacao.to_json())

        if len(lista_solicitacao)==0:
            st.write('Nenhuma solicitação feita')
        else:
            df = pd.DataFrame(lista_solicitacao)

            st.data_editor(
                df,
                key="my_key",
                column_config={
                    "confirmado": st.column_config.CheckboxColumn(
                        default=False,
                    )
                },
                hide_index=True,)
            editor = st.session_state["my_key"]["edited_rows"]
            if editor:
                for a in lista_solicitacao:
                    apresentacao = lista_solicitacao.index(a)
                    if editor[apresentacao]['confirmado']==True:
                      View.apresentacao_atualizar(a["id"],a["id_banda"],a["id_cidade"],datetime.strptime(a["data"], "%d/%m/%Y %H:%M"),True)
                      st.success('Apresentação confirmada com sucesso')
                      time.sleep(1)
                      st.rerun()

                
                 

                    