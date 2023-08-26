# Introdução ao método __init__ (inicializador de atributos)
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Luiz'  # str
# print(string.upper())
# O método __init__ em Python é um método especial usado para inicializar objetos de uma classe. Ele é chamado automaticamente quando um novo objeto é criado a partir da classe. O nome __init__ é uma abreviação de "initialize", o que significa inicializar em inglês.
class Pessoa:
    def __init__(self, nome, sobrenome, idade=0): # self referencia ao objeto que está sendo utilizado
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


p1 = Pessoa('Luiz', 'Otávio', idade=30)
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'

p2 = Pessoa('Maria', 'Joana')
# p2.nome = 'Maria'
# p2.sobrenome = 'Joana'

print(p1.nome)
print(p1.sobrenome)
print(p1.idade)

print()

print(p2.nome)
print(p2.sobrenome)
print(p2.idade)