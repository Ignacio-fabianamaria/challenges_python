# Faça um Programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros.


def kilometers_to_m_cm_mm():
    km = get_km()
    km_to_m(km)
    km_to_cm(km)
    km_to_mm(km)


def get_km():
    try:
        return float(input("Insira um valor em quilômetros: "))
    except ValueError as err:
        print(f"Os valores inseridos devem ser números. \n Detalhes: {err}")


def km_to_m(km):
    print(f"{km} km é igual a {km * 1000} metros")


def km_to_cm(km):
    print(f"{km} km é igual a {km * 100000} centímetros")


def km_to_mm(km):
    print(f"{km} km é igual a {km * 1000000} milímetros")


kilometers_to_m_cm_mm()
