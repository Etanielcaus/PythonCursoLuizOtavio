# Crie uma classe abstrata chamada Veiculo com métodos abstratos como acelerar e frear. Em seguida, crie classes derivadas como Carro, Moto e Bicicleta que herdem da classe Veiculo e implementem esses métodos de acordo com o tipo de veículo. Crie instâncias dessas classes e chame os métodos usando polimorfismo.

from abc import ABC, abstractmethod


class Veiculo(ABC):
    
    def acelerar(self):
        print('acelerando')
    
    @abstractmethod
    def frear(self): ...


class Carro(Veiculo):

    def frear(self):
        print('está freando')


class Moto(Veiculo):

    def frear(self):
        print('está freando')


def veiculofrear(veiculo):
    return veiculo.frear()


c1 = Carro()
c2 = Moto()

veiculofrear(c2)