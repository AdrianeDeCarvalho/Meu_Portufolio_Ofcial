class Estudante:
    escola = 'DIO'

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula


    def __str__(self):
        return f'{self.nome} - {self.matricula} - {self.escola}'
    

def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno1 = Estudante('Adriane', 1)
aluno2 = Estudante('Guilherme', 2)
mostrar_valores(aluno1, aluno2)

print()

Estudante.escola = 'Python'
aluno3 = Estudante('Chappie', 3)
mostrar_valores(aluno1, aluno2, aluno3)
