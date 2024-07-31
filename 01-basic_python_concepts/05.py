'''Escreva um programa que calcule o salário líquido. 
Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
- Renda até R$ 1.903,98: isento de imposto de renda;
- Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
- Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
- Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
- Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
'''

def get_gross_salary():
    try:
        gross_salary = float(input(f'Insira seu salário bruto em reais (ex: 2000.50): '))
        return gross_salary
    except ValueError as err:
        print(f'Os valores inseridos devem ser apenas números e não utilizar (,). \n Detalhes: {err}')

def  calculate_net_salary():
    gross_salary = get_gross_salary()
    if gross_salary <= 1903.98:
        print(f'Renda até R$ 1.903,98 é isento de imposto de renda')
    elif gross_salary <= 2826.65 and gross_salary >= 1903.99:
        print(f'Para sua renda bruta a alíquota é 7,5%. Seu salário líquido é R$: {(gross_salary - (gross_salary * 0.075)):.2f}')
    elif gross_salary <= 3751.05 and gross_salary >= 2826.66:
        print(f'Para sua renda bruta a alíquota é 15%. Seu salário líquido é R$: {(gross_salary - (gross_salary * 0.15)):.2f}')
    elif gross_salary <= 4664.68 and gross_salary >= 3751.06:
        print(f'Para sua renda bruta a alíquota é 22.5%. Seu salário líquido é R$: {(gross_salary - (gross_salary * 0.225)):.2f}')    
    else:
        print(f'Para sua renda bruta acima de R$ 4.664,68: alíquota máxima de 27,5%. Seu salário líquido é R$: {(gross_salary - (gross_salary * 0.275)):.2f}')    

calculate_net_salary()