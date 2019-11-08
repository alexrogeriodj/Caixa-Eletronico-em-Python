##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 06\06.41 - Programa 6.15 - Impressão de uma lista de strings, letra a letra.py
# Descrição:  Programa 6.15 - Impressão de uma lista de strings, letra a letra
##############################################################################

# Programa 6.15 - Impressão de uma lista de strings, letra a letra
L = ["maçãs", "peras", "kiwis"]
for s in L:
    for letra in s:
        print(letra)
