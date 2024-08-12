""" Criar um programa em Python que solicite três números ao usuário, utilize
estruturas condicionais para determinar o maior entre eles e apresente o
resultado."""


def get_numbers():
    try:
        num01 = int(input("Insira o primeiro número: "))
        num02 = int(input("Insira o segundo número: "))
        num03 = int(input("Insira o terceiro número: "))
        return num01, num02, num03
    except ValueError as err:
        print(f"Por favor, insira um valor válido. Detalhes: {err}")


def max_of_three_numbers():
    num01, num02, num03 = get_numbers()
    if num02 < num01 > num03:
        print(f"Dentre os números inseridos, o nº {num01} é o maior entre eles")
    elif num01 < num02 > num03:
        print(f"Dentre os números inseridos, o nº {num02} é o maior entre eles")
    else:
        print(f"Dentre os números inseridos, o nº {num03} é o maior entre eles")


max_of_three_numbers()
