import json
class Banda:
    def __init__(self,id,genero,nome,fone,email,senha):
        self.__id = id
        self.__genero = genero
        self.__nome  = nome
        self.__fone = fone
        self.__email = email
        self.__senha = senha
    
    def set_id(self,id): self.__id = id
    def set_genero(self,genero): self.__genero = genero
    def set_nome(self,nome): self.__nome = nome
    def set_fone(self,fone): self.__fone = fone
    def get_email(self,email): self.__email = email
    def set_senha(self,senha) : self.__senha = senha

    def get_id(self): return self.__id
    def get_genero(self): return self.__genero
    def get_nome(self): return self.__nome
    def get_fone(self): return self.__fone
    def get_email(self): return self.__email
    def get_senha(self): return self.__senha

    def to_json(self):
        return {
        "id": self.__id,
        "genero": self.__genero,
        "nome": self.__nome,
        "fone" : self.__fone,
        "email": self.__email,
        "senha": self.__senha
        }

    def __str__(self):
        return f"{self.__id} - {self.__genero} - {self.__nome} - {self.__fone} - {self.__email} - {self.__senha}"
    
class NBanda:
    __bandas = []
    @classmethod
    def inserir(cls,obj):
        cls.abrir()
        id=0
        for banda in cls.__bandas:
            id = banda.get_id()
        obj.set_id(id+1)
        cls.__bandas.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__bandas
    
    @classmethod
    def listar_id(cls,id):
        cls.abrir()
        for banda in cls.__bandas:
            if banda.get_id()==id:
                return banda
        return None
    
    @classmethod
    def atualizar(cls,obj):
        cls.abrir()
        banda = cls.listar_id(obj.get_id())
        if banda is not None:
            banda.set_genero(obj.get_genero())
            banda.set_nome(obj.get_nome())
            banda.set_fone(obj.get_fone())
            banda.set_email(obj.get_email())
            banda.set_senha(obj.get_senha())
            cls.salvar()

    @classmethod
    def excluir(cls,obj):
        cls.abrir()
        banda = cls.listar_id(obj.get_id())
        if banda is not None:
            cls.__bandas.remove(banda)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__bandas =[]
        try:
            with open("bandas.json" , mode='r') as arquivo:
                bandas_json = json.load(arquivo)
                for obj in bandas_json:
                    b = Banda(obj["id"],obj["genero"],obj["nome"],obj["fone"],obj["email"],obj["senha"])
                    cls.__bandas.append(b)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        bandas_salvar = []
        with open("bandas.json",mode="w") as arquivo:
            for banda in cls.__bandas:
                bandas_salvar.append(banda.to_json())
            json.dump(bandas_salvar,arquivo,indent=4)
        





