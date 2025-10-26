from herdadas import QuartoLuxo, QuartoSimples, Hospede

class Hotel:
    def __init__(self):
        self.hospedes = []
        self.quartos = []
    
    def adicionar_hospede(self, hospede):
        self.hospedes.append(hospede)

    def adicionar_quarto(self, quarto):
        self.quartos.append(quarto)

    def listar_hospedes(self):
        for hospede in self.hospedes:
            print(hospede.mostrar_informacoes())

    def listar_quartos(self):
        for quarto in self.quartos:
            print(quarto.mostrar_informacoes())

hospedes = []
quartoSimples = []
quartoLuxo = []
option = 0

def registrar_hospede(hospedes, nome, idade, dias_estadia):
    hospede = Hospede(nome, idade, dias_estadia)
    hospede._nome = input("Digite o nome do hóspede: ")
    hospede._idade = int(input("Digite a idade do hóspede: "))
    hospede.dias_estadia = int(input("Digite os dias de estadia do hóspede: "))
    hospedes.append(hospede)

def registrar_quarto_simples(quartoSimples, numero, preco_diaria):
    quarto = QuartoSimples(numero, preco_diaria)
    quarto._numero = input("Digite o número do quarto simples: ")
    quarto._preco_diaria = float(input("Digite o preço da diária do quarto simples: "))
    quartoSimples.append(quarto)

def registrar_quarto_luxo(quartoLuxo, numero, preco_diaria):
    quarto = QuartoLuxo(numero, preco_diaria)
    quarto._numero = input("Digite o número do quarto luxo: ")
    quarto._preco_diaria = float(input("Digite o preço da diária do quarto luxo: "))
    quartoLuxo.append(quarto)

def atribuir_quarto(hospedes, quartoSimples, quartoLuxo):
    nome_hospede = input("Digite o nome do hóspede para atribuir um quarto: ")
    op = 0

    quarto_simples_encontrado = None
    quarto_luxo_encontrado = None
    
    hospede_encontrado = None
    for hospede in hospedes:
        if hospede.nome == nome_hospede:
            hospede_encontrado = hospede
            break

    print("Quarto luxo ou simples?")
    op = int(input("Digite 1 para simples ou 2 para luxo: "))
    if op == 1:
        numero_quarto = input("Digite o número do quarto a ser atribuído: ")
        for quarto in quartoSimples:
            if quarto.numero == numero_quarto and not quarto.ocupado:
                quarto_simples_encontrado = quarto
                break

    elif op == 2:
        numero_quarto = input("Digite o número do quarto a ser atribuído: ")
        for quarto in quartoLuxo:
            if quarto.numero == numero_quarto and not quarto.ocupado:
                quarto_luxo_encontrado = quarto
                break
    
    if hospede_encontrado and quarto_simples_encontrado:
        hospede_encontrado.quarto = quarto_simples_encontrado
        quarto_simples_encontrado.ocupado = True
        print(f'Quarto simples Nº {quarto_simples_encontrado.numero} atribuído ao hóspede {hospede_encontrado.nome}.')

    elif hospede_encontrado and quarto_luxo_encontrado:
        hospede_encontrado.quarto = quarto_luxo_encontrado
        quarto_luxo_encontrado.ocupado = True
        print(f'Quarto luxo Nº {quarto_luxo_encontrado.numero} atribuído ao hóspede {hospede_encontrado.nome}.')

    else:
        print("Hóspede ou quarto não encontrado, ou o quarto já está ocupado.")

print("=== Bem-vindo ao Sistema de Gerenciamento do Hotel ===")

option = int(input("Digite:\n 1 para registrar um hóspede\n 2 para registrar um quarto simples\n 3 para registrar um quarto luxo\n 4 para listar hóspedes\n 5 para listar quartos\n 6 para atrubuir quarto a um cliente\n 0 para sair: "))
while option != 0:
    if option == 1:
        registrar_hospede(hospedes, None, None, None)
    elif option == 2:
        registrar_quarto_simples(quartoSimples, None, None)
    elif option == 3:
        registrar_quarto_luxo(quartoLuxo, None, None)
    elif option == 4:
        print("=== Lista de Hóspedes ===")
        for hospede in hospedes:
            print(hospede.mostrar_informacoes())
    elif option == 5:
        print("=== Lista de Quartos Simples ===")
        for quarto in quartoSimples:
            print(quarto.mostrar_informacoes())
        print("=== Lista de Quartos Luxo ===")
        for quarto in quartoLuxo:
            print(quarto.mostrar_informacoes())
    elif option == 6:
        atribuir_quarto(hospedes, quartoSimples, quartoLuxo)
    elif option == 0:
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
    
    option = int(input("Digite:\n 1 para registrar um hóspede\n 2 para registrar um quarto simples\n 3 para registrar um quarto luxo\n 4 para listar hóspedes\n 5 para listar quartos\n 6 para atrubuir quarto a um cliente\n 0 para sair: "))


