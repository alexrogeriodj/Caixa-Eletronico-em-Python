##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 04\04.04 - Programa 4.3 – Cálculo do Imposto de Renda.py
# Descrição:  Programa 4.3 – Cálculo do Imposto de Renda
##############################################################################

# Programa 4.3 – Cálculo do Imposto de Renda
salário = float(input("Digite o salário para cálculo do imposto: "))
base = salário
imposto = 0
if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)
print(f"Salário: R${salário:6.2f} Imposto a pagar: R${imposto:6.2f}")
