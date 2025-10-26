from abstratas import Pessoa, Quarto
class Hospede(Pessoa):
    def __init__(self, nome, idade, dias_estadia, quarto = None):
        super().__init__(nome, idade)

        self.dias_estadia = dias_estadia
        self.quarto = quarto

    def mostrar_informacoes(self):
        return f'Hóspede: {self.nome}, Idade: {self.idade}, Dias de Estadia: {self.dias_estadia}, Quarto: {self.quarto.numero if self.quarto else "Nenhum"}'

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def mostrar_informacoes(self):
        return f'Funcionário: {self.nome}, Idade: {self.idade}, Salário: {self.salario}'
    
    @property
    def nome(self):
        return self._nome  

    @nome.setter
    def nome(self, nome):
        self._nome = nome 
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade
    
class Gerente(Funcionario):
    def __init__(self, nome, idade, salario, bonus):
        super().__init__(nome, idade, salario)
        self.bonus = bonus

    def mostrar_informacoes(self):
        return f'Gerente: {self.nome}, Idade: {self.idade}, Salário: {self.salario}, Bônus: {self.bonus}'
    
    def calcular_salario_total(self):
        return self.salario + self.bonus
    
    @property
    def nome(self): 
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade

class Recepcionista(Funcionario):
    def __init__(self, nome, idade, salario, turno):
        super().__init__(nome, idade, salario)
        self.turno = turno

    def mostrar_informacoes(self):
        return f'Recepcionista: {self.nome}, Idade: {self.idade}, Salário: {self.salario}, Turno: {self.turno}'
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade 

    @property
    def turno(self):
        return self._turno
    
    @turno.setter
    def turno(self, turno):
        self._turno = turno

class TecnicoManutencao(Funcionario):
    def __init__(self, nome, idade, salario, especialidade):
        super().__init__(nome, idade, salario)
        self.especialidade = especialidade

    def mostrar_informacoes(self):
        return f'Técnico de Manutenção: {self.nome}, Idade: {self.idade}, Salário: {self.salario}, Especialidade: {self.especialidade}'
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade

    @property
    def especialidade(self):
        return self._especialidade
    
    @especialidade.setter
    def especialidade(self, especialidade):
        self._especialidade = especialidade

class TecnicoRecepcao(Funcionario):
    def __init__(self, nome, idade, salario, especialidade, turno):
        super().__init__(nome, idade, salario)
        self.especialidade = especialidade
        self.turno = turno

    def mostrar_informacoes(self):
        return f'Técnico de Recepção: {self.nome}, Idade: {self.idade}, Salário: {self.salario}, Especialidade: {self.especialidade}, Turno: {self.turno}'
    
    @property
    def nome(self):
        return self._nome  
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade

class QuartoSimples(Quarto):
    def __init__(self, numero, preco_diaria):
        super().__init__(numero, "Simples", preco_diaria)
        self.ocupado = False

    def mostrar_informacoes(self):
        return f'Quarto Simples Nº: {self.numero}, Preço Diária: {self.preco_diaria}, Ocupado: {self.ocupado}'
    
    @property
    def ocupado(self):
        return self._ocupado
    
    @ocupado.setter
    def ocupado(self, ocupado):
        self._ocupado = ocupado

    @property
    def preco_diaria(self):
        return self._preco_diaria
    
    @preco_diaria.setter
    def preco_diaria(self, preco_diaria):
        self._preco_diaria = preco_diaria

class QuartoLuxo(Quarto):
    def __init__(self, numero, preco_diaria):
        super().__init__(numero, "Luxo", preco_diaria)
        self.ocupado = False

    def mostrar_informacoes(self):
        return f'Quarto Luxo Nº: {self.numero}, Preço Diária: {self.preco_diaria}, Ocupado: {self.ocupado}'
    
    @property
    def ocupado(self):
        return self._ocupado
    
    @ocupado.setter
    def ocupado(self, ocupado):
        self._ocupado = ocupado

    @property
    def preco_diaria(self):
        return self._preco_diaria
    
    @preco_diaria.setter
    def preco_diaria(self, preco_diaria):
        self._preco_diaria = preco_diaria

