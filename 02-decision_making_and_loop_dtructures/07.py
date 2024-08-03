''' **Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.**'''

def get_user_age():
    while True:
        try:
            user_age = int(input('Por favor, insira sua idade: '))
            if user_age < 0:
                print('Entrada inválida, por favor não insira valores negativos')
            else:
                return user_age    
        except ValueError as err:
            print(f'Entrada inválida. Detalhes {err}')


def check_user_age():
    user_age = get_user_age()
    if 0 <= user_age <= 11:
        print(f'Sua idade é {user_age} anos. Status: CRIANÇA')
    elif 12<= user_age <=17:
        print(f'Sua idade é {user_age} anos. Status: ADOLESCENTE')
    elif 18<= user_age <=59:
        print(f'Sua idade é {user_age} anos. Status: ADULTO')
    elif 60<= user_age <=125:
        print(f'Sua idade é {user_age} anos. Status: IDOSO')
    else:
        print(f'Idade {user_age} inválida! Por favor insira uma idade até 130 anos')    


check_user_age()
    
    




