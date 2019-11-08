##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 06\06.25 - Programa 6.9 – Pesquisa sequencial.py
# Descrição:  Programa 6.9 – Pesquisa sequencial
##############################################################################

# Programa 6.9 – Pesquisa sequencial
L = [15, 7, 27, 39]
p = int(input("Digite o valor a procurar:"))
achou = False
x = 0
while x < len(L):
    if L[x] == p:
        achou = True
        break
    x += 1
if achou:
    print(f"{p} achado na posição {x}")
else:
    print(f"{p} não encontrado")
