faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}
#Faturalmento mensal dos estados

total_faturamento = sum(faturamento_estados.values())

print("Percentual por estado:")
for estado, faturamento in faturamento_estados.items():
    percentual = (faturamento / total_faturamento) * 100
    #calcula e transforma os valores em porcentagem
    
    print(f"{estado}: {percentual:.2f}%")