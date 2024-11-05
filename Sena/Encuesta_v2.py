votos = []
accion = 0
ficcion = 0

print('*'*75)
print('Bienvenido a la encuesta de satisfacción.')
print('Por favor ingresa la información requerida de acuerdo a tus preferencias:')

print('*'*75)
print('Ayúdanos a saber cuál es el género preferido de la gente indicando el número de tu género favorito:')
print('1 - Acción')
print('2 - Ciencia Ficción')
print('*'*75)

print('A continuación podras votar hasta 5 veces, incluye a tus amigos.')

for i in range(5):
    votos.append(int(input('Ingresa tu elección: ')))

for i in votos:
    if i == 1:
        accion += 1
    elif i == 2:
        ficcion += 1
    else:
        print('se ingreso una opción no valida, por favor vuelva a realizar sus elecciones con una opción valida: Acción (1) o Ciencia Ficción (2)')

print('Calculando votos...')

if accion > ficcion:
    print(f'Gracias a los votos recibidos, podemos saber que el género Acción es el más popular con un total de {accion} votos.')
    print('*'*75)
else:
    if ficcion > accion:
        print(f'Gracias a los votos recibidos, podemos saber que el género Ciencia Ficción es el más popular con un total de {ficcion} votos.')
        print('*'*75)
    else:
        print(f'Hay un empate con {accion} votos para cada género.')
        print('*'*75)