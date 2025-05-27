class Cachorro:
    '''O __init__ é o construtor'''
    def __init__(self, nome, cor, acordado=True):
        print('Inicializando a classe ...')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    
    def __del__(self):
        print('Removendo a instância da classe.')


    def falar(self):
        print('au au auuuu')


def criar_cachorro():
    c = Cachorro('Zeus', 'branco e preto', False)
    print(c.nome)

c = Cachorro('Lupi', 'preto')
c.falar()

criar_cachorro()