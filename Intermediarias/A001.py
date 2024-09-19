# Python básico é simplesmente tudo que dá pra fazer com as strings e seus prÂmetros de modo geral.

# Class significa classe o que possa definir as informações dendtro do um objeto. como por exemplo num carro sendo a cor, marca, ano, entre outras informações.

# no sentido do python, a palavra chave self simplesmente faz referêcia a outros atributos, nesse sentido pode ser usado por exemplo com o _init_ para que se tenha resultados promissores.

# O método _init_ é usado como um construtor que faz a definição de atributos nas instâncias ou diretamente nas classes.

# Exemplo
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descricao(self):
        return f"Este carro é um {self.marca} {self.modelo}."

# Criando uma instância da classe Carro
meu_carro = Carro("Toyota", "Corolla")
print(meu_carro.descricao())  # Saída: Este carro é um Toyota Corolla.

#o conceito por trás de uma fstring é que ela consegue por variáveis e outras funções ou métodos dentro de uma mensagem ou dependendo num tipo variável, lembrando que o f vem de format.

print('Hello world')

data = "18.9.2024"
print(f'Hoje é {data}.')