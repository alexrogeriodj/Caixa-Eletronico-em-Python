##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 09\09.09.py
# Descrição:
##############################################################################

with open("múltiplos de 4.txt", "w") as múltiplos4:
    with open("pares.txt") as pares:
        for l in pares.readlines():
            if int(l) % 4 == 0:
                múltiplos4.write(l)
