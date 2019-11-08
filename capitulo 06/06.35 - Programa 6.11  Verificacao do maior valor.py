##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 06\06.35 - Programa 6.11 – Verificação do maior valor.py
# Descrição:  Programa 6.11 – Verificação do maior valor
##############################################################################

# Programa 6.11 – Verificação do maior valor
L = [1, 7, 2, 4]
máximo = L[0]
for e in L:
    if e > máximo:
        máximo = e
print(máximo)
