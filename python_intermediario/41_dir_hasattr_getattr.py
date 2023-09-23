# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'

# print(dir(string)) # checar os métodos em que o objeto possui
# print(string)
if hasattr(string, metodo): # Este trecho de código verifica se o objeto string tem um atributo ou método chamado 'upper'. O método hasattr() retorna True se o atributo ou método existir, caso contrário, retorna False.
    print('Existe upper')
    print(getattr(string, metodo)()) # Se o atributo ou método 'upper' existir no objeto string, este trecho de código usa a função getattr() para obter o valor do método com o nome especificado em metodo (neste caso, 'upper'). Em seguida, os parênteses () são adicionados para chamar o método. O método upper() converte todos os caracteres da string para maiúsculas. Neste caso, como a string é "Luiz", a saída será "LUIZ".
    # print(string.upper())
    
else:
    print('Não existe o método', metodo)