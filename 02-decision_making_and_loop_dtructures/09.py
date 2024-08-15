"""O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir
 ue apenas números positivos sejam considerados na contagem e cálculos"""

list_numbers = []


def count_even_odd(list_numbers):
    even_count = 0
    odd_count = 0

    for num in list_numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count


def get_numbers():
    print(
        "Adicione um número à lista de números para checar s números pares e ímpares."
    )
    print("Você poderá adicionar quantos números desejar, um de cada vez.")
    print("Por favor, não adicione à lista números negativos.")
    print("Para finalizar o programa e exibir o resultado, digite 0.")

    while True:
        try:
            number_added = float(input("Insira seu número: "))
            if number_added == 0:
                even, odd = count_even_odd(list_numbers)
                print(f"Quandidade de números pares inseridos: {even}")
                print(f"Quantidade de números ímpares inseridos: {odd}")
                break
            elif number_added > 0:
                list_numbers.append(number_added)
            else:
                print("Número inválido. Adicione apenas números positivos.")
        except ValueError as err:
            print(f"Entrada inválida. Detalhes: {err}")
            break


get_numbers()
