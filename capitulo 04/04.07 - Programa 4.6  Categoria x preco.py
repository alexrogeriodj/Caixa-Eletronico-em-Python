##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 04\04.07 - Programa 4.6 – Categoria x preço.py
# Descrição:  Programa 4.6 – Categoria x preço
##############################################################################

# Programa 4.6 – Categoria x preço
1  categoria = int(input("Digite a categoria do produto:"))
2  if categoria == 1:
3      preço = 10
4  else:
5      if categoria == 2:
6          preço = 18
7      else:
8          if categoria == 3:
9              preço = 23
10         else:
11             if categoria == 4:
12                 preço = 26
13             else:
14                 if categoria == 5:
15                     preço = 31
16                 else:
17                     print("Categoria inválida, digite um valor entre 1 e 5!")
18                     preço = 0
19 print(f"O preço do produto é: R${preço:6.2f}")
