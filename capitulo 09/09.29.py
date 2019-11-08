##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 09\09.29.py
# Descrição:
##############################################################################

import os
import os.path
import time
import sys
nome = sys.argv[1]
print(f"Nome: {nome}")
print(f"Tamanho: {os.path.getsize(nome)}")
print(f"Criado: {time.ctime(os.path.getctime(nome))}")
print(f"Modificado: {time.ctime(os.path.getmtime(nome))}")
print(f"Acessado: {time.ctime(os.path.getatime(nome))}")
