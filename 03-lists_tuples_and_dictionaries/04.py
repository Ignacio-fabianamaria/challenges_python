"""Crie um dicionário representando contatos (nome, telefone).
Permita ao usuário procurar por um contato pelo nome."""

contacts = {
    "Ana Souza": "11 91234-5678",
    "Carlos Oliveira": "21 92345-6789",
    "Fernanda Lima": "31 93456-7890",
    "Lucas Santos": "41 94567-8901",
    "Mariana Costa": "51 95678-9012",
}


def format_phone_number(phone_number):
    phone_number = "".join(filter(str.isdigit, phone_number))
    if len(phone_number) == 11:
        formatted_phone_number = (
            f"{phone_number[:2]} {phone_number[2:7]}-{phone_number[7:]}"
        )
        return formatted_phone_number
    else:
        print("Número de telefone inserido inválido.")


def contact_list():
    print("📞 Bem vindo à sua lista de contatos. 📞\n")
    while True:
        try:
            print(
                "   O que você deseja fazer?\n   🔍 Pesquisar contato digite 1\n   ➕ Inserir contato digite 2\n   👁Ver lista digite 3\n   ❌ Sair digite 0"
            )
            user_option = int(input("\nInsira sua opção: "))
            if user_option not in (0, 1, 2, 3):
                print("Erro. Opção inválida")
            elif user_option == 1:
                search_contact = input(
                    "Insira o nome do contato que deseja pesquisar: "
                ).title()
                if search_contact in contacts:
                    print(
                        f"O telefone do contato {search_contact} é : {contacts[search_contact]}"
                    )
                    break
                else:
                    print(f"Contato {search_contact} não encontrado.")
            elif user_option == 2:
                name = input("Insira o nome do novo contato: ").title()
                phone = format_phone_number(
                    input("Insira o telefone com DDD do novo contato: ")
                )
                contacts[name] = phone
                print(
                    f"Novo contato adicionado à s lista.\nDetalhes: Nome: {name}, telefone: {phone}"
                )
                break
            elif user_option == 3:
                print(contacts)
                break
            else:
                break
        except ValueError as err:
            print(f"Entrada inválida. Detalhes: {err}")


contact_list()
