class Foo:
    '''@property - Não quero um atributo, quero que ele rode um código com sintáxe de atributo.
    @x.setter - estou criando um set para x
    @x.deleter definir ele para deletar (não apaga da memória)
    * Para retornar valor precisa obrigatóriamente de @property.
    * Para que seja possível retornar valor, fazer uma atribuição, eu preciso do @ .setter'''
    def __init__(self, x=None):
        self._x = x

    @property 
    def x(self):
        return self._x or 0
    

    @x.setter
    def x(self, value):
        return self._x + value
    

    @x.deleter
    def x(self):
        self._x = -1
    



foo =Foo(10)
print(foo.x)
foo.x = 10
print(foo.x)
del foo.x
print(foo.x)
