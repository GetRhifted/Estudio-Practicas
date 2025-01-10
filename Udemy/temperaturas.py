def cantidad_dias():
    while True:
        try:
            dias = int(input("Por favor ingresa la cantidad de días a los que quieres registrar sus temperaturas: "))
            if dias <= 0:
                raise ValueError("Recuerda registrar al menos un (1) día y hacer uso de numeros positivos.")
            return dias
        except ValueError as e:
            print(e)

def temperaturas_registro(dias):
    temperaturas = []
    while len(temperaturas) < dias:
        try:
            temperatura = int(input(f"Ingresa la temperatura registrada en el día {len(temperaturas) + 1}: "))
            if not temperatura:
                raise ValueError("No estas registrando datos.")
            temperaturas.append(temperatura)
        except ValueError as e:
            print(e)
    return temperaturas

def crear_archivoregistro(temperaturas):
    registro = open("temperaturas.txt", "w")
    for temperatura in temperaturas:
        registro.write(f"{temperatura}\n")
    registro.close()

def read_archivotxt():
    with open("temperaturas.txt", "r") as registro:
        temperaturas = registro.readlines()
        # Convertir cada línea en un número
        temperaturas = [int(temperatura.strip()) for temperatura in temperaturas]
        return temperaturas

def promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

def temp_max(temperaturas):
    return max(temperaturas)
        
def temp_min(temperaturas):
    return min(temperaturas)

def encima_media(temperaturas,promedio_temperaturas):
    counter = 0
    for temperatura in temperaturas:
        if temperatura > promedio_temperaturas:
            counter += 1
    return counter

def main():
    print("Bienvenido al analizador de temperaturas.")
    dias = cantidad_dias()
    temperaturas_sintxt = temperaturas_registro(dias)
    registro = crear_archivoregistro(temperaturas_sintxt)
    temperaturas = read_archivotxt()
    promedio_temperaturas = promedio(temperaturas)
    temperatura_maxima = temp_max(temperaturas)
    temperatura_minima = temp_min(temperaturas)
    dias_por_encima = encima_media(temperaturas, promedio_temperaturas)
    print(f"Análisis de temperaturas:\n - Promedio: {promedio_temperaturas} °C\n - Máxima: {temperatura_maxima} °C\n - Mínima: {temperatura_minima} °C\n - Días por encima del promedio: {dias_por_encima}.")

main()

