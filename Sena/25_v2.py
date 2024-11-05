numeros = []
numeros_condicion = []

for i in range(20):
    numeros.append(int(input('Ingresa un numero: ')))

for i in numeros:
    if i <= 25:
        numeros_condicion.append(i)

print(f'Hay un total de {len(numeros_condicion)} numeros que cumplen la condición, los cuales son: {numeros_condicion}')