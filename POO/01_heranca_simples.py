class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print('Ligando o motor')


    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'



class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_caregado(self):
        print(f'{'Sim' if self.carregado else 'Não'} está carregado')


moto = Motocicleta('preta', 'abc-1234', 2)
moto.ligar_motor()

carro = Carro('branco', 'xde-0098', 4)
carro.ligar_motor()

caminhao = Caminhao('roxo', 'gfd-8712', 8, True)
caminhao.ligar_motor()
print(caminhao)
caminhao.esta_caregado()


