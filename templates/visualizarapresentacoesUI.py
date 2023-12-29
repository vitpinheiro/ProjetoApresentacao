import streamlit as st
from pandas.api.types import (
    is_categorical_dtype,
    is_datetime64_any_dtype,
    is_object_dtype,
)
import pandas as pd
from views import View

class VisualizarApresentacoesUI:
    @staticmethod
    def main():
        st.header('Visualizar apresentações')
        tab1, tab2 = st.tabs(["Pendentes", "Realizadas"])
        with tab1:
            VisualizarApresentacoesUI.visualizar_pendentes()
        with tab2:
            VisualizarApresentacoesUI.visualizar_realizados()

    @staticmethod
    def visualizar_realizados():
        apresentacoes_realizados = View.apresentacoes_realizados(st.session_state["usuario_id"])
        
        if len(apresentacoes_realizados) == 0:
            st.write('Nenhuma apresentação cadastrada')
        else:
            dic = []
            for a in apresentacoes_realizados: 
                dic.append(a)
            df = pd.DataFrame(dic)
            st.dataframe(VisualizarApresentacoesUI.filter_dataframe(df, 'realizado'), hide_index=True)

    @staticmethod
    def visualizar_pendentes():
        apresentacoes_pendentes = View.apresentacoes_pendentes(st.session_state["usuario_id"])
        
        if len(apresentacoes_pendentes) == 0:
            st.write('Nenhuma apresentação cadastrada')
        else:
            dic = []
            for a in apresentacoes_pendentes: 
                dic.append(a)
            df = pd.DataFrame(dic)
            st.dataframe(VisualizarApresentacoesUI.filter_dataframe(df, 'pendente'), hide_index=True)

    @staticmethod
    def filter_dataframe(df: pd.DataFrame, identifier: str) -> pd.DataFrame:
        modify = st.checkbox("Adicionar filtros", key=f'filtro_checkbox_{identifier}')

        if not modify:
            return df

        df = df.copy()

        for col in df.columns:
            if is_object_dtype(df[col]):
                try:
                    df[col] = pd.to_datetime(df[col])
                except Exception:
                    pass

            if is_datetime64_any_dtype(df[col]):
                df[col] = df[col].dt.tz_localize(None)

        modification_container = st.container()

        with modification_container:
            to_filter_columns = st.multiselect(f"Filter dataframe on {identifier}", df.columns)
            for column in to_filter_columns:
                left, right = st.columns((1, 20))
                checkbox_key = f'filtro_checkbox_{identifier}_{column}'
                modify = right.checkbox("Add filters", key=checkbox_key)

                if modify:
                    if column.lower() == "data":
                        df[column] = pd.to_datetime(df[column], format='%Y-%m-%d %H:%M', errors='coerce')
                        user_date_input = right.date_input(
                            f"Values for {column}",
                            value=(df[column].min(), df[column].max()),
                        )
                        if len(user_date_input) == 2:
                            user_date_input = tuple(map(pd.to_datetime, user_date_input))
                            start_date, end_date = user_date_input
                            df = df.loc[df[column].between(start_date, end_date)]
                    elif is_categorical_dtype(df[column]) or df[column].nunique() < 10:
                        user_cat_input = right.multiselect(
                            f"Values for {column}",
                            df[column].unique(),
                            default=list(df[column].unique()),
                        )
                        df = df[df[column].isin(user_cat_input)]
                    else:
                        user_text_input = right.text_input(
                            f"Substring or regex in {column}",
                        )
                        if user_text_input:
                            df = df[df[column].astype(str).str.contains(user_text_input)]

        return df
