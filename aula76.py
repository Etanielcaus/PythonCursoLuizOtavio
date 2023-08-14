import os

palavra_secreta  = 'perfume'
letras_acertadas = ''
numero_tentativas = 0

while True:
    
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1 

    if len(letra_digitada) > 1: # Detectar somente uma letra
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta: # ele vai percorrer a palavra e iterar com a letra_secreta
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    
    print(f'Palavra formada: {palavra_formada}')
    
    if palavra_formada == palavra_secreta:
        os.system('clear')
        print('VOCÊ GANHOU!! PARABÉNS')
        print(f'A palavra era {palavra_secreta}')
        print(f'Tentativas: {numero_tentativas}')
        letras_acertadas = ''
        numero_tentativas = 0