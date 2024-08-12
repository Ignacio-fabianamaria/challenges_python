""" Faça um Programa que utilize 4 variáveis como preferir
e no final print uma mensagem amigável utilizando as variáveis criadas.
"""


def get_user_info():
    try:
        name = input("Insira seu nome: ").capitalize()
        age = input("Insira sua idade: ")
        place = input("Insira o nome da cidade que você mora: ").capitalize()
        job = input("Insira sua profissão: ").capitalize()
        return name, age, place, job
    except ValueError as err:
        print("Por favor, insira um valor válido. Detalhes: {err}")


def greeting_generator():
    name, age, place, job = get_user_info()
    print(
        f"Olá, {name}! É um prazer te conhecer. Você tem {age} anos e trabalha como {job}, que interessante!. "
        f"Espero que você esteja gostando de viver em {place}. Tenha um ótimo dia!"
    )


greeting_generator()
