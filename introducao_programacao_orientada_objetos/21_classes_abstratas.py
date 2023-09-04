# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstractmethods são métodos que não têm corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser instânciadas
# diretamente.
# Métodos abstratos DEVEM ser implementados
# nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno.
from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod
    def _log(self, msg): ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


l = LogPrintMixin()
l.log_error('Oi')
l.log_success('Oi')

# ----------------------------------------------------------------

# Em Python, abstractmethod (método abstrato) é um conceito relacionado com a programação orientada a objetos que permite criar uma classe base com métodos que devem ser implementados por suas subclasses. Um método abstrato é definido na classe base, mas não possui uma implementação real nessa classe. Em vez disso, ele serve como um contrato ou especificação para as subclasses, indicando que todas as subclasses devem fornecer uma implementação para esse método.

# Para criar um método abstrato em Python, você precisa usar o módulo abc (Abstract Base Classes). O módulo abc fornece uma classe chamada ABC (Abstract Base Class) e um decorador @abstractmethod para criar métodos abstratos. Aqui está um exemplo:


class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class Retangulo(Forma):
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura

    def calcular_area(self):
        return self.comprimento * self.largura

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        import math
        return math.pi * self.raio ** 2

circulo = Circulo(2)
print(circulo.calcular_area())


# Neste exemplo, a classe Forma é uma classe base abstrata que define um método abstrato calcular_area. As classes Retangulo e Circulo são subclasses de Forma e devem implementar o método calcular_area de acordo com as regras específicas de cada forma geométrica.

# Ao tentar criar uma instância de uma classe que herda de Forma sem implementar o método calcular_area, você obterá um erro em tempo de execução, indicando que a classe é abstrata e que o método abstrato não foi implementado. Isso garante que todas as subclasses forneçam uma implementação para o método abstrato, tornando o código mais robusto e claro em relação ao que é esperado em termos de funcionalidade.

