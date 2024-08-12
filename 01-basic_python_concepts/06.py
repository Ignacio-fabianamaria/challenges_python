""" Escreva um programa que calcule o tempo de uma viagem. 
Faça um comparativo do mesmo percurso de avião, carro e ônibus. 
Levando em consideração:
 - avião = 600 km/h
 - carro = 100 km/h
 - ônibus = 80 km/h
"""


def calculate_travel_time():
    distance = get_distance()
    print("Tempo de percurso:")
    travel_by_plane(distance)
    travel_by_car(distance)
    travel_by_bus(distance)


def get_distance():
    try:
        distance = float(input(f"Insira a distância do seu trajeto em quilômetros: "))
        return distance
    except ValueError as err:
        print(f"O valor inserido deve ser um número. Detalhes: {err}")


def travel_by_plane(distance):
    time_hours = distance / 600  # obtendo o tempo total
    hours, rest = divmod(
        time_hours * 3600, 3600
    )  # Obtendo as horas e segundos restantes
    min, sec = divmod(rest, 60)  # Converte os segundos restantes para min e segundos
    print(f"Avião: {int(hours)} horas, {int(min)} minutos e {int(sec)} segundos")


def travel_by_car(distance):
    time_hours = distance / 100  # obtendo o tempo total
    hours, rest = divmod(
        time_hours * 3600, 3600
    )  # Obtendo as horas e segundos restantes
    min, sec = divmod(
        rest, 60
    )  # Obtendo minutos e segundos com o valor remanescente do calculo anterior
    print(f"Carro: {int(hours)} horas, {int(min)} minutos e {int(sec)} segundos")


def travel_by_bus(distance):
    time_hours = distance / 80  # obtendo o tempo total
    hours, rest = divmod(
        time_hours * 3600, 3600
    )  # Obtendo as horas e segundos restantes
    min, sec = divmod(
        rest, 60
    )  # Obtendo minutos e segundos com o valor remanescente do calculo anterior
    print(f"Ônibus: {int(hours)} horas, {int(min)} minutos e {int(sec)} segundos")


calculate_travel_time()

""" A função divmod é uma função embutida em Python que realiza a divisão e
retorna tanto o quociente quanto o resto da divisão em uma única operaçã 
ex: 
quotient, remainder = divmod(10, 3)
print(quotient)   # Saída: 3
print(remainder)  # Saída: 1
---> Aqui, 10 dividido por 3 é 3, com um resto de 1.

https://www.w3schools.com/python/ref_func_divmod.asp
"""
