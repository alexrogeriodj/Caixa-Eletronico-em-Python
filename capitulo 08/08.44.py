##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.44.py
# Descrição:
##############################################################################

nomes = ["Ana", "Carlos", "Maria"]
try:
    i = int(input("Digite o índice que quer imprimir:"))
    print(nomes[i])
except ValueError as e:
    print("Digite um número!")
    raise
finally:
    print(f"Sempre o finally é executado")
