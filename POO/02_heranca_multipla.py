class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas


    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}'
    

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo = cor_pelo


class Aves(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico = cor_bico


class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Aves):
    '''__mro__ vai trazer a ordem de resolução, como o Python vai ler para encontrar os atributos e métodos dentro de Ornitorrinco'''
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        print(Ornitorrinco.__mro__)
        #print(Ornitorrinco.mro())

        super().__init__(cor_pelo= cor_pelo, cor_bico= cor_bico, nro_patas= nro_patas)


gato = Gato(nro_patas= 4, cor_pelo= 'Preto')
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=4, cor_pelo='Castanho', cor_bico= 'Laranja')
print(ornitorrinco)
