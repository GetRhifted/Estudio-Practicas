# El profesor Juan ha solicitado su ayuda para calcular el promedio
# de notas de 12 estudiantes. Usted debe construir un programa
# que permita almacenar en una lista la nota de cada estudiante.
# Después de almacenar las 12 notas debe mostrar el promedio
# del grupo.

# Primero vamos a iniciar una lista vacia donde guardaremos nuestros datos.
notas_estudiantes = []

# Menú de bienvenida.
print('*'*45)
print('Bienvenido al registro academico')
print('*'*45)
print('Por favor ingrese la siguiente información:')

# Ahora vamos a solicitar las notas de cada estudiante.
for nota in range(12):
    notas_estudiantes.append(float(input(f'Ingresa la nota del estudiante {nota + 1}: ')))

print('*'*45)  
print('Datos registrados')
print('Analizando Información.')

# Ahora calcularemos el promedio total de la clase.
promedio = sum(notas_estudiantes) / len(notas_estudiantes)

# Mostramos la información.
print('*'*45)  
print(f'El promedio total para las notas registradas es de {promedio}.')
