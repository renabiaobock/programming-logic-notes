# Curso Lógica de Programação Completo 2024 [Iniciantes] + Desafios + Muita prática
URL: https://www.youtube.com/watch?v=iF2MdbrTiBM&ab_channel=DevAprender%7CJhonatandeSouza


## Aula 01 - Por que um software é criado?

1. Para criar soluções para probemas do dia a dia. ex: Netflix, Google.
2. Automação e otimização de processos. ex: postes de luz que se ligam/desligam automaticamente.


## Aula 02 - Como um software é criado do zero e onde a lógica se encaixa nisso?

* Ciclo de desenvolvimento de software:
    * Estagio 1 - Idealização;
    * Estágio 2 - Especificação de Requisitos;
    * Estágio 3 - Validação da Solução;
    * Estágio 4 - Desenvolvimento e Testes;
    * Estágio 5 - Implantação e Entrega.


## Aula 03 - O problema que todo iniciante enfrenta.

1. escrever codigo lentamente;
2. resolver os mesmos problemas em situaçãoes diferentes;
3. se achar incapaz/insuficiente;
4. gradualmente conseguir solucionar problemas mais facilmente.


## Aula 04 - Aprender resolver problemas através da análise crítica.

> "Saber analisar e resolver um problema é mais importante que decorar os comandos de uma linguagem de programação!"

> "Quanto mais experiente se tornar, mais óbvio ficam os caminhos que levam a uma solução"

### Problema 01:

* Problema: Como chegar a medida de exatamente 2ml, sendo que só temos um pote de 5ml e de 3ml:
* Solução: Primeiro enchemos o pote de 5ml, depois despejamos o conteudo dele no pote de 3ml, restara exatamente 2ml no pote de 5ml.

### Problema 02:

* Problema: Como calular o salario hora de um funcionario, partindo do seu salario mensal e do total de horas trabalhados no mês.
* Solução:
    1. perguntar o salário do mês e armazenar a informação;
    2. perguntar a quantidade de horas trabalhadas no mês e armazenar a informação;
    3. dividir o salário do mês pela quantidade de horas trabalhadas.


## Aula 05 -  O que sao algoritmos e como montar algoritmos do zero

### 1. O que são algoritmos?
Um algorimo é simplesmente uma série de instruções a serem seguidas, para resolver um problema

### 2. Quando algoritmos devem ser criados?
Sempre que queremos montar uma sequência de passos necessários para solucionar um problema

### 3. Qual é a estratégia para montar um algorítmo?
#### Método 5Q's:
1. Quais são os dados de entrada necessários?
2. O que devo fazer com estes dados?
3. Quais são as restrições deste problema?
4. Qual é o resultado esperado?
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?


## Aula 06 - 4 conceitos obrigatórios para ser capaz de resolver problemas.

1. Variáveis;
2. Condicionais;
3. Laços de repetição;
4. Coleções.


## Aula 07 - Criando soluções em Pseudocódigo do básico ao avançado

### Exemplo 1 - Pseudocódigo (com uso de variáveis) - Valor por hora

Crie um programa que retorne o valor hora de um funcionário com base no seu salário mensal e horas trabalhadas por mês.

1. Quais são os dados de entrada necessários?
* salário do mês
* horas trabalhadas no mês
2. O que devo fazer com estes dados?
* devo utilizar estes dados para calcular o valor hora que o funcionario recebe
3. Quais são as restrições deste problema?
* os valores devem ser entregues somente no formato de salário por hora
4. Qual é o resultado esperado?
* o valor hora que um funcionário recebe
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
```
salario_do_mes = input float
horas_trabalhadas_no_mes = input int
valor_hora = salario_do_mes / horas_trabalhadas_no_mes
print valor_hora
```

### Exemplo 2 - Exibir o maior dos dois números

1. Quais são os dados de entrada necessários?
* primeiro número
* segundo número
2. O que devo fazer com estes dados?
* comparar os dois números para exibir qual é o maior 
3. Quais são as restrições deste problema?
* é possivel comparar apenas números
* preciso possuir dois números para que a comparação seja realizada
4. Qual é o resultado esperado?
* retornar qual é o maior dos dois números para o usuário
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
```
input primeiro_numero
input segundo_numero
if primeiro_numero > segundo_numero
    print "o primeiro valor é maior"
elif segundo_numero > primeiro_numero
    print "o segundo valor é maior"
else
    print "os números são iguais"
```

### Exemplo 3 - Fatorial de um número

1. Quais são os dados de entrada necessários?
* número
2. O que devo fazer com estes dados?
* após receber um número devo o multiplicar por todos os seus antecessores e exibir o resultado
3. Quais são as restrições deste problema?
* deve ser um número inteiro e positivo
4. Qual é o resultado esperado?
* é esperado que o fatorial do número recebido seja exibido
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
```
input numero
if numero < 0:
    print "digite apenas números positivos"
fatorial = 1
loop de 1 a numero
    fatorial = fatorial * numero
print fatorial
```

### Exemplo 4 - Some os valores de uma lista
1. Quais são os dados de entrada necessários?
* lista com os valores a serem somados
2. O que devo fazer com estes dados?
* somar cada numero ao numero anterior ate somar todos os numeros da lista
3. Quais são as restrições deste problema?
* apenas os valores da lista devem ser adicionados
4. Qual é o resultado esperado?
* é esperado que o valor total da soma dos numeros da lista seja exibido
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
```
input lista
total = 0
loop numero in lista:
    total = total + numero
print soma
```

### Exemplo 5 - Chute o número
1. Quais são os dados de entrada necessários?
* numero aleatorio
2. O que devo fazer com estes dados?
* comparar ao numero da tentativa do usuario e informar se acertou ou nao
3. Quais são as restrições deste problema?
* as tentativas devem ser de numeros entre 1 e 10
4. Qual é o resultado esperado?
* apos cada tentativa, deve ser exibido na tela uma das seguintes mensagens: "O chute é maior que o valor gerado", "O chute é menor que o valor gerado", "Acertou!"
5. Qual é a sequência de passos a ser feita para chegar ao resultado esperado?
```
input valor_aleatorio
acertou = false
while acertou = false
    input chute
    if chute = valor_aleatorio
        print "Acertou!"
        acertou = true
    if chute > valor_aleatorio
        "O chute é maior que o valor gerado"
    if chute < valor_aleatorio
        "O chute é menor que o valor gerado"
    else
        "Você chutou um valor invalido"
```


## Aula 08 - Criando soluções com fluxogramas

Fluxogramas são uma representação visual gráfica de um algorítmo.

![Legenda Fluxogramas](legenda_fluxogramas.png)


## Aula 09 - Seu primeiro programa em Python

1. Exemplo de variáveis na prática com python (aula1.py)
2. Exemplo de condicionais na prática com python (aula2.py)
3. Exemplo de coleções na prática com python (aula3.py)
4. Exemplo de laços de repetição na prática com python (aula4.py)
