# forçar a saída do terminal para UTF-8

import sys
sys.stdout.reconfigure(encoding='utf-8')

# nome = 'duda'
# print(nome)

# -------------- VARIÁVEIS PRIMITIVAS --------------

idade = 20 # (int) números inteiros
peso = 70.4 # (float) números decimais
nome = 'Duda' # (str) caracteres
ativo = True # (bool) valores lógicos
resultado = None # (NoneType) ausência de valor

# -------------- VALIDANDO OS TIPOS DE VARIÁVEIS --------------

# imprime somente o "VALOR" das variáveis

print(idade)
print(peso)
print(nome)
print(ativo)
print(resultado) 

# imprime somente a CLASSE / TIPO das variáveis

print(type(idade))
print(type(peso))
print(type(nome))
print(type(ativo))
print(type(nome))

# -------------- CONCATENANDO NO PRINT --------------

# "Meu nome é Duda e tenho 20 anos de idade":

print('Meu nome é', nome, 'e tenho', idade, 'anos de idade.')

# -------------- CÁLCULOS COM NÚMEROS -------------

num1 = 10
num2 = 3

resultado = num1 + num2

# imprime apenas o "VALOR" da variável RESULTADO

print(resultado)

# faz contas diretas no PRINT

print(10 + 10)
print(10 - 5)
print(10 * 5)
print(10 / 5)

# imprime apenas os "VALORES" das variáveis

print(num1)
print(num2)


resultado = num1 // num2 # retorna apenas a parte INTEIRA, no caso "3"

resultado = num1 % num2 # retorna apenas o RESTO da divisão, no caso "1": 10 / 3 = 3 * 3 = 9; 10 - 9 =1

# -------------- SOMA NO PYTHON -------------

alunosPresentes = 23
alunosAusentes = 17

totalAlunos = alunosPresentes + alunosAusentes

print(totalAlunos)

# -------------- OPERADOR DE ATRIBUIÇÃO AUMENTADA -------------

produto1 = 10
produto1 += 3 # operador de atribuição aumentada SOMA
produto1 -= 3 # operador de atribuição aumentada SUBTRAÇÃO
produto1 *= 3 # operador de atribuição aumentada MULTIPLICAÇÃO
produto1 /= 3 # operador de atribuição aumentada DIVISÃO
produto1 **= 3 # operador de atribuição aumentada POTÊNCIA

resultado = produto1 # + 3

print(resultado)

# -------------- FUNÇÕES BÁSICAS PARA NÚMEROS (FACILITA, POIS CRIA-SE MENOS VARIÁVEIS) -------------

# quero imprimir somente o INTEIRO, ou seja, o "3"

num3 = 3.1425 # <=4 = para baixo
num4 = 3.4425 # <=4 = para baixo
num5 = 3.5425 # >=5 = para cima
num6 = 3.7425 # >=5 = para cima


# print(num3)
print(round(num3)) # "puxar" ou arrendondar para o número inteiro / <=4 = para baixo / >=5 = para cima
print(round(num4))
print(round(num5))
print(round(num6))

# quero imprimir o INTEIRO e uma, duas, três.. casas decimais
# o número depois da vírgula e do espaço é a "ordem" das casas decimais

print(round(num3, 1)) # imprime  3.1
print(round(num3, 2)) # imprime  3.14
print(round(num3, 3)) # imprime  3.142
print(round(num3, 3)) # imprime  3.1425

# POTÊNCIA

#num7 = 2 * 2 * 2
# print(num7)

print(pow(2, 3)) # ou seja, 2 elevado a 3

# MÍNIMO E MÁXIMO

print(max(1, 4, 90, 2, 17,3)) # retorna o MAIOR entre a sequência de números, no caso o "90"

print(min(1, 4, 90, 2, 17,3)) # retorna o MENOR entre a sequência de números, no caso o "1"

# SOMA

print(sum([1, 3, 7])) # soma os números dentro dos colchetes, no caso "11"
