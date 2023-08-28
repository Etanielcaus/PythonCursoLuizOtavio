# Métodos em unstancias de classes Python
class Car:
    def __init__(self, name=None):
        self.name = name
    
    def speed_up(self):
        print(f'{self.name} está acelerando')


fusca = Car('Fusca')
print(fusca.name)
fusca.speed_up()
print('-' * 30)
celta = Car(name='Celta')
print(celta.name)
celta.speed_up()