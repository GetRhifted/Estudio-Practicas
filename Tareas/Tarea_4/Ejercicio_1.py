# Los investigadores de la escuela ECAPMA de la UNAD están
# desarrollando un estudio para verificar si existe temporada de
# heladas en sabana de Bogotá y le han solicitado su ayuda para
# la construcción de un programa que solicite la temperatura de
# los últimos 20 días. Por cada día se debe validar y mostrar acorde
# a la temperatura registrada en qué temporada queda clasificado:

# Primero vamos iniciar 4 contadores para llevar el conteo de nuestros datos según los parametros requeridos.
temporada_de_heladas = 0
temporada_proxima_a_heladas = 0
no_hay_temporada_de_heladas = 0
suma_temperaturas = 0

# Menú de bienvenida.
print('*'*45)
print('Bienvenido al registro climatico ECAPMA')
print('*'*45)
print('Por favor ingrese la siguiente información:')

# Ahora vamos a crear un bucle for con rango 20 para capturar las temperaturas de cada uno de los 20 días.
for día in range(20):
    # Aquí se ingresaran nuestros 20 datos.
    temperatura_20_días = (int(input(f'Ingresa la temperatura del día {día + 1}: ')))
    # Ahora empieza a plicarse la logica de nuestro programa.
    suma_temperaturas += temperatura_20_días
    if día <= 6:
        temporada_de_heladas += 1
    elif día > 6 and día <= 11:
        temporada_proxima_a_heladas += 1
    else:
        no_hay_temporada_de_heladas += 1

print('*'*45)    
print('Datos registrados')
print('Analisando Información.')


# Realizamos el calculo del promedio de las temperaturas ingresadas.
promedio_temperaturas = suma_temperaturas / 20

# Mostramos nuestros resultados.    
print('*'*45)
print(f'De acuerdo a la información registrada se encuentra que hubo un total de {temporada_de_heladas} días con una temperatura menor o igual a 6 grados.')
print(f'Igualmente hubo un total de {temporada_proxima_a_heladas} días con una temperatura entre 7 y 11 grados.')
print(f'Tambien se registra un total de {no_hay_temporada_de_heladas} días donde la temperatura fue mayor a 11 grados.')
print(f'Y finalmente tambien encontramos que el promedio total de las temperaturas registradas es de {promedio_temperaturas} grados.')
print('*'*45)
