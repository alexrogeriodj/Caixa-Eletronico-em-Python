##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 09\09.07 - Programa 9.3 – Gravação de números pares e ímpares em arquivos diferentes.py
# Descrição:  Programa 9.3 – Gravação de números pares e ímpares em arquivos diferentes
##############################################################################

# Programa 9.3 – Gravação de números pares e ímpares em arquivos diferentes
with open("ímpares.txt", "w") as ímpares:
    with open("pares.txt", "w") as pares:
        for n in range(0, 1000):
            if n % 2 == 0:
                pares.write(f"{n}\n")
            else:
                ímpares.write(f"{n}\n")
