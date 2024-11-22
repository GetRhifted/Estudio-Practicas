# Construir una función que permita saber el porcentaje de
# estudiantes que han aprobado un curso. Para esto, la función
# debe recibir como parámetro la cantidad total de estudiantes del
# curso y la cantidad de estudiantes que aprobaron el curso y con
# estos datos, la función debe calcular el porcentaje de aprobación
# del curso.

# Diseñamos una función donde se soliciten los datos necesarios para llevar acabo nuestros calculos.
def porcentaje_estudiantes_aprobados(cantidad_estudiantes, cantidad_total_de_aprobados):

    # Realizamos nuestra operación matemática.
    porcentaje_aprobacion = (cantidad_total_de_aprobados / cantidad_estudiantes) * 100

    # Mostramos los resultados.
    print(f'De acuerdo a los datos proporcionados, el porcentaje de aprobación del curso es del {porcentaje_aprobacion:.2f}%')

cantidad_estudiantes = int(input('Ingresa la cantidad de estudiantes en el curso: '))
cantidad_total_de_aprobados = int(input('Ingresa la cantidad total de los estudiantes aprobados: '))

porcentaje_estudiantes_aprobados(cantidad_estudiantes = cantidad_estudiantes, cantidad_total_de_aprobados = cantidad_total_de_aprobados)