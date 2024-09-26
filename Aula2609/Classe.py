class animal:
    def _init_(self, raca, som, genero)
        self.raca = raca
        self.som = som
        self.genero = genero
def _init_ (self)
print(f"{self.raca} está {self.som}")
class cachorro(animal):
    def __init__(self, nome, idade, raca, som, genero):
        super().__init__(raca, som, genero):
        self.nome = nome
        self.idade = idade
    def sentar(self):
        print(f"{self.nome} está sentado")

meu_cachorro = cachorro("vira-lata", "chico-âtomico", "2anos", "macho")
meu_cachorro.sentar()