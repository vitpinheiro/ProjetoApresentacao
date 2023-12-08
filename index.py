from templates.manterapresentacoesUI import ManterApresentacaoUI
from templates.manterbandaUI import ManterBandaUI
from templates.mantercidadeUI import ManterCidadeUI
from templates.loginUI import LoginUI
from views import View
import streamlit as st

class IndexUI:

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
    if op == "Login": LoginUI.main()

  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Apresentacoes", "Manter Bandas", 
    "Manter Cidades"])
    if op == "Manter Apresentacoes": ManterApresentacaoUI.main()
    if op == "Manter Bandas": ManterBandaUI.main()
    if op == "Manter Cidades": ManterCidadeUI.main()

  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["usuario_id"]
      del st.session_state["usuario_nome"]
      st.rerun()

  def sidebar():
    if "usuario_id" not in st.session_state:
      IndexUI.menu_visitante()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
      if st.session_state["usuario_nome"] == "admin":
        IndexUI.menu_admin()
      IndexUI.btn_logout()  

  def main():
    View.fa_admin()
    IndexUI.sidebar()

IndexUI.main()


