'''
Crie um programa que recebe um número e imprime o fatorial daquel número

# Método 5Q's:

Analise criticamente o problema;
Explicar em voz alta.

1. Quais são os dados de entrada necessários?
- Numero com o qual o programa deve calcular o fatorial
2. O que devo fazer com estes dados?
- Calcular o fatorial do numero digitado e imprimir na tela
3. Quais são as restrições deste problema?
- O número precisa ser inteiro e positivo.
4. Qual é o resultado esperado?
- O programa ira receber um número, calcular seu fatorial e imprimir na tela.
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?

input numero inteiro
if numero < 0:
    print "digite apenas números positivos"
else:
    fatorial = 1
    loop de 1 a numero
        fatorial = fatorial * numero
    print fatorial
'''
numero = int(input('Digite um numero para calcular seu fatorial: '))
if numero < 0:
    print("Digite apenas números inteiros.")
else:
    fatorial = 1
    for numero_atual in range(1, numero + 1):
        fatorial = fatorial * numero_atual
    print(fatorial)
