##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 06\06.64 - Program 6.24 – Exemplo de dicionário com valor padrão.py
# Descrição:  Program 6.24 – Exemplo de dicionário com valor padrão
##############################################################################

# Program 6.24 – Exemplo de dicionário com valor padrão
d = {}
for letra in "abracadabra":
    d[letra] = d.get(letra, 0) + 1
print(d)
