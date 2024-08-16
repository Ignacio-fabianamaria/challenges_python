"""Faça um programa, com uma função que necessite de três argumentos,
e que forneça a soma desses três argumentos"""

import random

args = random.sample(range(100), k = 3)

def sum_args(a, b, c):
   print(f'Argumentos: {a}, {b}, {c}')
   print(f'Soma dos argumento: {a + b + c}')

sum_args(*args)


"""
random.sample(): Essa é uma função do módulo random em Python.
Ela retorna uma lista contendo um número especificado (k) de elementos
aleatórios de uma sequência.

range() em Python é uma função que gera uma sequência de números.
Essa sequência é definida por um intervalo que for inserido.
para range(100) o intervalo sera de 0 até 99.
"""