##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 04\04.03 - Programa 4.2 - Carro novo ou velho, dependendo da idade.py
# Descrição:  Programa 4.2 - Carro novo ou velho, dependendo da idade
##############################################################################

# Programa 4.2 - Carro novo ou velho, dependendo da idade
idade = int(input("Digite a idade do seu carro: "))
if idade <= 3:
    print("Seu carro é novo")
if idade > 3:
    print("Seu carro é velho")
