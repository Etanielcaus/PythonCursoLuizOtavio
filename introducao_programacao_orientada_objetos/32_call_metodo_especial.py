# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".
class CallMe:
    def __init__(self, phone, nome):
        self.phone = phone
        self.nome = nome

    def __call__(self, nome):
        print(nome, 'está chamando', self.phone)
        return 2134
    
    def __repr__(self):
        return f'({self.nome} está chamando {self.phone})'


call1 = CallMe('23945876545', 'etaniel')
print(call1)
retorno = call1('Luiz Otávio')
print(retorno)

