import time

class Car:
    def __init__(self):
        self.is_activated = False
        self.color = 'Vermelho'
        self.brand = 'BMW'
        self.speed = 0

    def turn_on(self):
        self.is_activated = True
        print(f'{self.brand} de cor {self.color} está Ligado? {self.is_activated}')

    def turn_off(self):
        self.is_activated = False
        print(f'{self.brand} de cor {self.color} está Ligado? {self.is_activated}')

    def speed_up(self):
        if not self.is_activated:
            print(f'{self.brand} não está ligado. Não é possível acelerar.')
            return
        else:
            self.speed += 10

    def slow_down(self):
        if not self.is_activated:
            print(f'{self.brand} não está ligado. Não é possível desacelerar.')
            return
        elif self.speed == 0:
            return
        else:
            self.speed -= 20


# Crie uma instância da classe carro
my_car = Car()

#Andando de carro

def riding_my_car():
    try:
        while True:
            choice = int(input('Vamos andar de carro? \n Sim: digite 1 \n Não: digite 0 \n'))
            if choice == 1:
                my_car.turn_on()
                print(f'Carro ligado! {my_car.brand} - {my_car.is_activated}')
                while  my_car.speed < 80:
                    my_car.speed_up()
                    print(f' {my_car.brand} acelerando... {my_car.speed}km/h')
                    time.sleep(1)
                    if my_car.speed == 80:
                        print(f'🚗 .........................')
                        time.sleep(10)
                while my_car.speed >0:
                    my_car.slow_down()
                    print(f'{my_car.brand} desacelerando... {my_car.speed}km/h')
                    time.sleep(1)
                    if my_car.speed == 0:
                        print(f'🚗')
                        time.sleep(5)
                my_car.turn_off()
                print(f'{my_car.brand} parada. Você chegou ao seu destino. Até a próxima viagem!!!')
                break
            elif choice == 0:
                print('Você optou por não andar de carro.')
                break
            else:
                print('Escolha inválida. Tente novamente.')  
    except ValueError as err:
        print(f'Por favor, insira um valor válido: Detalhes: {err}')

riding_my_car()

