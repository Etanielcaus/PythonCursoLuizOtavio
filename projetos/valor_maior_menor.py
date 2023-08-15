primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'o valor {primeiro_valor=} é maior que {segundo_valor=}')
elif primeiro_valor == segundo_valor:
    print(f'o valor {primeiro_valor=} é igual ao {segundo_valor=}')
else:
    print(f'o valor {segundo_valor=} é menor que o {primeiro_valor=}')
