from models.apresentacao import Apresentacao,NApresentacao
from models.banda import Banda,NBanda
from models.cidade import Cidade,NCidade
from models.genero import  Genero,NGenero
from datetime import datetime,timedelta

class View:
    @staticmethod
    def apresentacao_inserir(id_banda,id_cidade,data,confirmado):
        apresentacao = Apresentacao(0,id_banda,id_cidade,data,confirmado)
        NApresentacao.inserir(apresentacao)
    def apresentacao_listar():
        return NApresentacao.listar()
    def apresentacao_listar_id(id):
        return NApresentacao.listar_id(id)
    def apresentacao_atualizar(id,id_banda,id_cidade,data,confirmado):
        apresentacao = Apresentacao(id,id_banda,id_cidade,data,confirmado)
        NApresentacao.atualizar(apresentacao)
    def apresentacao_excluir(id):
        apresentacao = Apresentacao(id,"","","","")
        NApresentacao.excluir(apresentacao)

 

    def banda_inserir(id_genero,nome,fone,email,senha):
        banda = Banda(0,id_genero,nome,fone,email,senha)
        NBanda.inserir(banda)
    def banda_listar():
        return NBanda.listar()
    def banda_listar_id(id):
        return NBanda.listar_id(id)
    def banda_atualizar(id,id_genero,nome,fone,email,senha):
        banda = Banda(id,id_genero,nome,fone,email,senha)
        NBanda.atualizar(banda)
    def banda_excluir(id):
        banda = Banda(id,"","","","","")
        NBanda.excluir(banda)
    def admin():
        for b in View.banda_listar():
            if b.get_nome()=="admin":  
                return 
        View.banda_inserir(0, "admin", "0000", "admin", "admin")
  
    def usuario_login(email, senha):
        for b in View.banda_listar():
            if b.get_email() == email and b.get_senha() == senha:
                return b
        return None
    

    def cidade_inserir(nome):
        cidade = Cidade(0,nome)
        NCidade.inserir(cidade)
    def cidade_listar():
        return NCidade.listar()
    def cidade_listar_id(id):
        return NCidade.listar_id(id)
    def cidade_atualizar(id,nome):
        cidade  = Cidade(id,nome)
        NCidade.atualizar(cidade)
    def cidade_excluir(id):
        cidade = Cidade(id,"")
        NCidade.excluir(cidade)

    
    
    def genero_inserir(nome):
        genero = Genero(0,nome)
        NGenero.inserir(genero)
    def genero_listar():
        return NGenero.listar()
    def genero_listar_id(id):
        return NGenero.listar_id(id)
    def genero_atualizar(id,nome):
        genero = Genero(id,nome)
        NGenero.atualizar(genero)
    def genero_excluir(id):
        genero = Genero(id,"")
        NGenero.excluir(genero)
    def abrir_apresentacao_do_dia(data_ini,data_final,intervalo):
        data_hoje =datetime.today()
        if data_ini<=data_hoje or data_final<data_ini or intervalo<=0:
            raise ValueError
        
        intervalo_ =  timedelta(minutes=intervalo)       
        while data_ini <=data_final:
            NApresentacao.inserir(Apresentacao(0,0,0,data_ini,False))
            data_ini= data_ini + intervalo_
