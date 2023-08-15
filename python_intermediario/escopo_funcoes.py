"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x= 1 # ele está em um escopo global
def escopo():
    x = 10
    
    def outra_funcao(): # Este está dentro somente desta funcao
        x = 11
        y = 2
        print(x, y) # executa o X e o y que está dentro de outra_funcao
    
    outra_funcao() # chama a funcao que está dentro de escopo 
    print(x) # X dentro da funcao escopo

print(x) # Aqui ele vai executar o X fora da function
escopo() # Executa a function

# print(x) # x não está definido fora da função

