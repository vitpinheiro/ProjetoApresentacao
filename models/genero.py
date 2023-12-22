import json
class Genero:
    def __init__(self,id,nome):
        self.__id = id
        self.__nome = nome

    def set_id(self,id): self.__id = id
    def set_nome(self,nome): self.__nome = nome
    

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome
   

    def to_json(self):
        return  {
        "id": self.__id,
        "nome": self.__nome}
    def __eq__(self, x):
        if x is not None:
            if self.__id == x.__id and self.__nome == x.__nome:
                return True
        return False

    def __str__(self):
        return f"{self.__id} - {self.__nome}"
    
from abc import ABC, abstractclassmethod

class NGenero(ABC):
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id=0
        for aux in cls.objetos:
            for aux in cls.objetos:
                if aux.get_id() > id: 
                    id = aux.get_id()
        obj.set_id(id+1)
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
        cls.objetos = []
        try:
            with open("generos.json", mode='r') as arquivo:
                generos_json = json.load(arquivo)
                for obj in generos_json:
                    g = Genero(obj["id"], obj["nome"])
                    cls.objetos.append(g)
        except FileNotFoundError:
            pass
    @abstractclassmethod
    def salvar(cls):
        generos_salvar = []
        with open("generos.json",mode="w") as arquivo:
            for genero in cls.objetos:
                generos_salvar.append(genero.to_json())
            json.dump(generos_salvar,arquivo,indent=4)
        





