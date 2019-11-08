##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 06\06.39 - Programa 6.14 – Lendo e imprimindo uma lista de compras.py
# Descrição:  Programa 6.14 – Lendo e imprimindo uma lista de compras
##############################################################################

# Programa 6.14 – Lendo e imprimindo uma lista de compras
compras = []
while True:
    produto = input("Produto:")
    if produto == "fim":
        break
    compras.append(produto)
for p in compras:
    print(p)
