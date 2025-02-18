import csv

def lectura_archivo():
    with open("Genshin Impact Character List 2024 Merged.csv", newline='') as archivo:
        data = csv.reader(archivo, delimiter=',')
        lista_datos = list(data)
        return lista_datos

def mostrar_datos(lista_datos):
    encabezados = lista_datos[0]  # Separa los encabezados de los datos
    for fila in lista_datos[1:]:  # Itera sobre las filas sin incluir el encabezado
        print('\n'.join(f"{encabezado}: {valor}" for encabezado, valor in zip(encabezados, fila)))
        print()  # Agrega un salto de línea entre registros

def filtrar_nación(lista_datos):
    while True:
        try:
            region = input("Ingresa la región por la cual deseas filtrar a los personajes: ").capitalize().strip()
            if region not in["Mondstadt", "Liyue", "Inazuma", "Sumeru", "Fontaine", "Natlan"]:
                raise ValueError("La opción ingresada no esta disponible")
            encabezados = lista_datos[0]
            nacion = encabezados.index("Region")
            for fila in lista_datos[1:]:
                if fila[nacion].startswith(region):
                    print('\n'.join(f"{encabezado}: {valor}" for encabezado, valor in zip(encabezados, fila)))
                    print()  
            break
        except ValueError as e:
            print(e)


lista_datos = lectura_archivo()
filtrar_nación(lista_datos)
