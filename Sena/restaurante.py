total_pagado = 0

while True:
    consumo_realizado = int(input('Ingresa la cantidad consumida por el cliente: '))

    if consumo_realizado == 0:
        break

    if consumo_realizado >= 50000:
        consumo_total = consumo_realizado * 0.80
        print(f'El consumo total es de {consumo_realizado} pesos, pero hemos aplicado un descuento total al 20% por lo tanto su consumo total es de {consumo_total} pesos.')
    else:
        consumo_total = consumo_realizado
        print(f'El consumo total es de {consumo_total} pesos.')

    total_pagado += consumo_total

print(f'\nEl total de todos los pagos es de {total_pagado:.2f} pesos.')