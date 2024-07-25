#Peça ao usuário para informar o ano de nascimento. Em seguida,calcule e imprima a idade atual
import datetime

def getYearBirth():
    try:
        year = int(input('Digite seu ano de nascimento: '))
        return year
    except ValueError as err:
        print(f'Por favor, insira um valor válido. Detalhes: {err}')

def calculateAge():
    year = getYearBirth()
    currentYear = datetime.datetime.now().year
    print(f'Sua idade é: {currentYear - year} anos')


calculateAge()
    
