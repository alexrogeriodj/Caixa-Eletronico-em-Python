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
# Arquivo: exercicios\capitulo 07\exercicio-07-07.py
##############################################################################

palavra = input("Digite a palavra secreta:").lower().strip()
for x in range(100):
     print()
digitadas = []
acertos = []
erros = 0
while True:
     senha = ""
     for letra in palavra:
         senha += letra if letra in acertos else "."
     print(senha)
     if senha == palavra:
         print("Você acertou!")
         break
     tentativa = input("\nDigite uma letra:").lower().strip()
     if tentativa in digitadas:
         print("Você já tentou esta letra!")
         continue
     else:
         digitadas += tentativa
         if tentativa in palavra:
               acertos += tentativa
         else:
               erros += 1
               print("Você errou!")
     print("X==:==\nX  :   ")
     print("X  O   " if erros >= 1 else "X")
     linha2 = ""
     if erros == 2:
         linha2 = "  |   "
     elif erros == 3:
         linha2 = " \|   "
     elif erros >= 4:
         linha2 = " \|/ "
     print("X%s" % linha2)
     linha3 = ""
     if erros == 5:
         linha3 += " /     "
     elif erros >= 6:
         linha3 += " / \ "
     print("X%s" % linha3)
     print("X\n===========")
     if erros == 6:
         print("Enforcado!")
         print("A palavra secreta era: %s" % palavra)
         break
