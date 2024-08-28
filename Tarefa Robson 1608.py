nome = input('Qual é seu nome ?')
genero = input('Qual é seu gênero ?')
faixaetaria = input('Qual é sua idade ?')
candidatos = input("Sabendo que há os candidatos A, B e C escolha: ('A', 'B' ou 'C'): ")

if candidatos == 'A':
    print("Você escolheu o Candidato A")
elif candidatos == 'B':
    print("Você escolheu o Candidato B")
elif candidatos == 'C':
    print("Você escolheu o Candidato C")
else:
    print("Escolha inválida. Por favor, escolha A, B ou C.")

def mostrarFaixaEtaria(faixaetaria):
    if 16 <= faixaetaria <= 25:
        print("Faixa etária: 16 a 25")
    elif 26 <= faixaetaria <= 30:
        print("Faixa etária: 26 a 30")
    elif 31 <= faixaetaria <= 35:
        print("Faixa etária: 31 a 35")
    elif 36 <= faixaetaria <= 45:
        print("Faixa etária: 36 a 45")
    elif 46 <= faixaetaria <= 55:
        print("Faixa etária: 46 a 55")
    elif 56 <= faixaetaria <= 65:
        print("Faixa etária: 56 a 65")
    elif faixaetaria > 65:
        print("Faixa etária: Mais de 65")
    else:
        print("A idade colocada está fora das faixas especificadas")

print(f'Muito obrigado pela sua contribuição {nome}, você por ter {faixaetaria} anos, pode ser que seu candidato vença.')