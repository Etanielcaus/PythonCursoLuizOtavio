# Métodos em unstancias de classes Python
class Car:
    def __init__(self, name=None):
        self.name = name
    
    def acelear(self):
        print(f'{self.name} está acelerando')


fusca = Car('Fusca')
print(fusca.name)
fusca.acelear()
print('-' * 30)
celta = Car(name='Celta')
print(celta.name)
celta.acelear()