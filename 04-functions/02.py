"""Reverso do número. Faça uma função que retorne o reverso de um
número inteiro informado. Por exemplo: 127 -> 721"""

import random


def reverse_number():
    num = random.randint(10, 1000)
    reverse = str(num)[::-1]
    print(f'Número atual: {num}\nReverso do número: {reverse}')


reverse_number()