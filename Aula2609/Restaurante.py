# class restaurante:
#      def _init_(self, cardapio, endereco, telefone):
#         self.cardapio =  cardapio
#         self.endereco = endereco
#         self.telefone = telefone

#      def cozinha(self):
#         print(f"O cardápio do dia é {self.cardapio}, nos localizamos em {self.endereco}, e nosso telefone é {self.telefone}.")

# meurestaurante = restaurante("Lasanha","Av. Paulo Scander 192","19(99999-9999)")
# meurestaurante = cozinha()

class restaurante:
    def __init__(self, cardapio, endereco, telefone):
        self.cardapio = cardapio
        self.endereco = endereco
        self.telefone = telefone

    def cozinha(self):
        print(f"O cardápio do dia é {self.cardapio}, nos localizamos em {self.endereco}, e nosso telefone é {self.telefone}.")

meurestaurante = restaurante("Lasanha","Av. Paulo Scander 192","19(99999-9999)")
meurestaurante.cozinha()

class sorveteria(restaurante):
    def  __init__(self, cardapio, endereco, telefone, sabores):
        super().__init__(cardapio, endereco, telefone)
        self.sabores = sabores

    def imprimir_sabores(self):
        print(f"Os sabores do dia são {self.sabores}, e lembr-se que nós estamos localizados em {self.endereco}, e nosso telefone é {self.telefone}.")

sorvete = sorveteria("Menta com chocolate","Av. Paulo Scander 192","19(99999-9999)","Leite-ninho, chocolate, baunilha")
sorvete.imprimir_sabores()