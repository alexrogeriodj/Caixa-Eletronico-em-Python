##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2017
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Primeira reimpressão - Outubro/2011
# Segunda reimpressão - Novembro/2012
# Terceira reimpressão - Agosto/2013
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Primeira reimpressão - Segunda edição - Maio/2015
# Segunda reimpressão - Segunda edição - Janeiro/2016
# Terceira reimpressão - Segunda edição - Junho/2016
# Quarta reimpressão - Segunda edição - Março/2017
#
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem\capitulo 04\04.07 - Categoria x preço.py
##############################################################################

categoria = int(input("Digite a categoria do produto:"))
if categoria == 1:
    preço = 10
else:
    if categoria == 2:
       preço = 18
    else:
       if categoria == 3:
          preço = 23
       else:
          if categoria == 4:
             preço = 26
          else:
             if categoria == 5:
                preço = 31
             else:
                print("Categoria inválida, digite um valor entre 1 e 5!")
                preço = 0
print("O preço do produto é: R$%6.2f" % preço)
