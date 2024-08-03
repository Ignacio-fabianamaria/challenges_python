'''Faça um programa que lê três números inteiros e os mostra em ordem crescente.'''

def order_three_numbers():
    while True:
        try:
            print('Insira 3 números inteiros para serem ordenados:')
            num01 = int(input('Insira o primeiro número: '))
            num02 = int(input('Insira o segundo número: '))
            num03 = int(input('Insira o terceiro número: '))
            numbers = [num01, num02, num03]
            numbers.sort()
            print(f'Numeros: {numbers}')
            break
        except ValueError as err:
            print(f'Por favor, insira somento números inteiros! Detalhes: {err}')



order_three_numbers()