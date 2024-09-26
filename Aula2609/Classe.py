class cachorro:
    def __init__(self, raca, nome, idade, genero):
        self.raca = raca
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def sentar(self):
        print(f"{self.nome} está sentado")

meu_cachorro = cachorro("vira-lata", "chico-âtomico", "2anos", "macho")
meu_cachorro.sentar()