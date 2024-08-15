"""Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime.**
   
   As perguntas são:
   - "Telefonou para a vítima?"
   - "Esteve no local do crime?"
   - "Mora perto da vítima?"
   - "Devia para a vítima?"
   - "Já trabalhou com a vítima?"

   O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
   - Se a pessoa responder positivamente a 2 questões, ela deve ser classificada como "Suspeita".
   - Entre 3 e 4 como "Cúmplice".
   - E 5 como "Assassino".
   - Caso contrário, ela será classificada como "Inocente".
"""


def investigate_crime_suspect():
    questions_list = [
        "Telefonou para a vítima? ",
        "Esteve no local do crime? ",
        "Mora perto da vítima? ",
        "Devia para a vítima? ",
        "Já trabalhou com a vítima? "
    ]
    positive_responses = 0

    print('Precisamos fazer umas perguntas sobre o crime ocorrido.\nPor favor, nos forneça apenas resposta com "sim" ou "não".\n')

    for question in questions_list:
        while True:
            try:
                response = input(question).strip().lower()
                if response == 'sim':
                    positive_responses += 1
                    break
                elif response in ['não', 'nao']:
                    break
                else:
                    print('Resposta inválida. Por favor, responda apenas "sim" ou "não"')
            except ValueError as err:
                print(f'Entrada inválida. Detalhes: {err}')

    if positive_responses == 2:
        classification = "🤔 Suspeita"
    elif 3 <= positive_responses <= 4:
        classification = "🕵️‍♂️ Cúmplice"
    elif positive_responses == 5:
        classification = "🩸 Assassino"
    else:
        classification = "😇 Inocente"

    print(f"\nClassificação: {classification}")


investigate_crime_suspect()