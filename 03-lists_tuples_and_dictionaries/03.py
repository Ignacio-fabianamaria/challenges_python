"""Faça um Programa que peça as quatro notas de 5 alunos, 
calcule e armazene numa lista a média de cada aluno,
e imprima o número de alunos com média maior ou igual a 7.0."""


def student_grade():
    grade_list = []
    num_student = 5
    current_student = 0
    while current_student < num_student:
        try:
            student_grade_input = (input('Por favor, insira as quatro notas do aluno separadas por virgula. ')).strip().split(' ')       
            if len(student_grade_input) != 4:
                print("Erro! Por favor, insira somente 4 notas separadas por espaço. ")
            else:
                student_grade_list = [float(grade.replace(',', '.')) for grade in student_grade_input]
                student_average = (sum(student_grade_list) / len(student_grade_list))
                grade_list.append(student_average)
                current_student += 1
                print(f'Notas do aluno: {student_grade_list} Média do aluno: {student_average}')
        except ValueError as err:
            print(f'Entrada inválida. Detalhes: {err}')
    return grade_list

def average():
    grade_list = student_grade()
    result = sum(1 for grade in grade_list if grade >= 7)
    print(f'O número de alunos com média maior ou igual a 7.0 foi : {result}')


average()