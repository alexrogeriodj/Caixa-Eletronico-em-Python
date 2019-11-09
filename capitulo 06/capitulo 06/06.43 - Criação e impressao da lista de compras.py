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
# Arquivo: listagem\capitulo 06\06.43 - Criação e impressao da lista de compras.py
##############################################################################

compras = [   ]
while True:
     produto = input("Produto: ")
     if produto == "fim":
         break
     quantidade = int(input("Quantidade: "))
     preço = float(input("Preço: "))
     compras.append([produto, quantidade, preço])
soma = 0.0
for e in compras:
     print("%20s x%5d %5.2f %6.2f" % (e[0],
                         e[1],e[2],
                         e[1] * e[2]))
     soma += e[1] * e[2]
print("Total: %7.2f" % soma)
