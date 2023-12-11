import streamlit as st
from views import View
class ApresentacaoHojeUI:
    @staticmethod
    def main():
        st.header('Cancelar apresentações')
        ApresentacaoHojeUI.listar()
    def listar():
        st.write('Apresentações hoje')

        
