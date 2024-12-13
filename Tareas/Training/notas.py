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