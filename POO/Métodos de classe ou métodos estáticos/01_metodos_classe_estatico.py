class Pessoa:
    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade


    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)
    

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    

p = Pessoa().criar_de_data_nascimento(2005, 30, 12, 'Adriane')
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
