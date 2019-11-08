##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 05\05.16.py
# Descrição:
##############################################################################

tabuada = 1
número = 1
while tabuada <= 10:
    print(f"{tabuada} x {número} = {tabuada * número}")
    número += 1
    if número == 11:
        número = 1
        tabuada += 1
