#  Try, except, else e finally
try:
    print('Abrir arquivo')
    # 8/0
except ZeroDivisionError:
    print('Dividiu Zero')
else:
    print('Não deu erro')
finally:  # Sempre será executado, mesmo se ocorra um error
    print('Fechar arquivo')
