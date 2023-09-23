# Variáveis livres + nonocal
# O conceito chave aqui é o de encerramento (closure). Uma função interna pode acessar as variáveis da função externa na qual ela está contida, mesmo que a função externa já tenha retornado. O Python mantém uma referência a essas variáveis enquanto a função interna existir.
# def fora(x):
#     a = x # variavel livre
    
#     def dentro():
#         print(locals())# verificar variaveis locais
#         return a
#     return dentro


# dentro1 = fora(10) 
# dentro2 = fora(20) 

# print(dentro1())
# print(dentro2())


def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))