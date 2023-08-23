
# nos caminhos de sys.path

import modulo_teste
from modulo_teste import soma, variavel_modulo

print('Este módulo se chama', __name__)
# print('Este módulo se chama', __name__)
print(modulo_teste.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(modulo_teste.soma(2, 3))