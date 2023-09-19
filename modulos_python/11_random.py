# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
import random
import secrets
import string

# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
# random.seed(0)

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 20, 2)
# print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 20)
# print(r_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_uniform = random.uniform(10, 20)
# print(r_uniform)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nomes = ['Luiz', 'Maria', 'Helena', 'Joana']
# random.shuffle(nomes)
# print(nomes)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
novos_nomes = random.sample(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nomes, k=3)
# print(nomes)
# print(novos_nomes)

# random.choice(Iterável) -> Escolhe um elemento do iterável

# --------------------------------------------------
# Gerar numeros aleatórios seguro
#   -> O módulo secrets fornece funções para gerar números inteiros,
#   flutuantes e bytes aleatórios com segurança. Essas funções são
#   adequadas para criptografia, quando você precisa de uma fonte de
#   entropia (aleatoriedade) segura.
#   -> O módulo secrets é uma adição relativamente recente ao Python,
#   portanto, você precisará ter certeza de que está usando a versão
#   correta do Python (3.6 ou superior) se quiser usar esse módulo.
# doc: https://docs.python.org/pt-br/3/library/secrets.html

# import secrets

random.seed(0)  # Não funciona

random = secrets.SystemRandom()
print(random.randrange(10, 20, 2))
# exemplos:
# print(secrets.randbelow(50))  # -> Retorna um número inteiro aleatório em
# range(n)
#   -> secrets.randbits(k) -> Retorna um número inteiro aleatório com k bits
#   -> secrets.choice(seq) -> Retorna um elemento aleatório de uma sequência
#   -> secrets.token_bytes([nbytes=None]) -> Retorna um número inteiro
# aleatório com nbytes de tamanho
#   -> secrets.token_hex([nbytes=None]) -> Retorna uma string hexadecimal
# aleatória com nbytes de tamanho
#   -> secrets.token_urlsafe([nbytes=None]) -> Retorna uma string url-safe
# aleatória com nbytes de tamanho
#   -> secrets.compare_digest(a, b) -> Retorna True se as strings são iguais,
# False caso contrário
#   -> secrets.token_bytes([nbytes=None]) -> Retorna um número inteiro
# aleatório com nbytes de tamanho
#   -> secrets.token_hex([nbytes=None]) -> Retorna uma string hexadecimal
# aleatória com nbytes de tamanho
#   -> secrets.token_urlsafe([nbytes=None]) -> Retorna uma string url-safe
# aleatória com nbytes de tamanho
#   -> secrets.compare_digest(a, b) -> Retorna True se as strings são iguais,
# False caso contrário
#   -> secrets.token_bytes([nbytes=None]) -> Retorna um número inteiro
# aleatório com nbytes de tamanho
#   -> secrets.token_hex([nbytes=None]) -> Retorna uma string hexadecimal
# aleatória com nbytes de tamanho
#   -> secrets.token_urlsafe([nbytes=None]) -> Retorna uma string url-safe
# aleatória com nbytes de tamanho
#   -> secrets.compare_digest(a, b) -> Retorna True se as strings são iguais,
# False caso contrário
#   -> secrets.token_bytes([nbytes=None]) -> Retorna um número inteiro
# aleatório com nbytes de tamanho
#   -> secrets.token_hex([nbytes=None]) -> Retorna uma string hexadecimal
# aleatória com nbytes de tamanho
#   -> secrets.token_urlsafe([nbytes=None]) -> Retorna uma string url-safe
# aleatória com nbytes de tamanho
#   -> secrets.compare_digest(a, b) -> Retorna True se as strings são iguais,
# False caso contrário
#   -> secrets.token_bytes([nbytes=None]) -> Retorna um número inteiro
# aleatório com nbytes de tamanho
#   -> secrets.token_hex([nbytes=None]) -> Retorna uma string hexadecimal
# aleatória com nbytes de tamanho

# Criar uma senha: https://docs.python.org/pt-br/3/library/secrets.html
print(secrets.token_hex(16))

# Gerar senha segura com maiusculas, minusculas, numeros e simbolos
# https://docs.python.org/pt-br/3/library/secrets.html
alfabeto = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(secrets.choice(alfabeto) for i in range(16))
print(senha)
