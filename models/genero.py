import json
from models.modelo import Modelo
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
    

class NGenero(Modelo):

    @classmethod
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
    @classmethod
    def salvar(cls):
        generos_salvar = []
        with open("generos.json",mode="w") as arquivo:
            for genero in cls.objetos:
                generos_salvar.append(genero.to_json())
            json.dump(generos_salvar,arquivo,indent=4)
        





