##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.19 - Programa 8.8 - Exemplo de validação sem usar uma função.py
# Descrição:  Programa 8.8 - Exemplo de validação sem usar uma função
##############################################################################

# Programa 8.8 - Exemplo de validação sem usar uma função
while True:
    v = int(input("Digite um valor entre 0 e 5:"))
    if v < 0 or v > 5:
        print("Valor inválido.")
    else:
        break
