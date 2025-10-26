from abc import ABC, abstractmethod
class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def mostrar_informacoes(self):
        pass

    
    @property
    @abstractmethod
    def nome(self):
        pass

    @nome.setter
    @abstractmethod
    def nome(self, nome):
        pass

    @property
    @abstractmethod
    def idade(self):
        pass

    @idade.setter
    @abstractmethod
    def idade(self, idade):
        pass

class Quarto(ABC):
    def __init__(self, numero, tipo, preco_diaria):
        self.numero = numero
        self.tipo = tipo
        self.preco_diaria = preco_diaria

    @abstractmethod
    def mostrar_informacoes(self):
        pass

    @property
    @abstractmethod
    def ocupado(self):
        pass

    @ocupado.setter
    @abstractmethod
    def ocupado(self, ocupado):
        pass

    @property
    @abstractmethod
    def preco_diaria(self):
        pass

    @preco_diaria.setter
    @abstractmethod
    def preco_diaria(self, preco_diaria):
        pass

