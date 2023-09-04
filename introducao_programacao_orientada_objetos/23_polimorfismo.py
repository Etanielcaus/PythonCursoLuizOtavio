# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.

# O polimorfismo é um dos princípios fundamentais da programação orientada a objetos em Python e em muitas outras linguagens de programação. Em Python, o polimorfismo permite que objetos de diferentes classes respondam de maneira diferente a métodos com o mesmo nome. Isso torna o código mais flexível e genérico, facilitando a reutilização e a manutenção do código.

# Existem duas formas principais de polimorfismo em Python:

# Polimorfismo de sobrecarga de operador (ou operador sobrecarregado): Isso envolve a definição de métodos especiais em uma classe que permitem que os objetos dessa classe respondam a operadores específicos, como +, -, *, / e assim por diante. Esses métodos especiais têm nomes como __add__, __sub__, __mul__ e __div__. Quando você aplica esses operadores a objetos de diferentes classes, o Python chama automaticamente os métodos apropriados com base nos tipos dos objetos.

# Polimorfismo de método: Isso envolve a criação de métodos em diferentes classes com o mesmo nome, mas com implementações específicas para cada classe. Quando você chama esse método em um objeto, o Python seleciona a implementação correta com base no tipo do objeto em tempo de execução. Isso permite que objetos de diferentes classes respondam de maneira diferente ao mesmo método.

# Aqui está um exemplo simples de polimorfismo de método em Python:


class Animal:
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Latindo"

class Gato(Animal):
    def fazer_som(self):
        return "Miando"

# Função que usa o polimorfismo
def fazer_barulho(animal):
    return animal.fazer_som()

# Criando instâncias das classes
animal1 = Cachorro()
animal2 = Gato()

# Chamando a função usando polimorfismo
print(fazer_barulho(animal1))  # Saída: "Latindo"
print(fazer_barulho(animal2))  # Saída: "Miando"

# Neste exemplo, temos uma classe base Animal com um método fazer_som. As classes Cachorro e Gato herdam da classe Animal e implementam seu próprio método fazer_som. A função fazer_barulho usa o polimorfismo para chamar o método fazer_som em objetos de diferentes classes, e cada objeto responde de acordo com sua implementação específica. Isso é um exemplo de polimorfismo de método em Python.

from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('E-mail: enviando - ', self.mensagem)
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando - ', self.mensagem)
        return False


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificação enviada')
    else:
        print('Notificação NÃO enviada')


notificacao_email = NotificacaoEmail('testando e-mail')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('testando SMS')
notificar(notificacao_sms)