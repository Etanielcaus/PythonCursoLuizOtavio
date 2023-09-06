# Funções decoradoras e decoradores com classes

def meu_repr(self):
    class_name = self.__class__.__name__
    class_dict = self.__dict__
    class_repr = f'{class_name}({class_dict})'
    return class_repr


def adiciona_repr(cls):
    cls.__repr__ = meu_repr
    return cls


@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome


@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)

# ----------------------------------------------------------------
def decorador_repr(classe):
    def minha_repr(objeto):
        atributos = ', '.join(f'{chave}={valor!r}' for chave, valor in objeto.__dict__.items())
        return f'{objeto.__class__.__name__}({atributos})'
    
    classe.__repr__ = minha_repr
    return classe

@decorador_repr
class MinhaClasse:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

objeto = MinhaClasse("Exemplo", 30)
print(repr(objeto))  # Isso chamará a função __repr__ personalizada definida pelo decorador

