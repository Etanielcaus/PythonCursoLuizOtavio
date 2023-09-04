# Crie uma classe abstrata Animal com métodos abstratos emitir_som() e mover(). Em seguida, crie subclasses concretas para diferentes tipos de animais, como Cachorro, Gato e Pássaro, que implementam esses métodos de acordo com o comportamento esperado de cada animal.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def emitir_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class Cachorro(Animal):
    def __init__(self, name, som, passos):
        self.name = name
        self.som = som
        self. passos = passos

    def emitir_som(self):
        return f'{self.name} está emitindo {self.som}' 

    def mover(self):
        return f'{self.name} se moveu {self.passos} passos'

cao = Cachorro(name='Ju', som='auau', passos=8)
print(cao.emitir_som())
print(cao.mover())
