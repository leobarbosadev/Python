# Curso de Desenvolvimento de Sistemas
# Turma 0152
# Autor: Leonardo Barbosa
# Data: 24/04/2024
# Objetivo: Verificando um valor decimal

import os


os.system('cls')

print('-' * 70)
print('Estudo de Condicional: Parte 1')
print('=' * 70)

# Entrada
valor = float(input('Digite um número: '))
resposta = ''

# Condicional
if valor % 2 == 0:
    resposta = f'Entrada incorreta, o valor {int(valor)} é um inteiro!'
else:
    resposta = f'Entrada correta, o valor {valor} é um decimail!'

# Saída
print('=' * 70)
print(resposta)

print('Fim do programa!\n') # \n salta uma linha