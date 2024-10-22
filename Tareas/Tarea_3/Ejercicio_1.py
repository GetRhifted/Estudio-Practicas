# La Escuela ECAPMA busca verificar el cambio climatico en la ciudad, 
# para ello, nuestro programa requiere poder tomar la temperatura de los ultimos 5 días para generar un promedio.

# Menú de bienvenida.
print('*'*45)
print('Bienvenido al promediador climatico ECAPMA')
print('*'*45)
print('Por favor ingrese la siguiente información:')

# Ahora vamos a solicitar las temperaturas para cada día.
dia_1 = int(input('¿Cuál fue la temperatura del día 1? '))
dia_2 = int(input('¿Cuál fue la temperatura del día 2? '))
dia_3 = int(input('¿Cuál fue la temperatura del día 3? '))
dia_4 = int(input('¿Cuál fue la temperatura del día 4? '))
dia_5 = int(input('¿Cuál fue la temperatura del día 5? '))

# Ahora que contamos con nuestros datos, procedemos a realizar el calculo del promedio
# Para eso tomaremos nuestros datos y los incluiremos dentro de una lista.
temperaturas = [dia_1,dia_2,dia_3,dia_4,dia_5]

# Una vez dentro de nuestra lista procedemos a realizar nuestra logíca Matemática.
promedio_total = sum(temperaturas)/len(temperaturas)

# Ahora solo nos queda presentar la información calculada.
print('*'*45)
print('Calculando promedio...')

# Incluimos la logíca de nuestro programa. 
if promedio_total >= 22:
    print(f'El promedio de temperatura de los ultimos 5 días es de {promedio_total} grados, el clima de tu región es cálido.')
    print('Gracias por preferirinos.')
    print('*'*45)
else:
    print(f'El promedio de temperatura de los ultimos 5 días es de {promedio_total} grados, el clima de tu región es frio.')
    print('Gracias por preferirinos.')
    print('*'*45)
