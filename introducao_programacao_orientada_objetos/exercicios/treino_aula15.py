# Crie um sistema de biblioteca com as classes Livro, Autor e Biblioteca. Um autor pode ter vários livros, e a biblioteca mantém uma coleção de livros.

class Biblioteca:
    def __init__(self):
        self._livros = []
    
    def inserir_livros(self, *livros):
        self._livros.extend(livros)
        # self._produtos.extend(produtos)
    
    def mostrar_livros(self):
        print()
        for li in self._livros:
            print(li.nome, li.autor)
            

class Livro:
    def __init__(self, nome, autor):
        self.nome = nome
        self.autor = autor


b1 = Biblioteca()
autor1 = Livro(nome='Romeu e Julieta', autor='William Shakespeare')
autor2 = Livro(nome='O vermelho e o negro', autor='Stendhal')

b1.inserir_livros(autor1, autor2)
b1.mostrar_livros()

# ----------------------------------------------------------------
# Elabore um sistema de reservas de hotel com as classes Hotel, Quarto e Reserva. Um hotel possui vários quartos, e um quarto pode ser reservado várias vezes.

class Hotel:
    def __init__(self):
        self._quartos = []
    
    def adicionar_quarto(self, quarto):
        self._quartos.append(quarto)
    
    def mostrar_quartos(self):
        for quarto in self._quartos:
            print(f"Quarto: {quarto.nome}, Reservado: {quarto.reservado}")

class Quarto:
    def __init__(self, nome):
        self.nome = nome
        self.reservado = False
    
    def fazer_reserva(self):
        self.reservado = True
    
    def cancelar_reserva(self):
        self.reservado = False

class Reserva:
    def __init__(self, quarto):
        self.quarto = quarto
        quarto.fazer_reserva()

# Criar instâncias
budapeste = Hotel()
quarto1 = Quarto(nome='Quarto 1')
reserva1 = Reserva(quarto=quarto1)

# Adicionar quarto ao hotel
budapeste.adicionar_quarto(quarto1)

# Mostrar estado dos quartos
budapeste.mostrar_quartos()
