def promediador(minutos, km):
    promedio = minutos / km
    print(f'De acuerdo a la información dada, el tiempo medio es de {round(promedio, 2)} minutos por kilómetro.')

try:
   
    minutos = float(input('Ingresa la cantidad de minutos empleados: '))
    kilometros = float(input('Ingresa la cantidad de kilómetros recorridos: '))
    
    promediador(minutos = minutos, km = kilometros)

except ValueError:
    print('Ingresa valores válidos por favor.')