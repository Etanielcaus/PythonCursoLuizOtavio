# Try, except, else e finally

try:
    a = 18
    b = 0
    c = a / b
except ZeroDivisionError as error: # Ele vai tratar um erro especifico, como erro faz com que o erro va para uma variavel
    print('MSG: ', error)
    print('Nome: ', error.__class__.__name__)
    print('dividiu por zero.')
except (NameError, IndexError): # Ele vai tratar um erro especifico, e também pode tratar dois erros 
    print('Nome b não está definido')
except IndentationError as error: # faz com que o erro va para uma variavel
    print('MSG: ', error)
except Exception: # Ele vai tratar qualquer erro que ainda não foi tratado
    print('ERRO DESCONHECIDO')


print('CONTINUAR')