##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 04\04.06 - Programa 4.5 - Conta de telefone com três faixas de preço.py
# Descrição:  Programa 4.5 - Conta de telefone com três faixas de preço
##############################################################################

# Programa 4.5 - Conta de telefone com três faixas de preço
minutos = int(input("Quantos minutos você utilizou este mês:"))
if minutos < 200:
    preço = 0.20
else:
    if minutos < 400:
        preço = 0.18
    else:
        preço = 0.15
print(f"Você vai pagar este mês: R${minutos * preço:6.2f}")
