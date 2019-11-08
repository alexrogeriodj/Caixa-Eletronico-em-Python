##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.55 - Programa 8.19 – Módulo soma (soma.py) que importa entrada.py
# Descrição:  Programa 8.19 – Módulo soma (soma.py) que importa entrada
##############################################################################

# Programa 8.19 – Módulo soma (soma.py) que importa entrada
import entrada
L = []
for x in range(10):
    L.append(entrada.valida_inteiro("Digite um número:", 0, 20))
print(f"Soma: {sum(L)}")
