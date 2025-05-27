class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        


    def buzinar(self):
        print('Plim plim ...')


    def parar(self):
        print('Parando bicicleta ...')
        print('Bicicleta parada!')


    def correr(self):
        print('Vrummmmmmm ...')

    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}'
    

b1 = Bicicleta('vermelha', 'Caloi', 2022, 600)

b1.buzinar()
b1.correr()
b1.parar()

print(f'Cor - {b1.cor}, modelo - {b1.modelo}, ano - {b1.ano}, valor - {b1.valor}\n')

b2 = Bicicleta('Vermelha', 'Monark', 2000, 1890)


Bicicleta.buzinar(b2)
print(f'Cor - {b2.cor}, modelo - {b2.modelo}, ano - {b2.ano}, valor - {b2.valor}\n')

print(b2)
