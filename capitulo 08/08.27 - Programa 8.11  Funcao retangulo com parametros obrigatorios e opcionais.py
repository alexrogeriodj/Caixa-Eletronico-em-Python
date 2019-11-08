##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2019
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira edição - Janeiro/2019 - ISBN 978-85-7522-718-3
# Site: http://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 08\08.27 - Programa 8.11 – Função retângulo com parâmetros obrigatórios e opcionais.py
# Descrição:  Programa 8.11 – Função retângulo com parâmetros obrigatórios e opcionais
##############################################################################


# Programa 8.11 – Função retângulo com parâmetros obrigatórios e opcionais
def retângulo(largura, altura, caractere="*"):
    linha = caractere * largura
    for i in range(altura):
        print(linha)
