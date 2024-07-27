'''Faça um programa que permita ao usuário digitar o seu nome e
em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. Dica: lembre−se que ao
informar o nome o usuário pode digitar letras maiúsculas ou
minúsculas.'''


def get_username():
    try:
        while True:
            username = input('Por favor, insira seu primeiro nome: ').upper()
            if len(username) < 2:
                print('Por favor, insira um nome com pelo menos 2 caracteres:')
            else:
                return username
    except ValueError as err:
        print(f'Por favor, insira um valor válido: Detalhes: {err}')


def reversed_username():
    username = get_username()
    username_list = list(username)
    reversed = ''.join(username_list[::-1])

    print(f'O seu nome de trás para frente ficou : {reversed}')


reversed_username()
