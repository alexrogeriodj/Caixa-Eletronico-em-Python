##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 09\09.34 - Programa 9.10 – Árvore de diretórios sendo percorrida.py
# Descrição:  Programa 9.10 – Árvore de diretórios sendo percorrida
##############################################################################

# Programa 9.10 – Árvore de diretórios sendo percorrida
import os
import sys
for raiz, diretorios, arquivos in os.walk(sys.argv[1]):
    print("\nCaminho:", raiz)
    for d in diretorios:
        print(f"  {d}/")
    for f in arquivos:
        print(f"  {f}")
    print(f"{len(diretorios)} diretório(s), {len(arquivos)} arquivo(s)")
