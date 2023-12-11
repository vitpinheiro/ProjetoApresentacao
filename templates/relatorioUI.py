import streamlit as st
from views import View
import time

class RelatorioUI:
  def main():
    st.header("Entrar no Sistema")
    RelatorioUI.listar()
  def entrar():
    st.write('Relatórios de apresentação')