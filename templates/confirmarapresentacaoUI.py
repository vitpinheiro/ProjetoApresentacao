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
        apresentacoes_solicitadas = View.apresentacoes_solicitadas(st.session_state["usuario_id"])

        if len(apresentacoes_solicitadas)==0:
            st.write('Nenhuma solicitação feita')
        else:
            df = pd.DataFrame(apresentacoes_solicitadas)

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
                for a in apresentacoes_solicitadas:
                    apresentacao = apresentacoes_solicitadas.index(a)
                    if editor[apresentacao]['confirmado']==True:
                      View.apresentacao_atualizar(a["id"],a["id_banda"],a["id_cidade"],a["data"],True)
                      st.success('Apresentação confirmada com sucesso')
                      time.sleep(1)
                      st.rerun()

                
                 

                    