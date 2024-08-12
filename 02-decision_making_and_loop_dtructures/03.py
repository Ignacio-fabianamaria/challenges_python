""" Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.**"""


def request_grade():
    while True:
        try:
            grade = float(input("Por favor insira uma nota com o valor entra 0 e 10: "))
            if 0 <= grade <= 10:
                print(f"Sua nota inserida foi : {grade}")
                break
            else:
                ("Por favor, informe um valor válido entra 0 e 10")
        except ValueError as err:
            print(f"Entrada inválida. Por favor, insira um número. Detalhes: {err} ")


request_grade()
