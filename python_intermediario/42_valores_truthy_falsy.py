# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
lista = [] # lista vazia = falsy
dicionario = {} # dicionario vazia = falsy
conjunto = set() # conjunto vazia = falsy
tupla = () # tupla vazia = falsy
string = '' # string vazia = falsy
inteito = 0 # inteito vazia = falsy
flutuante = 0.0 # flutuante vazia = falsy
nada = None # None = falsy
falso = False # False = falsy
intervalo = range(0) # range 0 = falsy


def falsy(valor):
    return 'falsy'if not valor else 'truthy'


print(f'TESTE', falsy('Teste'))
print(f'{lista=} =', falsy(lista))
print(f'{dicionario=} =', falsy(dicionario))
print(f'{conjunto=} =', falsy(conjunto))
print(f'{tupla=} =', falsy(tupla))
print(f'{string=} =', falsy(string))
print(f'{inteito=} =', falsy(inteito))
print(f'{flutuante=} =', falsy(flutuante))
print(f'{nada=} =', falsy(nada))
print(f'{falso=} =', falsy(falso))
print(f'{intervalo=} =', falsy(intervalo))