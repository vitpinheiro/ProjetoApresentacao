import json
from models.modelo import Modelo

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
    def __eq__(self, x):
        if x is not None:
            if self.__id == x.__id and self.__nome == x.__nome:
                return True
        return False

    def __str__(self):
        return f"{self.__id} - {self.__nome}"

class NCidade(Modelo):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("cidades.json", mode='r') as arquivo:
                cidades_json = json.load(arquivo)
                for obj in cidades_json:
                    c = Cidade(obj["id"], obj["nome"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        cidades_salvar = []
        with open("cidades.json", mode="w") as arquivo:
            for cidade in cls.objetos:
                cidades_salvar.append(cidade.to_json())
            json.dump(cidades_salvar, arquivo, indent=4)

