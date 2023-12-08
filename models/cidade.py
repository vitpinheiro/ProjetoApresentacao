import json
import datetime

class Cidade:
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome

    def get_id(self): return self.__id
    def get_nome(self): return self.__nome

    def set_id(self, id): self.__id = id
    def set_nome(self, nome): self.__nome = nome

    def to_json(self):
        return {
            "id": self.__id,
            "nome": self.__nome
        }

    def __str__(self):
        return f"{self.__id} - {self.__nome}"

class NCidade:
    __cidades = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for cidade in cls.__cidades:
            if cidade.get_id() > id:
                id = cidade.get_id()
        obj.set_id(id + 1)
        cls.__cidades.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__cidades

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for cidade in cls.__cidades:
            if cidade.get_id() == id:
                return cidade
        return None


    @classmethod
    def atualizar(cls, obj):
        cls.abrir()
        cidade = cls.listar_id(obj.get_id())
        if cidade is not None:
            cidade.set_nome(obj.get_nome())
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        cls.abrir()
        cidade = cls.listar_id(obj.get_id())
        if cidade is not None:
            cls.__cidades.remove(cidade)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__cidades = []
        try:
            with open("cidades.json", mode='r') as arquivo:
                cidades_json = json.load(arquivo)
                for obj in cidades_json:
                    c = Cidade(obj["id"], obj["nome"])
                    cls.__cidades.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        cidades_salvar = []
        with open("cidades.json", mode="w") as arquivo:
            for cidade in cls.__cidades:
                cidades_salvar.append(cidade.to_json())
            json.dump(cidades_salvar, arquivo, indent=4)
