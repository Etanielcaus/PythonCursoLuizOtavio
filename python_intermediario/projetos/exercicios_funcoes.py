# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total
        
empacotamento = 3, 3
total_numeros = multiplica(*empacotamento)
print(f'Total dos valores é: {total_numeros}')

def parorimpar():
    if total_numeros % 2 == 0:
        return f"{total_numeros} é par"
    # else: #Este else é redundante, já que o código ele termina quando atinge o primeiro return
    #     return f"{total_numeros} é impar" 
    return f"{total_numeros} é impar"  # Portanto, é possível colocar fora, já que se o anterior não for alcançado, este vai.

par =  parorimpar()
print(par)

