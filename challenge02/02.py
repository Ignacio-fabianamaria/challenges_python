''' Faça um Programa que pergunte em que turno você estuda. 
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.**'''

def get_study_shift():
    study_shift = input('Por favor insira o seu turno de estudo conforme as opções abaixo:\n'
                        'M - Matutino\n'
                        'V - Vespertino\n'
                        'N - Noturno\n').upper().strip()
    if(study_shift == 'M'):
        print('Bom Dia!')
    elif(study_shift == 'V'):
        print('Boa Tarde!')
    elif(study_shift == 'N'):
        print('Boa Noite!')
    else:
        print('Valor inválido')        


get_study_shift()