''' Solicite ao usuário o peso em kg e a altura em metros.
Calcule e imprima o Índice de Massa Corporal (IMC) usando a fórmula: IMC = peso / (altura x altura).'''

def get_weight_height():
    try:
        weight = float(input('Insira seu peso em quilogramas: '))
        height = float(input('Insira sua altura em metros: '))
        return weight, height
    except ValueError as err:
        print(f'Insira um valor válido. Detalhes: {err}')
        return None, None

def calc_imc():
    weight, height = get_weight_height()
    imc = weight / (height * height)
    if imc < 18.5:
        print(f'Seu imc foi {imc:.2f}. 🚨 Você está abaixo do seu peso ideal 🚨')
    elif 18.5 <= imc <= 24.9:
        print(f'Seu imc foi {imc:.2f}. 🌟 Você está ano seu peso ideal. Parabéns 🌟')
    elif 25 <= imc <= 30:
        print(f'Seu imc foi {imc:.2f}. 🚨  Atenção! Você está em sobrepeso. 🚨 ')
    else:
        print(f'Seu imc foi {imc:.2f}. 🚨🚨 Atenção! Você já está no quadro de obesidade. 🚨🚨')

calc_imc()                  

