# Escopo da classe e de métodos da Classe
class Animal:
    def __init__(self, name):
        self.name = name

        variavel = 'valor' # A variavel faz parte somente deste escopo
        print(variavel)
    
    def eating(self, food=None):
        # print(variavel) # Não é possivel acessar, pois está fora da Classe
        return f'{self.name} are eating {food}' # self.food não é o ideal, pois food não recebe de Animal
    
    def executar(self, *args, **kwargs):
        return self.eating(*args, **kwargs)

lion =  Animal(name='Lion')
print(lion.name)
print(lion.eating(food='Meat'))
print(lion.executar(food='Rice'))