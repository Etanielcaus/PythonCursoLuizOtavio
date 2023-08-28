# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta

    @property
    def cor_tampa(self):
        return 123456

###########################


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor_tampa)

#####################################

# class Caneta:
#     def __init__(self, cor):
#         self.cor_tinta = cor

#     def get_cor(self):
#         print('GET COR')
#         return self.cor_tinta

# ###########################


# caneta = Caneta('Azul')
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())
# print(caneta.get_cor())

# ----------------------------------------------------------------
# A palavra-chave `property` em Python é usada para criar métodos de acesso para atributos de classe, permitindo que você controle como esses atributos são obtidos e definidos. Ela ajuda a encapsular a lógica de acesso aos atributos e pode ser útil quando você deseja adicionar validações, cálculos ou operações personalizadas ao acessar ou modificar um atributo.

# Vamos dar uma olhada em como usar a `property`:


class Circulo:
    def __init__(self, raio):
        self._raio = raio
    
    @property
    def raio(self):
        return self._raio
    
    @raio.setter
    def raio(self, novo_raio):
        if novo_raio >= 0:
            self._raio = novo_raio
        else:
            raise ValueError("O raio não pode ser negativo.")
    
    @property
    def area(self):
        return 3.14159 * self._raio ** 2

# Criando um objeto Circulo
circulo = Circulo(raio=5)

# Acessando o raio usando a property
print(circulo.raio)  # Saída: 5

# Acessando a área usando a property
print(circulo.area)  # Saída: 78.53975

# Tentando definir um raio negativo
try:
    circulo.raio = -2
except ValueError as e:
    print(e)  # Saída: O raio não pode ser negativo.


# No exemplo acima, a classe `Circulo` possui um atributo privado `_raio` e três métodos `raio`, `raio.setter` e `area` decorados com `@property`. 

# - O método `raio` é uma property que permite acessar o valor do raio.
# - O método `raio.setter` permite definir o valor do raio, mas com uma validação para garantir que o raio não seja negativo.
# - O método `area` é outra property que calcula a área do círculo baseada no raio.

# A `property` oferece uma maneira elegante de definir e controlar o acesso aos atributos, permitindo que você adicione lógica personalizada durante o processo de obtenção ou definição.