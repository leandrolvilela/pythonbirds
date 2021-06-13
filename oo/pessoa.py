class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)

    #adicionar atributo dinamicamente no objeto luciano (não é boa prática)
    luciano.sobrenome = 'Ramalho'
    print(luciano.sobrenome)

    #verificar os atributos e valores das instancias do objeto Pessoa
    print(luciano.__dict__)
    print(renzo.__dict__)

    #remover os atributos dinamicamente (não é boa prática)
    del luciano.filhos

    print(luciano.__dict__)
    print(renzo.__dict__)
