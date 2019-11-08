CI240 - Fundamentos de Programação - 30/10/2019



TRABALHO 



Faça um programa em Python para simular ações em um caixa eletrônico, considerando que:

1) O usuário possui um saldo inicial de R$1000 (mil reais). 

2) As notas disponíveis são de R$100, R$50, R$20 e R$10. 

3) O caixa possui a quantidade de 20 para cada valor de notas disponíveis. Ou seja, o programa

   deve iniciar com 20 notas de R$100, 20 de R$50, 20 de R$20 e 20 de R$10.





O programa deve iniciar mostrando um menu de opções ao usuário, como abaixo:

----------------------------------------------------------

Bem vindo ao Banco CI240

----------------------------------------------------------

  Caixa Eletrônico

    [1] Saldo

    [2] Saque

    [3] Depósito

    [4] Extrato

    [5] Sair

  Digite a opção desejada:





Ao digitar 1, opção Saldo, o programa deve mostrar o saldo da conta e em

seguida o menu para que o usuário possa escolher nova operação, como no exemplo:



----------------------------------------------------------

Bem vindo ao Banco CI240

----------------------------------------------------------

  Caixa Eletrônico

    [1] Saldo

    [2] Saque

    [3] Depósito

    [4] Extrato

    [5] Sair

  Digite a opção desejada: 1

----------------------------------------------------------

    Saldo atual: R$1000

----------------------------------------------------------



----------------------------------------------------------

Bem vindo ao Banco CI240

----------------------------------------------------------

  Caixa Eletrônico

    [1] Saldo

    [2] Saque

    [3] Depósito

    [4] Extrato

    [5] Sair

  Digite a opção desejada:





Se o usuário escolher a opção 2, Saque, o programa deve perguntar o valor

desejado e em seguida calcular a quantidade de cada uma das notas que serão

entregues ao usuário. O programa deve minimizar o número de notas para o 

usuário, ou seja, se por exemplo o valor do saque for 150, o caixa deve entregar

uma nota de 100 e uma nota de 50, e não 15 notas de 10. É importante lembrar que ao fazer

este cálculo de quais e quantas serão as notas, o programa deve sempre verificar se existe

quantidade de notas disponíveis de cada valor. Ou seja, se durante a execução

do programa, forem feitos 20 saques sucessivos de 50, então o caixa já entregou

todas as notas de 50 disponíveis, e com isso se o próximo saque for de 150, o

programa deve calcular que o saque será de 1x de 100, 2x de 20 e 1x de 10. Caso

O saque não seja possível, o programa deve informar ao usuário.

Também é necessário verificar antes do cálculo de notas, se o usuário possui

saldo suficiente. Observe que esta é parte mais complexa do programa, ou

seja, calcular quantas e quais as notas que serão entregues, avaliando

sempre o saldo e a quantidade de notas ainda disponíveis no caixa.



Exemplo do que deve aparecer para o usuário quando for digitado a opção 2:



----------------------------------------------------------

Bem vindo ao Banco CI240

----------------------------------------------------------

  Caixa Eletrônico

    [1] Saldo

    [2] Saque

    [3] Depósito

    [4] Extrato

    [5] Sair

  Digite a opção desejada: 2

----------------------------------------------------------

    Digite o valor do saque: 120

----------------------------------------------------------

      Saque efetuado: 1x R$100, 1x R$20

----------------------------------------------------------



----------------------------------------------------------

Bem vindo ao Banco CI240

----------------------------------------------------------

  Caixa Eletrônico

    [1] Saldo

    [2] Saque

    [3] Depósito

    [4] Extrato

    [5] Sair

  Digite a opção desejada: 





Se o valor do saque não for possível de ser realizado, o programa

deve emitir uma mensagem ao usuário, e mostrar

a quantidade de cada uma das notas no caixa, como por exemplo:



----------------------------------------------------------

Bem vindo ao Banco CI240

----------------------------------------------------------

  Caixa Eletrônico

    [1] Saldo

    [2] Saque

    [3] Depósito

    [4] Extrato

    [5] Sair

  Digite a opção desejada: 2

----------------------------------------------------------

    Digite o valor do saque: 125

----------------------------------------------------------

    Valor de saque não disponível

    Notas no caixa: 10x R$100, 5x R$50, 10x R$20 e 5x R$10

----------------------------------------------------------



----------------------------------------------------------

Bem vindo ao Banco CI240

----------------------------------------------------------

  Caixa Eletrônico

    [1] Saldo

    [2] Saque

    [3] Depósito

    [4] Extrato

    [5] Sair

  Digite a opção desejada: 





Outra situação de saque não disponível é quando o usuário não tem saldo 

suficiente para o saque. Neste caso, o programa deve informar ao usuário, como

por exemplo:



----------------------------------------------------------

Bem vindo ao Banco CI240

----------------------------------------------------------

  Caixa Eletrônico

    [1] Saldo

    [2] Saque

    [3] Depósito

    [4] Extrato

    [5] Sair

  Digite a opção desejada: 2

----------------------------------------------------------

    Digite o valor do saque: 12000

----------------------------------------------------------

    Saldo insuficiente para o saque

----------------------------------------------------------



----------------------------------------------------------

Bem vindo ao Banco CI240

----------------------------------------------------------

  Caixa Eletrônico

    [1] Saldo

    [2] Saque

    [3] Depósito

    [4] Extrato

    [5] Sair

  Digite a opção desejada: 





Escolhendo a opção 3 para depósito, o programa deve perguntar qual o valor a

ser depositado, e atualizar o saldo do usuário. Nesta opção pode ser qualquer

valor, inclusive de qualquer nota. Exemplo da execução segue abaixo:



----------------------------------------------------------

Bem vindo ao Banco CI240

----------------------------------------------------------

  Caixa Eletrônico

    [1] Saldo

    [2] Saque

    [3] Depósito

    [4] Extrato

    [5] Sair

  Digite a opção desejada: 3

----------------------------------------------------------

    Digite o valor do deposito: 270

----------------------------------------------------------

      Saldo atualizado: R$ 1150

----------------------------------------------------------



----------------------------------------------------------

Bem vindo ao Banco CI240

----------------------------------------------------------

  Caixa Eletrônico

    [1] Saldo

    [2] Saque

    [3] Depósito

    [4] Extrato

    [5] Sair

  Digite a opção desejada: 





Na opção 4 extrato o programa deve imprimir todas as operações de saque e depósito

realizadas com suas respectivas datas e horários, incluindo os segundos, para

auxiliar a visualização dos dados, além do salto final na conta.

Mostre estas operações em ordem cronológica e de forma organizada para o usuário.

Para isso você pode utilizar o módulo datetime. Você pode usar um arquivo para

armazenar estas informações se preferir. Considere o exemplo abaixo:



----------------------------------------------------------

Bem vindo ao Banco CI240

----------------------------------------------------------

  Caixa Eletrônico

    [1] Saldo

    [2] Saque

    [3] Depósito

    [4] Extrato

    [5] Sair

  Digite a opção desejada: 4

----------------------------------------------------------

    Extrato de operações

----------------------------------------------------------

      30/10/2019  10:20:21     Saldo inicial R$1000    

      30/10/2019  10:22:13     Saque R$120

      30/10/2019  10:23:45     Depósito R$270

      30/10/2019  10:23:45     Saldo atualizado R$1150

----------------------------------------------------------





Você poderá utilizar funções para desenvolver seu programa.

Um exemplo de função é imprimir o menu, outra para imprimir extrato.

Funções para verificar a quantidade de notas, atualizar saldo também podem ser utilizadas.

 

Para sair do programa basta selecionar a opção 5.



----------------------------------------------------------

Bem vindo ao Banco CI240

----------------------------------------------------------

  Caixa Eletrônico

    [1] Saldo

    [2] Saque

    [3] Depósito

    [4] Extrato

    [5] Sair

  Digite a opção desejada: 5

----------------------------------------------------------

    Obrigado por usar o Banco CI240

----------------------------------------------------------

   

A entrega do trabalho deve ser por email para luciano@ufpr.br

O programa a ser enviado deve ser nomeado como caixa_GRR1_GRR2.py,

onde o GRR1 e GRR2 são os números do registro acadêmico da dupla que estará

Entregando o trabalho, por exemplo: caixa_GRR20190443_GRR20192222.py



A data de entrega está disponível na página da disciplina. Além da

entrega na data definida, também é necessário apresentar o trabalho para o 

Professor no laboratório de informática.

