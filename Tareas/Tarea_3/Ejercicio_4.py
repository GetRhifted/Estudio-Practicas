# La empresa Netflix solicita ayuda para poder determinar el género de streaming más popular entre
# Acción y Ciencia Ficción, para ello necesita recolectar la preferencia de 5 personas para determinar el género favorito.

# Menú de Bienvenida.
print('*'*75)
print('Bienvenido a la encuesta de satisfacción de Netflix')
print('Por favor ingresa la información requerida de acuerdo a tus preferencias:')

# Menú de opciones.
print('*'*75)
print('Ayúdanos a saber cuál es el género preferido de la gente indicando el número de tu género favorito:')
print('1 - Acción')
print('2 - Ciencia Ficción')
print('*'*75)

# Tomamos los datos de los usuarios.
persona_1 = int(input('Primer participante, ingresa tu elección: '))
persona_2 = int(input('Segundo participante, ingresa tu elección: '))
persona_3 = int(input('Tercer participante, ingresa tu elección: '))
persona_4 = int(input('Cuarto participante, ingresa tu elección: '))
persona_5 = int(input('Quinto participante, ingresa tu elección: '))
print('*'*75)

# Contabilizamos los votos de cada opción.
print('Calculando votos...')
votos_1 = 0
votos_2 = 0

# Votación persona 1
if persona_1 == 1:
    votos_1 += 1
else:
    if persona_1 == 2:
        votos_2 += 1
    else:
        print('Opción inválida.')

# Votación persona 2
if persona_2 == 1:
    votos_1 += 1
else:
    if persona_2 == 2:
        votos_2 += 1
    else:
        print('Opción inválida.')

# Votación persona 3
if persona_3 == 1:
    votos_1 += 1
else:
    if persona_3 == 2:
        votos_2 += 1
    else:
        print('Opción inválida.')

# Votación persona 4
if persona_4 == 1:
    votos_1 += 1
else:
    if persona_4 == 2:
        votos_2 += 1
    else:
        print('Opción inválida.')

# Votación persona 5
if persona_5 == 1:
    votos_1 += 1
else:
    if persona_5 == 2:
        votos_2 += 1
    else:
        print('Opción inválida.')

# Ahora presentamos nuestros resultados.
if votos_1 > votos_2:
    print(f'Gracias a los votos recibidos, podemos saber que el género Acción es el más popular con un total de {votos_1} votos.')
    print('*'*75)
else:
    if votos_2 > votos_1:
        print(f'Gracias a los votos recibidos, podemos saber que el género Ciencia Ficción es el más popular con un total de {votos_2} votos.')
        print('*'*75)
    else:
        print(f'Hay un empate con {votos_1} votos para cada género.')
        print('*'*75)
