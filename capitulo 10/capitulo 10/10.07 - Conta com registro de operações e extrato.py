##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2017
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Primeira reimpressão - Outubro/2011
# Segunda reimpressão - Novembro/2012
# Terceira reimpressão - Agosto/2013
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Primeira reimpressão - Segunda edição - Maio/2015
# Segunda reimpressão - Segunda edição - Janeiro/2016
# Terceira reimpressão - Segunda edição - Junho/2016
# Quarta reimpressão - Segunda edição - Março/2017
#
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem\capitulo 10\10.07 - Conta com registro de operações e extrato.py
##############################################################################

class Conta:
     def __init__(self, clientes, número, saldo = 0):
         self.saldo = 0
         self.clientes = clientes
         self.número = número
         self.operações = []
         self.deposito(saldo)
     def resumo(self):
         print("CC N°%s Saldo: %10.2f" %
               (self.número, self.saldo))
     def saque(self, valor):
         if self.saldo >= valor:
               self.saldo -= valor
               self.operações.append(["SAQUE", valor])
     def deposito(self, valor):
         self.saldo += valor
         self.operações.append(["DEPÓSITO", valor])
     def extrato(self):
         print("Extrato CC N° %s\n" % self.número)
         for o in self.operações:
               print("%10s %10.2f" % (o[0],o[1]))
         print("\n       Saldo: %10.2f\n" % self.saldo)
