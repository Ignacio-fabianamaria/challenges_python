""" Implemente um programa que classifique um aluno com base em sua pontuação em um exame.
O programa deverá solicitar uma nota de 0 a 10. Se a pontuação for maior ou igual a 7,
o aluno é aprovado; caso contrário, é reprovado."""


def classify_student():
    try:
        while True:
            student_score = float(
                input(
                    "Por favor insira sua pontuação para verificar seu status no exame. \n"
                    "O valor inserido dever ser entre 0 a 10\n"
                )
            )
            if 11 > student_score >= 7:
                print(
                    f"Parabéns, você está APROVADO!\nPontuação alcançada: {student_score}"
                )
                break
            elif 0 <= student_score < 7:
                print(
                    f"Pontuação alcançada de {student_score} é insucifiente para aprovação.\nREPROVADO!"
                )
                break
            else:
                print("🚫 Entrada inválida")
    except ValueError as err:
        print(f"Entrada inválida. Por favor, insira um número. Detalhes: {err}")


classify_student()
