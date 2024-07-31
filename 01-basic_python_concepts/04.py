'''Faça um Programa que receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. 
Calcule e imprima o consumo médio em km/l.'''

def get_liters_and_distance():
    try:
        liters = float(input(f'Insira a quantidade de litros de combustível consumidos: '))
        distance = float(input(f'Insira a distância percorrida em km: '))
        return liters, distance
    except ValueError as err:
        print(f'Os valores inseridos devem ser números. \n Detalhes: {err}')    

def average_consumption():
    liters, distance = get_liters_and_distance()
    print(f'Para a distância percorrida de {distance}km, {liters}l de combustível foram consumidos.\n Portanto, o consumo médio foi de : {(distance / liters):.1f}km/l')    

average_consumption()       