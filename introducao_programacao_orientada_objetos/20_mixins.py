# Abstração
# Em Python, um mixin é uma técnica de programação que permite adicionar funcionalidades a uma classe sem precisar herdar de uma classe específica. Em vez disso, você cria uma classe separada com os métodos que deseja adicionar e, em seguida, a classe principal a utiliza como um mixin, incorporando seus métodos e comportamentos.

# Os mixins são úteis quando você deseja compartilhar código entre várias classes de forma flexível, sem criar uma hierarquia complexa de herança. Eles promovem a reutilização de código e tornam o código mais modular e fácil de manter.

# Um exemplo comum de uso de mixins é quando você deseja adicionar funcionalidades específicas, como métodos de serialização, a várias classes diferentes. Em vez de criar uma classe base com esses métodos e fazer com que todas as outras classes herdem dela, você pode criar um mixin com esses métodos e simplesmente incorporá-lo nas classes que precisam dessas funcionalidades.

# Definindo um mixin com um método de serialização
class SerializableMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

# Classe principal que incorpora o mixin
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Usando o mixin para adicionar funcionalidade de serialização
class PessoaSerializavel(Pessoa, SerializableMixin):
    pass

# Criando uma instância da classe PessoaSerializavel
pessoa = PessoaSerializavel("Joao", 30)

# Agora podemos serializar a instância em JSON
print(pessoa.to_json())