'''
Medidor de velocidade.

A velocidade permitida da via é de 80km. Crie um programa que recebe a velocidade do usuario e informe se ele nao levou uma multa, levou uma multa leve, levou uma multa grave ou levou uma multa gravissima.

nao levou multa: dentro da velocidade permitida;
multa leve: ate 10km acima da velocidade permitida;
multa grave: 11 a 20km acima da velocidade permitida;
multa gravissima: acima de 20km da velocidade permitida.

Método 5Q's:
1. Quais são os dados de entrada necessários?
Velocidade do veiculo
2. O que devo fazer com estes dados?
Verificar o grau da multa baseado na velocidade recebida
3. Quais são as restrições deste problema?

4. Qual é o resultado esperado?
Receber a velocidade do veiculo e informar se nao recebeu multa, recebeu uma multa leve, grave ou gravissima.
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
input velocidade
if velocidade <= 80:
    print nao recebeu multa
if velocidade > 80 and <= 90:
    print multa leve
if velocidade > 90 and <=100:
    print multa grave
if velocidade > 100:
    print multa gravissima
'''
velocidade_maxima = 80
velocidade = int(input('Velocidade do veiculo: '))
if velocidade <= velocidade_maxima:
    print('Nao recebeu multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('Multa leve')
elif velocidade > velocidade_maxima + 10 and velocidade <= velocidade_maxima + 20:
    print('Multa grave')
elif velocidade > velocidade_maxima + 20:
    print('Multa gravissima')
