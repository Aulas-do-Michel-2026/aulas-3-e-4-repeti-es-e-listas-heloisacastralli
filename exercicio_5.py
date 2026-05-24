lista_de_organismos = [
    [50, 50, 50],
    [125, 99, 12],
    [19, 91, 42],
    [40, 189, 0],
    [1, 0, 0],
    [100, 100, 70],
    [99, 12, 12]
]

maior_media = 0
posicao_maior_media = 0

for i in range(len(lista_de_organismos)):
    
    soma = 0
    
    for leitura in lista_de_organismos[i]:
        soma = soma + leitura
    
    media = soma / len(lista_de_organismos[i])
    
    if media > maior_media:
        maior_media = media
        posicao_maior_media = i

print(f"O organismo com maior média é o da posição {posicao_maior_media} da lista.")
