# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯
# O método @property é usado para definir um getter para um atributo de uma classe. O getter é usado para obter o valor do atributo. No caso da aula 213, o getter foi definido para o atributo cor. Quando o getter é chamado, a mensagem "ESTOU NO GETTER" é exibida e o valor do atributo _cor é retornado.

# O método @setter é usado para definir um setter para um atributo de uma classe. O setter é usado para definir o valor do atributo. No exemplo mostrado na aula 213, o setter foi definido para o atributo cor. Quando o setter é chamado, a mensagem "SETANDO NOVA COR" é exibida e o valor do atributo _cor é definido.

# O getter e o setter são usados para controlar o acesso aos atributos de uma classe. No caso da aula 213, o getter e o setter foram usados para controlar o acesso ao atributo _cor. O getter é usado para obter o valor do atributo e o setter é usado para definir o valor do atributo.

# O método @property é necessário para definir um getter, mesmo que não haja uma atribuição de valor para o atributo no __init__. Isso ocorre porque o getter é usado para obter o valor atual do atributo, que pode ter sido definido em outro lugar. Já o método @setter é necessário para definir um setter, pois é nesse método que o valor do atributo é definido.
class Caneta:
    def __init__(self, cor):
        # private protected
        self.cor = cor
        self._cor_tampa = None

    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor

    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        self._cor = valor

    @property
    def cor_tampa(self):
        return self._cor_tampa

    @cor_tampa.setter
    def cor_tampa(self, valor):
        self._cor_tampa = valor


caneta = Caneta('Azul')
caneta.cor = 'Rosa'
caneta.cor_tampa = 'Azul'
print(caneta.cor)
print(caneta.cor_tampa)