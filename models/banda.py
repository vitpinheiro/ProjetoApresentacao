import json
from models.modelo import Modelo
class Banda:
    def __init__(self,id,id_genero,nome,fone,email,senha):
        self.__id = id
        self.__id_genero = id_genero
        self.__nome  = nome
        self.__fone = fone
        self.__email = email
        self.__senha = senha
    
    def set_id(self,id): self.__id = id
    def set_id_genero(self,id_genero): self.__id_genero = id_genero
    def set_nome(self,nome): self.__nome = nome
    def set_fone(self,fone): self.__fone = fone
    def set_email(self,email): self.__email = email
    def set_senha(self,senha) : self.__senha = senha

    def get_id(self): return self.__id
    def get_id_genero(self): return self.__id_genero
    def get_nome(self): return self.__nome
    def get_fone(self): return self.__fone
    def get_email(self): return self.__email
    def get_senha(self): return self.__senha
    def __eq__(self, x):
        if x is not None:
            if self.__id == x.__id and self.__id_genero == x.__id_genero and self.__nome == x.__nome and self.__fone== x.__fone and self.__email == x.__email and self.__senha ==x.__senha:
                return True
        return False

    def to_json(self):
        return {
        "id": self.__id,
        "id_genero": self.__id_genero,
        "nome": self.__nome,
        "fone" : self.__fone,
        "email": self.__email,
        "senha": self.__senha
        }

    def __str__(self):
        return f"{self.__id} - {self.__id_genero} - {self.__nome} - {self.__fone} - {self.__email} - {self.__senha}"
    
class NBanda(Modelo):

    @classmethod
    def abrir(cls):
        cls.objetos =[]
        try:
            with open("bandas.json" , mode='r') as arquivo:
                bandas_json = json.load(arquivo)
                for obj in bandas_json:
                    b = Banda(obj["id"],obj["id_genero"],obj["nome"],obj["fone"],obj["email"],obj["senha"])
                    cls.objetos.append(b)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        bandas_salvar = []
        with open("bandas.json",mode="w") as arquivo:
            for banda in cls.objetos:
                bandas_salvar.append(banda.to_json())
            json.dump(bandas_salvar,arquivo,indent=4)
        





