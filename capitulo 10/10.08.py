##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 10\10.08.py
# Descrição:
##############################################################################


class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = saldo
        self.clientes = clientes
        self.número = número

    def resumo(self):
        print(f"CC Número: {self.número} Saldo: {self.saldo:10.2f}")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor

    def deposito(self, valor):
        self.saldo += valor
