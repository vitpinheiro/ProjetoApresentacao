import streamlit as st
from views import View
import time
class LoginUI:
  def main():
    st.header("Entrar no Sistema")
    LoginUI.entrar()
  def entrar():

    
    email = st.text_input("Informe o e-mail")
    senha = st.text_input("Informe a senha",type="password")
    if st.button("Login"):
      usuario = View.usuario_login(email, senha) 
      if usuario is not None:
        st.success("Login realizado com sucesso")
        st.success("Bem-vindo(a), " + usuario.get_nome())
        st.session_state["usuario_id"] = usuario.get_id()
        st.session_state["usuario_nome"] = usuario.get_nome()
        
      else:
        st.error("Usuário ou senha inválido(s)")
      time.sleep(2)
      st.rerun()      