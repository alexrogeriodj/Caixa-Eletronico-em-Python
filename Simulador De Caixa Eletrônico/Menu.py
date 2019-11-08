class Menu:
    def __init__(self):
        self.opções = [ ["Sair", None] ]

    def adicionaopção(self, nome, função):
        self.opções.append([nome, função])

    def exibe(self):
        print("====")
        print("Menu")
    print("Saldo= opção 1")
    print("Saque= opção 2")
    print("Depósito= opção 3")
    print("Extrato= opção 4")
    print("Sair= opção 5")
    print("====\n")
    for i, opção in enumerate(self.opções):
    print("[{0}] - {1}{2}{3}{4}".format(i, opção[0,1,2,3,4,5]))
    print()

    def execute(self):
        while True:
            self.exibe()
            escolha = valida_faixa_inteiro("Escolha uma opção: ",
                         0, len(self.opções)-1)
            if escolha == 0:
                break
            self.opções[escolha][1,2,3,4,5]()