# Condicionais
# if, elif, else

'''
Eu cheguei atrasado na aula, ainda posso entrar?
Se essa não for sua terceira vez chegando atrasado, então pode sim, caso contrário irá tomar uma suspensão.
'''

numero_de_atrasos = 2
if numero_de_atrasos >= 3:
    print("Você está suspenso!")
elif numero_de_atrasos == 1:
    print("Pode entrar, porém caso tome mais duas faltas, irá ser suspenso")
    numero_de_atrasos += 1
elif numero_de_atrasos == 2:
    print("Pode entrar, porém caso tome mais uma falta, irá ser suspenso")
    numero_de_atrasos += 1
else:
    print("Pode entrar")


# Encontre o maior valor entre dois números

primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))
if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior')
elif segundo_valor > primeiro_valor:
    print('O segundo valor é maior')
else:
    print('Os números são iguais')
