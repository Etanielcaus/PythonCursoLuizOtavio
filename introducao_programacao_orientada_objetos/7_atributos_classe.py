# Atributos de Classe


class People:
    YEAR_CURRENT = 2022

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def get_yaer_birth(self):
        return People.YEAR_CURRENT - self.age


p1 = People('João', 35)
p2 = People('Helena', 12)

print(People.YEAR_CURRENT)

# People.YEAR_CURRENT = 1

print(p1.get_yaer_birth())
print(p2.get_yaer_birth())