"""Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno."""


def get_user_info():
    try:
        print(
            "Insira os comprimentos dos três lados de um triângulo para classifica-los."
        )
        side01 = float(input("Comprimento do primeiro lado: "))
        side02 = float(input("Comprimento do segunfo lado: "))
        side03 = float(input("Comprimento do terceiro lado: "))
        return side01, side02, side03
    except ValueError as err:
        print(f"Entrada Inválida. Detalhes: {err}")


def classify_triangle():
    side01, side02, side03 = get_user_info()
    if side01 <= 0 or side02 <= 0 or side03 <= 0:
        print("Triângulo inválido!")
    elif side01 == side02 == side03:
        print("Triângulo Equilátero")
    elif side01 == side02 or side02 == side03 or side03 == side01:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")


classify_triangle()
