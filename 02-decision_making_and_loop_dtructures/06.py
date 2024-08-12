"""**Crie um programa que solicite ao usuário um login e uma senha.
O programa deve permitir o acesso apenas se o usuário for "admin" e a senha for "admin123",
caso contrário imprima uma mensagem de erro.**"""

username = "admin"
password = "admin123"


def login():
    while True:
        try:
            username_entered = input("Usuário: ").lower()
            password_entered = input("Senha: ")
            if username_entered == username and password_entered == password:
                print("Login Efetuado com sucesso!")
                break
            else:
                print("🚫 Usuário ou senha incorretos!")
        except ValueError as err:
            print(f"Usuário ou senha incorretos! Detalhes: {err}")


login()
