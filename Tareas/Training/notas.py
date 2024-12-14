try:
    notas = []

    for nota in range(5):
        notas.append(float(input(f"Ingresa la nota {nota + 1}: ")))


        promedio = sum(notas) / len(notas)
        if promedio >= 3.0:
            print(f"El estudiante a aprobado el curso con una nota de: {promedio} ")
        
        
        else:
            print(f"El estudiante no ha aprobado la materia ya que su nota maxima es de: {promedio:.2f}")

except ValueError:
    print("Ingresa valores validos.")


# Versión mejorada:

try:
    notas = []
    
    print("Por favor, ingresa las 5 notas del estudiante (valores entre 0 y 5):")
    for i in range(5):
        nota = float(input(f"Ingrese la nota {i + 1}: "))
        
        # Validar que la nota esté en el rango permitido
        if nota < 0 or nota > 5:
            raise ValueError("Las notas deben estar entre 0 y 5.")
        
        notas.append(nota)

    # Calcular el promedio una vez que todas las notas han sido ingresadas
    promedio = sum(notas) / len(notas)
    
    # Mostrar el resultado basado en el promedio
    if promedio >= 3.0:
        print(f"El estudiante ha aprobado el curso con un promedio de: {promedio:.2f}.")
    else:
        print(f"El estudiante no ha aprobado la materia. Su promedio es de: {promedio:.2f}.")

except ValueError as e:
    print(f"Error: {e}")