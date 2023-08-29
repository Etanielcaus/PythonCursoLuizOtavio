class Caneta:
    def __init__(self, cor):
        self.cor = cor
    
    @property
    def cor(self):
        return self._cor # ele vai retornar o primeiro valor
    
    @cor.setter # configurar cor
    def cor(self, valor):
        self._cor = valor 

    
c1 = Caneta('azul')
print(c1.cor)

# Crie uma classe chamada Pessoa com os atributos nome e idade. Implemente os métodos getter e setter para ambos os atributos. Certifique-se de que o método setter para a idade verifique se o valor é positivo.

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, value):
        self._idade = value
        if value > 0:
            print('idade positiva')
        else:
            print('Idade negativa')
        
    
p1 = Pessoa(nome='Etaniel', idade=22)
print(p1.idade)

# Crie uma classe chamada ContaBancaria com um atributo privado _saldo. Implemente os métodos getter e setter para o saldo, e adicione um método realizar_deposito que atualiza o saldo.

class ContaBanciaria:
    def __init__(self, saldo):
        self.saldo = saldo

    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, value):
        self._saldo = value
    
    def realizar_deposito(self, value):
        self._saldo += value


conta1 = ContaBanciaria(saldo=500)
conta1.realizar_deposito(value=250)
print('Seu saldo é de: ', conta1.saldo)