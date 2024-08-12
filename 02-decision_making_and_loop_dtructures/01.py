"""Faça um Programa que peça dois números e imprima o maior deles"""


def check_larger_number():
    try:
        number01 = float(input("Por favor insira o primeiro número: "))
        number02 = float(input("Por favor insira o segundo número: "))
        if number01 > number02:
            print(f"{number01} é o maior valor inserido!")
        elif number01 < number02:
            print(f"{number02} é o maior valor inserido")
        else:
            print("Os valores inseridos são iguais")
    except ValueError as err:
        print(f"Entrada inválida! Detalhes: {err}")


check_larger_number()
