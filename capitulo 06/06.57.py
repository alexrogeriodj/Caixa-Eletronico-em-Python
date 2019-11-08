##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 06\06.57.py
# Descrição:
##############################################################################

L = [0] * 10
hash("A")
hash("A") % 10  # Se utilizarmos o resto da divisão entre o hash e o tamanho da lista, teremos um índice a partir da chave
L[hash("A") % 10] = "A"
L
