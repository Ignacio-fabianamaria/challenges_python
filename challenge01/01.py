# Faça um Programa que peça dois números, realize as principais operações soma, subtração, multiplicação, divisão


def calculator():
    num1, num2 = parameters()
    add(num1, num2)
    subtract(num1, num2)
    multiply(num1, num2)
    divide(num1, num2)

def parameters():
    try:
       num1 = float(input('Digite um número: '))
       num2 = float(input('Digite outro número: '))
       return num1, num2 
    except ValueError as err:
        print(f'Os valores inseridos devem ser números. \n Detalhes: {err}')
       

def add(num1, num2):
    print(f"Soma: {num1 + num2}")

def subtract(num1, num2):
    print(f"Subtração: {num1 - num2}")

def multiply(num1, num2):
    print(f"Multiplicação: {num1 * num2}")

def divide(num1, num2):
    try:
        print(f"Divisão: {num1 / num2}")
    except ZeroDivisionError:
        print("Não é possível dividir um valor por zero")           

calculator()      