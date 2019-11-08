##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.65 - Programa 8.21 – Navegando listas a partir do tipo de seus elementos.py
# Descrição:  Programa 8.21 – Navegando listas a partir do tipo de seus elementos
##############################################################################

# Programa 8.21 – Navegando listas a partir do tipo de seus elementos
L = ["a", ["b", "c", "d"], "e"]
for x in L:
    if isinstance(type(x), str):
        print(x)
    else:
        print("Lista:")
        for z in x:
            print(z)
