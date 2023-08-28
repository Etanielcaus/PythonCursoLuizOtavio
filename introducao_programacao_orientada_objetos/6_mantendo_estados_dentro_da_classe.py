# Mantendo estados dentro da Classe
class Camera:
    def __init__(self, name, shooting=False):
        self.name = name
        self.shooting = shooting

    def film(self):
        if self.shooting is True:
            print(f'{self.name} já está filmando...')
            
        
        print(f'{self.name} está filmando...')
        self.shooting = True


c1 = Camera(name='Canon')
c2 = Camera(name='Sony')

c1.film()

print(c1.shooting) # c1 está filmando
print(c2.shooting) # c2 não está filmando
c1.film()