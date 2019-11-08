##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.57 - Programa 8.20 – Adivinhando o número.py
# Descrição:  Programa 8.20 – Adivinhando o número
##############################################################################

# Programa 8.20 – Adivinhando o número
import random
n = random.randint(1, 10)
x = int(input("Escolha um número entre 1 e 10:"))
if x == n:
    print("Você acertou!")
else:
    print("Você errou.")
