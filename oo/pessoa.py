class Pessoa:
    #Atributo de classe
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        #Atributo de instancias (idade, nome, filhos)
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

    #Exibe somente os atributos de instancia e não de classe
    print('Após a remoção do atributo filhos')
    print(luciano.__dict__)
    print(renzo.__dict__)

    #Exibe atributo de classe
    print('Impressão do atributo de Classe')
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)

    #id do atributo de classe Olhos (serão os mesmos ids)
    print(id(Pessoa.olhos),id(luciano.olhos), id(renzo.olhos))

    #Quando for alterar valores de atributo de Classe tem que alterar pelo nome da classe (exemplo: Pessoa.olhos = 3)
    #Se for alterar por objeto, será criado um mesmo atributo como um atributo de instancia (Exemplo: luciano.olhos = 1)
    #Só utilizar ATRIBUTO DE CLASSE quando o valor for igual para todos os objetos