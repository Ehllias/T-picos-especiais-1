#list compriention é a compreenção de lista, muito usada direto em loops como while e for pode ser usada em IAs para resolução de redundâncias.

lista = [] #1 a 10
for v in range(1,11):
    lista.append(v)
print(f'conte comigo do 1 a 10: {lista}')

# a questão da list compreention está em criar uma lista e adicionar um for dentro dela no momento em que declarar a variável lista.

lista2 = [ v for v in range(11) ]
print(f'Conte comigo de 0 a 10 {lista2}')

# para que simplemeste comece pelo 1 nesse exemplo acima é necessário que seja colocado na declaração o v + 1. por exemplo:

lista2 = [ v+1 for v in range(10) ]
print(f'Conte comigo de 1 a 10 {lista2}')

#modelo com letras
lista3 = [ v for v in ('çkbvuisudbafibdfjxzbvcbjhxzcl')]
print (lista3)

#modelo com tuplas:

lista4 = []
for v in [1,2,3]:
    for b in [4,5,6]:
        #if v %2 == 0:
        lista4.append((v,b))
        print(lista4)

lista5 = [v+b for v in [1,2,3] for b in [4,5,6]]
lista6 = [(v,b) for v in [1,2,3] for b in [4,5,6]]
print(lista5)
print(lista6)