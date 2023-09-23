from sys import path

import aula99_package
import aula99_package.modulo
from aula99_package.modulo import soma_do_modulo # Faz a importação do modulo dentro do package

# print(*path, sep='\n')
print(soma_do_modulo(1, 2))
# print(aula99_package.modulo.soma_do_modulo(1, 2))
print(aula99_package.dobra(2))

