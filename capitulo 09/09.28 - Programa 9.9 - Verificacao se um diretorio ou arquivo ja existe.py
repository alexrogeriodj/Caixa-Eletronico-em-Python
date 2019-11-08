##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 09\09.28 - Programa 9.9 - Verificação se um diretório ou arquivo já existe.py
# Descrição:  Programa 9.9 - Verificação se um diretório ou arquivo já existe
##############################################################################

# Programa 9.9 - Verificação se um diretório ou arquivo já existe
import os.path
if os.path.exists("z"):
    print("O diretório z existe.")
else:
    print("O diretório z não existe.")
