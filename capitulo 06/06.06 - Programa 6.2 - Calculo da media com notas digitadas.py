##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 06\06.06 - Programa 6.2 - Cálculo da média com notas digitadas.py
# Descrição:  Programa 6.2 - Cálculo da média com notas digitadas
##############################################################################

# Programa 6.2 - Cálculo da média com notas digitadas
notas = [0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 5:
    notas[x] = float(input(f"Nota {x}:"))
    soma += notas[x]
    x += 1
x = 0
while x < 5:
    print(f"Nota {x}: {notas[x]:6.2f}")
    x += 1
print(f"Média: {soma / x:5.2f}")
