'''
Escreva um programa que, ao iniciar, gera um valor aleatório de 1 a 10 e permite que o usuário chute um número, até que o valor aleatório gerado, no início do programa, seja chutado corretamente.

O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.

Método 5Q's:
Quais são os dados de entrada necessários?
Numero aleatorio
O que devo fazer com estes dados?
Solicitar um chute ao usuario e compar com o valor gerado.
Quais são as restrições deste problema?
Deve ser um numero de 1 a 10
Qual é o resultado esperado?
O programa deve gerar um numero aleatorio e solicitar chute ao usuario. O programa deve informar se o chute foi acima, abaixo ou igual ao valor aleatório gerado no início do programa.
Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
input numero_aleatorio
chute = 0
while chute <> numero_aleatorio:
    input chute de 1 a 10
    if chute > numero_aleatorio:
        print 'O numero aleatório é menor do que o número chutado'
    if chute < numero_aleatorio:
        print 'O numero aleatório é maior do que o número chutado'
    if chute == numero_aleatorio:
        print 'Você acertou!'
'''
from random import randint

numero_aleatorio = randint(1, 10)
acertou = False
while not acertou:
    chute = int(input('Chute um número de 1 a 10: '))
    if chute > numero_aleatorio:
        print('Seu chute foi maior do que o número aleatório')
    elif chute < numero_aleatorio:
        print('Seu chute foi menor do que o número aleatório')
    elif chute == numero_aleatorio:
        print('Você acertou!')
        acertou = True
