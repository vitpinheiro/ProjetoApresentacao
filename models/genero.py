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
    
class NGenero:
    __generos = []
    @classmethod
    def inserir(cls,obj):
        cls.abrir()
        id=0
        for genero in cls.__generos:
            id = genero.get_id()
        obj.set_id(id+1)
        cls.__generos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.__generos
    
    @classmethod
    def listar_id(cls,id):
        cls.abrir()
        for genero in cls.__generos:
            if genero.get_id()==id:
                return genero
        return None
    
    @classmethod
    def atualizar(cls,obj):
        cls.abrir()
        genero = cls.listar_id(obj.get_id())
        if genero is not None:
            genero.set_nome(obj.get_nome())
            cls.salvar()
        
    @classmethod
    def excluir(cls,obj):
        cls.abrir()
        genero = cls.listar_id(obj.get_id())
        if genero is not None:
            cls.__generos.remove(genero)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.__generos = []
        try:
            with open("generos.json", mode='r') as arquivo:
                generos_json = json.load(arquivo)
                for obj in generos_json:
                    g = Genero(obj["id"], obj["nome"])
                    cls.__generos.append(g)
        except FileNotFoundError:
            pass
    @classmethod
    def salvar(cls):
        generos_salvar = []
        with open("generos.json",mode="w") as arquivo:
            for genero in cls.__generos:
                generos_salvar.append(genero.to_json())
            json.dump(generos_salvar,arquivo,indent=4)
        





