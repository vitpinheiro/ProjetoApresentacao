from templates.manterapresentacaoUI import ManterApresentacaoUI
from templates.manterbandaUI import ManterBandaUI
from templates.mantercidadeUI import ManterCidadeUI
from templates.mantergeneroUI import ManterGeneroUI
from templates.loginUI import LoginUI
from views import View
from templates.abrircontaUI import AbrirContaUI

from templates.agendarapresentacaoUI import ApresentacaoHorarioUI
from templates.confirmarapresentacaoUI import ConfirmarAgendamentoUI
from templates.editarperfilUI import EditarPerfilUI
from templates.editarapresentacoesUI import EditarApresentacoesUI
from templates.cancelarapresentacaoUI import CancelarApresentacaoUI
from templates.visualizarapresentacoesUI import VisualizarApresentacoesUI
from templates.apresentacaohojeUI import ApresentacaoHojeUI
from templates.relatorioUI import RelatorioUI
import streamlit as st

class IndexUI:

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
    if op == "Login":
      LoginUI.main()
    if op == "Abrir Conta" : AbrirContaUI.main()

  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Apresentacoes", "Manter Bandas", 
    "Manter Cidades","Manter Generos","Confirmar apresentacao","Editar perfil","Relatório"])
    if op == "Manter Apresentacoes": ManterApresentacaoUI.main()
    if op == "Manter Bandas": ManterBandaUI.main()
    if op == "Manter Cidades": ManterCidadeUI.main()
    if op == "Manter Generos": ManterGeneroUI.main()

    if op == "Confirmar apresentacao" : ConfirmarAgendamentoUI.main()
    if op == "Editar perfil" : EditarPerfilUI.main()
    if op == "Relatório" : RelatorioUI.main()

  def menu_banda():
    op = st.sidebar.selectbox("Menu", ["Abrir Conta","Editar perfil","Agendar Apresentações",
    "Editar Apresentações","Cancelar Apresentação","Visualizar Apresentações","Apresentações Hoje","Relatório"])
    if op == "Abrir Conta" : AbrirContaUI.main()
    if op == "Editar perfil" : EditarPerfilUI.main()
    if op == "Agendar Apresentações" : ApresentacaoHorarioUI.main()
    if op == "Editar Apresentações" : EditarApresentacoesUI.main()
    if op == "Cancelar Apresentação": CancelarApresentacaoUI.main()
    if op == "Visualizar Apresentações" : VisualizarApresentacoesUI.main()
    if op == "Apresentações Hoje" : ApresentacaoHojeUI.main()
    if op == "Relatório" : RelatorioUI.main()
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
      else: 
        IndexUI.menu_banda()
      IndexUI.btn_logout()

  def main():
    View.admin()
    IndexUI.sidebar()

IndexUI.main()

