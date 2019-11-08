##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 04\04.02 - Programa 4.1 – Lê dois valores e imprime qual é o maior.py
# Descrição:  Programa 4.1 – Lê dois valores e imprime qual é o maior
##############################################################################

# Programa 4.1 – Lê dois valores e imprime qual é o maior
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
if a > b:
    print("O primeiro valor é o maior!")
if b > a:
    print("O segundo valor é o maior!")
