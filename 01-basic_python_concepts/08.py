""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês. """


def collect_payment_info():
    try:
        hourly_pay = float(input("Insira quanto você ganha por hora: "))
        hours_worked = float(input("Insira o total de hs trabalhadas por mês: "))
        if (hourly_pay or hours_worked) == 0:
            print("Por favor, insira um valor maior que zero")
        else:
            return hourly_pay, hours_worked

    except ValueError as err:
        print(f"Por favor, insira um valor válido! Detalhes: {err}")


def salary_calculation():
    hourly_pay, hours_worked = collect_payment_info()
    print(f"Seu salário mensal é R$: {(hourly_pay * hours_worked):.2f}")


salary_calculation()
