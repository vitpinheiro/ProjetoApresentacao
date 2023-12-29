from models.apresentacao import Apresentacao,NApresentacao
from models.banda import Banda,NBanda
from models.cidade import Cidade,NCidade
from models.genero import  Genero,NGenero
from datetime import datetime,timedelta

class View:
    @staticmethod
    def apresentacao_inserir(id_banda,id_cidade,data,confirmado):
        if id_banda == None: raise ValueError('Selecione uma banda')
        elif id_cidade == None: raise ValueError('Selecione uma cidade')
        format = "%d/%m/%Y %H:%M"
        try:
            data = datetime.strptime(data,format)
        except:
            raise ValueError('Data inválida')
        hoje = datetime.today()
        if hoje > data : raise ValueError('Data no passado')
        apresentacao = Apresentacao(0,id_banda,id_cidade,data,confirmado)
        NApresentacao.inserir(apresentacao)
    def apresentacao_listar():
        return NApresentacao.listar()
    def apresentacao_listar_id(id):
        return NApresentacao.listar_id(id)
    def apresentacao_atualizar(id,id_banda,id_cidade,data,confirmado):
        if id==None: raise ValueError('Selecione uma apresentação')
        format = "%d/%m/%Y %H:%M"
        try:
            data = datetime.strptime(data,format)
        except:
            raise ValueError('Data inválida')
        hoje = datetime.today()
        if hoje > data : raise ValueError('Data no passado')
        apresentacao = Apresentacao(id,id_banda,id_cidade,data,confirmado)
        NApresentacao.atualizar(apresentacao)
    def apresentacao_excluir(id):
        apresentacao = Apresentacao(id,"","","","")
        NApresentacao.excluir(apresentacao)

 

    def banda_inserir(id_genero,nome,fone,email,senha):
        if id_genero is None: raise ValueError('Selecione um gênero')
        elif nome == "": raise ValueError('Nome inválido')
        elif fone == "": raise ValueError('Fone inválido')
        elif email == "" : raise ValueError('Email Inválido')
        for x in View.banda_listar():
            if x.get_email() == email: 
                raise ValueError("Email repetido")
        if senha == "": raise ValueError('Senha Inválida')
        banda = Banda(0,id_genero,nome,fone,email,senha)
        NBanda.inserir(banda)



    def banda_listar():
        return NBanda.listar()
    def banda_listar_id(id):
        return NBanda.listar_id(id)

    def banda_atualizar(id,id_genero,nome,fone,email,senha):
        if id_genero == "": raise ValueError('Selecione um gênero')
        elif nome == "": raise ValueError("Nome inválido")
        elif fone == "": raise ValueError("Fone inválido")
        elif email == "" : raise ValueError('Email Inválido')
        for x in View.banda_listar():
            if x.get_email() == email: 
                raise ValueError("Email repetido")
        if senha == "": raise ValueError('Senha Inválida')
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
        if nome=="": raise ValueError('Nome de cidade inválido')
        cidade = Cidade(0,nome)
        NCidade.inserir(cidade)
    def cidade_listar():
        return NCidade.listar()
    def cidade_listar_id(id):
        return NCidade.listar_id(id)
    def cidade_atualizar(id,nome):
        if nome=="": raise ValueError('Nome de cidade inválido')
        cidade  = Cidade(id,nome)
        NCidade.atualizar(cidade)
    def cidade_excluir(id):
        cidade = Cidade(id,"")
        NCidade.excluir(cidade)

    
    
    def genero_inserir(nome):
        if nome=="": raise ValueError('Nome de gênero inválido')
        genero = Genero(0,nome)
        NGenero.inserir(genero)
    def genero_listar():
        return NGenero.listar()
    def genero_listar_id(id):
        return NGenero.listar_id(id)
    def genero_atualizar(id,nome):
        if nome=="": raise ValueError('Nome de gênero inválido')
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
    def apresentacoes_usuario(u):
        usuario = View.banda_listar_id(u)
        if usuario.get_nome()=="admin":
            return View.apresentacao_listar()
        else:
            apresentacoes_usuario =[]
            for a in View.apresentacao_listar():
                if a.get_id_banda()==usuario.get_id():
                    apresentacoes_usuario.append(a)
            return apresentacoes_usuario
   
        
    def relatorio_meses(u,ano):
        apresentacoes=View.apresentacoes_usuario(u)
        
        data_apresentacao=[]
        for a in apresentacoes:
            data_apresentacao.append(a.get_data())

        data_total = []
        anos = ['Todas',2023,2024,2025]
        
    
        for a in anos:
            meses=[]
            for d in data_apresentacao:
                if d.year == a:
                    meses.append(d.month)
                elif a=='Todas':
                    meses.append(d.month)
            data_total.append({"Ano": a, 'Meses': {'Janeiro': meses.count(1), 'Fevereiro': meses.count(2),
                                            'Março': meses.count(3), 'Abril': meses.count(4),
                                            'Maio': meses.count(5), 'Junho': meses.count(6),
                                            'Julho': meses.count(7), 'Agosto': meses.count(8),
                                            'Setembro': meses.count(9), 'Outubro': meses.count(10),
                                            'Novembro': meses.count(11), 'Dezembro': meses.count(12)}})
        data = data_total[anos.index(ano)]
        qtd_data=[]
        for m in data['Meses'].values():
            qtd_data.append(m)

        return qtd_data
    
    def relatorio_cidades(u,ano):
        apresentacoes=View.apresentacoes_usuario(u)


        anos=["Todas",2023,2024,2025]
        cidade_total=[]
        for a in anos:
            cidade=[]
            cidade_ano=[]
            for x in apresentacoes:
                if x.get_data().year== a:
                    c=View.cidade_listar_id(x.get_id_cidade())
                    cidade_ano.append(c.get_nome())
                if a=="Todas":
                    c=View.cidade_listar_id(x.get_id_cidade())
                    cidade_ano.append(c.get_nome())

            for c in View.cidade_listar():
                cidade.append({'Nome':c.get_nome(),'qtd':cidade_ano.count(c.get_nome())})
            cidade_total.append({'Ano':a,'qtds':cidade})
        
        cidades_ano = cidade_total[anos.index(ano)]
        cidades = cidades_ano['qtds']
        nomes_cidade=[]
        qtd_cidade=[]
        for c in cidades:
            nomes_cidade.append(c['Nome'])
            qtd_cidade.append(c['qtd'])

        return [nomes_cidade,qtd_cidade]
    def relatorio_bandas():
        bandas = View.banda_listar()
        apresentacoes = View.apresentacao_listar()
        bandas_total = []
        for b in bandas:
            qtd = 0
            if b.get_id() != 0:
                for a in apresentacoes:
                    if b.get_id() == a.get_id_banda():
                        qtd += 1
                bandas_total.append({"Banda": b.get_nome(), "qtd": qtd})
        nomes_banda = []
        qtd_banda = []
        for b in bandas_total:
            nomes_banda.append(b['Banda'])
            qtd_banda.append(b['qtd'])
        return [nomes_banda, qtd_banda]
    
    def relatorio_generos():
        generos =View.genero_listar()
        bandas=View.banda_listar()
        generos_total = []

        for g in generos:
            qtd=0
            for b in bandas:
                if g.get_id()==b.get_id_genero():
                    qtd+=1
            generos_total.append({"Genero":g.get_nome(),"qtd": qtd})
        nomes_genero=[]
        qtd_genero = []
        for g in generos_total:
            nomes_genero.append(g['Genero'])
            qtd_genero.append(g['qtd'])
        return [nomes_genero,qtd_genero]

    def apresentacoes_solicitadas(u):
        if u==0:
            hoje = datetime.today()
            apresentacoes_solicitadas =[]
            for a in View.apresentacao_listar():
                if  a.get_confirmado() == False and hoje<a.get_data():
                    apresentacoes_solicitadas.append(a.to_json())
            return apresentacoes_solicitadas
        else:
            apresentacoes=View.apresentacoes_usuario(u)
            hoje = datetime.today()
            apresentacoes_solicitadas=[]
            for a in apresentacoes:
                if  a.get_confirmado() == False and hoje<a.get_data():
                    cidade = View.cidade_listar_id(a.get_id_cidade())
                    data = a.get_data().strftime("%d/%m/%Y %H:%M")
                    apresentacoes_solicitadas.append({"cidade":cidade.get_nome(),"data":data})
            return apresentacoes_solicitadas
    
    def apresentacoes_realizados(u):
        apresentacoes_usuario= View.apresentacoes_usuario(u)
        hoje = datetime.today()
        apresentacoes_realizadas=[]
        for a in apresentacoes_usuario:
            if a.get_confirmado()== True and a.get_data()<hoje:
                cidade = View.cidade_listar_id(a.get_id_cidade())
                data = a.get_data().strftime("%d/%m/%Y %H:%M")
                apresentacoes_realizadas.append({"cidade":cidade.get_nome(),"data":data})
        return apresentacoes_realizadas
    
    def apresentacoes_pendentes(u):
        apresentacoes_usuario= View.apresentacoes_usuario(u)
        hoje = datetime.today()
        apresentacoes_pendentes=[]
        for a in apresentacoes_usuario:
            if a.get_confirmado()== True and a.get_data()>hoje:
                cidade = View.cidade_listar_id(a.get_id_cidade())
                data = a.get_data().strftime("%d/%m/%Y %H:%M")
                apresentacoes_pendentes.append({"cidade":cidade.get_nome(),"data":data})
        return apresentacoes_pendentes

    def apresentacoes_pendentes_todas(u):
        apresentacoes_usuario= View.apresentacoes_usuario(u)
        hoje = datetime.today()
        apresentacoes_pendentes=[]
        for a in apresentacoes_usuario:
            if  a.get_data()>hoje:
                apresentacoes_pendentes.append(a)
        return apresentacoes_pendentes





