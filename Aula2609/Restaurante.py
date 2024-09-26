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