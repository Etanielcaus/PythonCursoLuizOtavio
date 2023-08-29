# Crie duas classes, "Aluno" e "Curso". Um aluno pode estar associado a um único curso. Implemente essa associação e crie métodos para exibir informações sobre o aluno e o curso.

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self._curso = None
    
    @property
    def curso(self):
        return self._curso
    
    @curso.setter
    def curso(self, curso):
        self._curso = curso
    
    
class Curso:
    def __init__(self, nome):
        self.nome = nome
    
    def exibir_curso(self):
        return f'{self.nome} está escrevendo'

aluno1 = Aluno(nome='luiz')
direito = Curso(nome='direito')

aluno1.curso = direito

print(direito.exibir_curso())


# escritor = Escritor('Luiz')
# caneta = FerramentaDeEscrever('Caneta Bic')
# maquina_de_escrever = FerramentaDeEscrever('Máquina')
# escritor.ferramenta = maquina_de_escrever

# print(caneta.escrever())
# print(maquina_de_escrever.escrever())
# print(escritor.ferramenta.escrever())


