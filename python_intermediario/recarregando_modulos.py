import importlib

import modulo_teste

print(modulo_teste.variavel)

for i in range(10):
    importlib.reload(modulo_teste)
    print(i)

print('Fim')