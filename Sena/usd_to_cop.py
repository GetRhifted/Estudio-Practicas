tasa_de_cambio = 4436.82
costo_camisetas = []

for i in range(5):
    costo_camisetas.append(float(input('Ingresa el costo de tus productos: ')))

costo_total = float(sum(costo_camisetas))
costo_cop = costo_total * tasa_de_cambio

# :.2f indica que queremos formatear el número como un float (f) y mostrar 2 decimales después del punto decimal.
print(f'El costo total en USD es de {costo_total}, el costo en pesos colombianos seria un total de {costo_cop:.2f} pesos')