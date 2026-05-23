numero = int(input("Digite um número: "))
i = 1
fatorial = 1
    
while i <= numero:
        fatorial = fatorial * i
        i = i + 1

print(f"O fatorial de {numero} é {fatorial}.")
