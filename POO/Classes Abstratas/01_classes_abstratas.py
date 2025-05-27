from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    '''Quando eu digo que um método é abstrato, a classe filha é obrigada a implementar'''
    @abstractmethod
    def ligar(self):
        pass


    @abstractmethod
    def desligar(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV ...\nLigado!')

    
    def desligar(self):
        print('Desligar a TV ...\nDesligado!\n')


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o Ar Condicionado ...\nLigado!')

    
    def desligar(self):
        print('Desligar o Ar Condicionado ...\nDesligado!')


controle = ControleTV()
controle.ligar()
controle.desligar()


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
