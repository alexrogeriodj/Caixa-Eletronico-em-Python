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
# Arquivo: listagem\capitulo 06\06.50 - Obtenção do preço com um dicionário.py
##############################################################################

tabela = { "Alface": 0.45,
           "Batata": 1.20,
           "Tomate": 2.30,
           "Feijão": 1.50 }
while True:
     produto = input("Digite o nome do produto, fim para terminar:")
     if produto == "fim":
         break
     if produto in tabela:
         print("Preço %5.2f" % tabela[produto])
     else:
         print("Produto não encontrado!")
