class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])

    from clientes import Cliente
	from contas import Conta, ContaEspecial
	joão = Cliente("João da Silva", "777-1234")
	maria = Cliente("Maria da Silva", "555-4321")
	conta1 = Conta([joão], 1, 1000)
	conta2 = ContaEspecial([maria, joão], 2, 500, 1000)
	conta1.saque(50)
	conta2.deposito(300)
	conta1.saque(190)
	conta2.deposito(95.15)
	conta2.saque(1500)
	conta1.extrato()
	conta2.extrato()