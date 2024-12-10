# Problema 1 - Valor por hora
# Escreva um programa que retorna o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

salario_mensal = float(input('Salário Mensal: '))
horas_trabalhadas = int(input('Horas trabalhadas no mês: '))
valor_hora = salario_mensal / horas_trabalhadas
print(valor_hora)
