from models.apresentacao import Apresentacao,NApresentacao
from models.avaliacao import Avaliacao,NAvaliacao
from models.banda import Banda,NBanda
from models.cidade import Cidade,NCidade
from models.fa import Fa,NFa
from models.seguidor import Seguidor,NSeguidor
from models.genero import Genero,NGenero

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

        
    def avaliacao_inserir(id_fa,id_apresentacao,estrelas,comentario):
        avaliacao =  Avaliacao(0,id_fa,id_apresentacao,estrelas,comentario)
        NAvaliacao.inserir(avaliacao)
    def avaliacao_listar():
        return NAvaliacao.listar()
    def avaliacao_listar_id(id):
        return NAvaliacao.listar_id(id)
    def avaliacao_atualizar(id,id_fa,id_apresentacao,estrelas,comentario):
        avaliacao =  Avaliacao(id,id_fa,id_apresentacao,estrelas,comentario)
        NAvaliacao.atualizar(avaliacao)
    def avaliacao_excluir(id):
        avaliacao= Avaliacao(id,"","","","")
        NAvaliacao.excluir(avaliacao)

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
    def fa_admin():
        for fa in View.fa_listar():
            if fa.get_nome()=="admin":  
                return 
        View.fa_inserir(0, "admin", 0, "0000", "admin", "admin")  
    def usuario_login(email, senha):
        for fa in View.fa_listar():
            if fa.get_email() == email and fa.get_senha() == senha:
                return fa
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
        if id!=0:
            return NCidade.listar_id(id)
        return None
    def cidade_atualizar(id,nome):
        cidade  = Cidade(id,nome)
        NCidade.atualizar(cidade)
    def cidade_excluir(id):
        cidade = Cidade(id,"")
        NCidade.excluir(cidade)

    
    def fa_inserir(id_cidade, nome, idade, fone, email, senha):
        fa = Fa(0, id_cidade, nome, idade, fone, email, senha)
        NFa.inserir(fa)
    def fa_listar():
        return NFa.listar()
    def fa_listar_id(id):
        return NFa.listar_id(id)
    def fa_atualizar(id,id_cidade,nome, idade, fone, email, senha):
        fa = Fa(id, id_cidade, nome, idade, fone, email, senha)
        NFa.atualizar(fa) 
    def fa_excluir(id):
        fa = Fa(id, "", "", "", "","","")
        NFa.excluir(fa)

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

    def seguidor_inserir(id_banda,id_fa,data):
        seguidor = Seguidor(0,id_banda,id_fa,data)
        NSeguidor.inserir(seguidor)
    def seguidor_listar():
        return NSeguidor.listar()
    def seguidor_listar_id(id):
        return NSeguidor.listar_id(id)
    def seguidor_atualizar(id,id_banda,id_fa,data):
        seguidor = Seguidor(id,id_banda,id_fa,data)
        NSeguidor.atualizar(seguidor)
    def seguidor_excluir(id):
        seguidor = Seguidor(id,"","","")
        NSeguidor.excluir(seguidor)




