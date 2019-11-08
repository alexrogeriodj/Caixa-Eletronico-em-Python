##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 06\06.07 - Programa 6.3 – Apresentação de números.py
# Descrição:  Programa 6.3 – Apresentação de números
##############################################################################

# Programa 6.3 – Apresentação de números
números = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    números[x] = int(input(f"Número {x + 1}:"))
    x += 1
while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    print(f"Você escolheu o número: {números[escolhido - 1]}")
