import json
from datetime import datetime
class Apresentacao:
    @staticmethod
    def __init__(self,id,id_banda,id_cidade,data,confirmado):
        self.__id = id
        self.__id_banda = id_banda
        self.__id_cidade = id_cidade
        self.__data = data
        self.__confirmado = confirmado

    def set_id(self,id): self.__id = id
    def set_id_banda(self,id_banda): self.__id_banda = id_banda
    def set_id_cidade(self,id_cidade): self.__id_cidade = id_cidade
    def set_data(self,data): self.__data = data
    def set_confirmado(self,confirmado): self.__confirmado = confirmado    

    def get_id(self): return self.__id
    def get_id_banda(self): return self.__id_banda
    def get_id_cidade(self): return self.__id_cidade
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
   

    def to_json(self):
        return {
        "id": self.__id,
        "id_banda": self.__id_banda,
        "id_cidade": self.__id_cidade,
        "data": self.__data.strftime("%d/%m/%Y %H:%M"),
        "confirmado": self.__confirmado,
        }

    def __str__(self):
        return f"{self.__id} - {self.__id_banda}  - {self.__id_cidade} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__confirmado}"
    
class NApresentacao:
    __apresentacoes = []
    @classmethod
    def inserir(cls,obj):
        cls.abrir()
        id=0
        for apresentacao in cls.__apresentacoes:
            id = apresentacao.get_id()
        obj.set_id(id+1)
        cls.__apresentacoes.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__apresentacoes
    
    @classmethod
    def listar_id(cls,id):
        cls.abrir()
        for apresentacao in cls.__apresentacoes:
            if apresentacao.get_id()==id:
                return apresentacao
        return None
    
    @classmethod
    def atualizar(cls,obj):
        cls.abrir()
        apresentacao = cls.listar_id(obj.get_id())
        if apresentacao is not None:
            apresentacao.set_idBanda(obj.get_id_banda())
            apresentacao.set_idCidade(obj.get_id_cidade())
            apresentacao.set_data(obj.get_data())
            apresentacao.set_confirmado(obj.get_confirmado())
            cls.salvar()

        
    @classmethod
    def excluir(cls,obj):
        cls.abrir()
        apresentacao = cls.listar_id(obj.get_id())
        if apresentacao is not None:
            cls.__apresentacoes.remove(apresentacao)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__apresentacoes =[]
        try:
            with open("apresentacaoes.json" , mode='r') as arquivo:
                apresentacoes_json = json.load(arquivo)
                for obj in apresentacoes_json:
                    a = Apresentacao(obj["id"],obj["id_banda"],obj["id_cidade"],obj["data"],obj["confirmado"])
                    cls.__apresentacoes.append(a)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        apresentacoes_salvar = []
        with open("apresentacoes.json",mode="w") as arquivo:
            for apresentacao in cls.__apresentacoes:
                apresentacoes_salvar.append(apresentacao.to_json())
            json.dump(apresentacoes_salvar,arquivo,indent=4)
        





