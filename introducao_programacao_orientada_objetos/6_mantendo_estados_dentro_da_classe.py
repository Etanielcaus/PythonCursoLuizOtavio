# Mantendo estados dentro da Classe
class Camera:
    def __init__(self, name, shooting=False):
        self.name = name
        self.shooting = shooting

    def film(self):
        if self.shooting is True:
            print(f'{self.name} já está filmando...')
        else: 
            print(f'{self.name} está filmando...')
        self.shooting = True
        
    def stop_film(self):
        if not self.shooting:
            print(f'{self.name} não está filmando...')
            return
            
        
        print(f'{self.name} está parando de filmar...')
        self.shooting = False
    
    def photograph(self):
        if self.shooting is True:
            print(f'{self.name} não pode fotografar filmando...')
            return

        print(f'{self.name} está fotografando')
        self.photograph = True

c1 = Camera(name='Canon')
c2 = Camera(name='Sony')

c1.film()
c1.stop_film()
c1.photograph()
c1.film()


print('-' * 80)
print(c1.shooting) # c1 está filmando
print(c2.shooting) # c2 não está filmando
c1.film()