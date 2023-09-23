# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
def recursiva(inicio=0, fim=4):

    print(inicio, fim)

    # Caso base
    if inicio >= fim:
        return fim

    # Caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)


print(recursiva())

# Funções recursivas em Python são funções que chamam a si mesmas para resolver um problema. Essa abordagem é muito utilizada quando um problema pode ser quebrado em subproblemas menores e idênticos ao problema original. A recursão é uma técnica poderosa, mas também requer um cuidadoso planejamento para garantir que a função não entre em um loop infinito e que alcance uma condição de parada.

# A estrutura básica de uma função recursiva inclui dois elementos principais:

# 1. **Caso Base:** É uma condição que define o ponto onde a recursão deve parar. Quando o caso base é alcançado, a função recursiva para de chamar a si mesma e começa a retornar os resultados.

# 2. **Caso Recursivo:** Nessa parte, a função se chama novamente com argumentos modificados. Isso permite que o problema seja dividido em subproblemas menores e mais simples. A ideia é que, eventualmente, os subproblemas se tornem pequenos o suficiente para serem resolvidos diretamente pelo caso base.

# Aqui está um exemplo de uma função recursiva simples em Python, que calcula o fatorial de um número:


# def fatorial(n):
#     if n == 0:
#         return 1  # Caso base: fatorial de 0 é 1
#     else:
#         return n * fatorial(n - 1)  # Caso recursivo

# numero = 5
# resultado = fatorial(numero)
# print(f"O fatorial de {numero} é {resultado}")


# Neste exemplo, a função `fatorial` calcula o fatorial de um número `n`. Ela utiliza a recursão para calcular `n * fatorial(n - 1)`, onde `n - 1` é um subproblema menor do mesmo tipo. O caso base é quando `n` é igual a 0, onde o fatorial é 1. A recursão começa a diminuir `n` até alcançar o caso base, momento em que a função começa a retornar valores e calcular o resultado final.

# Lembre-se de que, ao lidar com funções recursivas, é importante garantir que a condição de parada seja alcançada e que a recursão seja feita de forma eficiente para evitar estouro de pilha em casos de profundidade excessiva.