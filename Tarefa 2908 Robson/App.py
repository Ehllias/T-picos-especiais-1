colegas = ["Ehllias", "Hamilton", "Helen", "Isabela", "Isabela Serafini", "Jeferson", "João", "João Marçal", "Jonas", "Jhonatas", "Kelven", "Leandro", "Lucas", "Laura", "Mariana", "Marcos", "Maria", "Matheus", "Matheus" "Covizzi", "Victoria", "Vinícius", "Vittor", "Vitoria"]

cidades = ["Dobrada", "Taquaritinga", "Taquaritinga", "Taquaritinga", "Taquaritinga", "Taquaritinga", "Jaboticabal", "Ibitinga", "Taquaritinga", "Jaboticabal", "Taquaritinga", "Candido Rodrigues", "Taquaritinga", "Taquaritinga", "Dobrada", "Jaboticabal", "Jaboticabal", "Matão", "Itápolis", "Matão", "Araraquara", "Jaboticabal", "Taquaritinga"]

faixaEtaria = [23, 42, 19, 19, 19, 32, 19, 19, 39, 19, 19, 19, 19, 19, 19, 19, 19, 19, 21, 19, 20, 19, 19]

def faixasEtarias(faixaEtaria):
    if 18 <= faixaEtaria <= 23:
        return "18 a 23 anos"
    elif 24 <= faixaEtaria <= 27:
        return "24 a 27 anos"
    elif 28 <= faixaEtaria <= 30:
        return "28 a 30 anos"
    elif 31 <= faixaEtaria <= 40:
        return "31 a 40 anos"
    elif 41 <= faixaEtaria <= 50:
        return "41 a 50 anos"
    elif faixaEtaria >= 51:
        return "Mais de 51 anos"
    
def dados(colegas, cidades, faixaEtaria):
    dado = {
        'Aluno':colegas[],
        'Cidade':cidades[],
        'Idade':faixaEtaria[],
    }