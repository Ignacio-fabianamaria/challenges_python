"""Crie um dicionário representando um carrinho de compras. 
Adicione produtos (chaves) e quantidades (valores) ao carrinho.
Calcule o total do carrinho de compra."""

def grocery_cart():
    my_cart = {}
    print('Meu Carrinho 🛒\n')
    while True:
        try:
            user_input = input('01 - Adicionar itens.\n02 - Sair\n').capitalize()
            if user_input in ('02', '2', 'Sair'):
                print(f'Total de itens no carrinho de compras: {sum(my_cart.values())}')
                break
            elif user_input in ('01', '1', 'Adicionar itens'):
                product_name = input('Inserir produtos: ').capitalize()
                product_quantity = float(input('Inserir quantidade: '))
                my_cart[product_name] = product_quantity
                print(f'Carrinho atualizado: {my_cart}')
        except ValueError as err:
            print(f'Entrada inválida. Detalhes: {err}')


                
grocery_cart()
  