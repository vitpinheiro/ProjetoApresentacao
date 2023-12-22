from datetime import datetime
import json
class Apresentacao:
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

    def __eq__(self, x):
        if x is not None:
            if self.__id == x.__id and self.__id_banda == x.__id_banda and self.__id_cidade == x.__id_cidade and self.__data== x.__data and self.__confirmado == x.__confirmado:
                return True
        return False
    

    def to_json(self):
        return{
        "id": self.__id,
        "id_banda": self.__id_banda,
        "id_cidade": self.__id_cidade,
        "data": self.get_data().strftime('%d/%m/%Y %H:%M'), 
        "confirmado": self.__confirmado,
        }

    def __str__(self):
        return f"{self.__id} - {self.__id_banda}  - {self.__id_cidade} - {self.get_data().strftime('%d/%m/%Y %H:%M')} - {self.__confirmado}"
    
from abc import ABC, abstractclassmethod

class NApresentacao(ABC):
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.objetos:
            if aux.get_id() > id: 
                id = aux.get_id()
        obj.set_id(id + 1)
        cls.objetos.append(obj)
        cls.salvar()


    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id: 
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.objetos.remove(aux)
            cls.salvar()


    @abstractclassmethod
    def abrir(cls):
        cls.objetos =[]
        try:
            with open("apresentacoes.json" , mode='r') as arquivo:
                apresentacoes_json = json.load(arquivo)
                for obj in apresentacoes_json:
                    obj["data"] = datetime.strptime(obj["data"], '%d/%m/%Y %H:%M')
                    a = Apresentacao(obj["id"], obj["id_banda"], obj["id_cidade"], obj["data"], obj["confirmado"])                    
                    cls.objetos.append(a)
        except FileNotFoundError:
            pass

    @abstractclassmethod
    def salvar(cls):
        apresentacoes_salvar = []
        with open("apresentacoes.json",mode="w") as arquivo:
            for apresentacao in cls.objetos:
                apresentacoes_salvar.append(apresentacao.to_json())
            json.dump(apresentacoes_salvar,arquivo,indent=4)

    




