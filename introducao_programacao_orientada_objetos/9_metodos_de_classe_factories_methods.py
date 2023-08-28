# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
# print(Pessoa.ano)
# Pessoa.metodo_de_classe()

# ----------------------------------------------------------------
print('-' * 80)

# Métodos de Classe:
# Em Python, métodos de classe são métodos que são associados à classe em vez de instâncias individuais dessa classe. Eles são decorados com o decorator @classmethod e recebem o primeiro argumento como a própria classe, geralmente chamado de cls.

# A principal diferença entre um método de instância e um método de classe é que um método de instância opera em instâncias específicas da classe, enquanto um método de classe opera na classe como um todo, podendo acessar ou modificar atributos da classe.

# Aqui está um exemplo de como definir e usar um método de classe:


class MinhaClasse:
    atributo_de_classe = 0
    
    def __init__(self, valor):
        self.valor = valor
    
    @classmethod
    def modificar_atributo_de_classe(cls, novo_valor):
        cls.atributo_de_classe = novo_valor

# Usando o método de classe
MinhaClasse.modificar_atributo_de_classe(10)

# Acessando o atributo de classe modificado
print(MinhaClasse.atributo_de_classe)  # Saída: 10


# Factories (Fábricas):
# O conceito de factory (fábrica) refere-se à criação de objetos complexos de forma centralizada e gerenciada. Isso é útil quando a criação de um objeto requer várias etapas ou é complexa. As factories encapsulam a lógica de criação e fornecem uma interface simples para criar objetos.

# Em Python, uma factory pode ser implementada como um método de classe que cria e retorna instâncias da classe. Isso é útil para abstrair a complexidade da criação de objetos e tornar o código mais organizado.

# Aqui está um exemplo de como usar uma factory para criar objetos de uma classe:


class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def mostrar_info(self):
        print(f"Carro: {self.marca} {self.modelo}")

class FabricaDeCarros:
    @classmethod
    def criar_carro(cls, marca, modelo):
        return Carro(marca, modelo)

# Usando a factory para criar um carro
carro1 = FabricaDeCarros.criar_carro("Toyota", "Corolla")
carro1.mostrar_info()  # Saída: Carro: Toyota Corolla
# Neste exemplo, a classe FabricaDeCarros possui um método de classe criar_carro que cria e retorna instâncias da classe Carro. Isso permite que a criação de objetos Carro seja encapsulada em uma factory, tornando o código mais legível e modular.