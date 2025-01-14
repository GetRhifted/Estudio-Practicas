def get_range():
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad de numeros con la que deseas trabajar: "))
            if cantidad < 0:
                raise ValueError("Por favor introduce un valor positivo")
            return cantidad
        except ValueError as e:
            print(e)

def generar_lista(cantidad):
    lista_numeros = []
    while len(lista_numeros) < cantidad:
        try:
            numero = int(input(f"Por favor, ingresa el numero {len(lista_numeros) + 1}:  "))
            lista_numeros.append(numero)
        except ValueError:
            print("Por favor ingresa valores validos.")
    return lista_numeros

def mediana(lista_numeros):
    lista_numeros = sorted(lista_numeros)
    numeros = len(lista_numeros)
    if numeros % 2 == 1:
        return lista_numeros[numeros // 2]
    else:
        medio1 = lista_numeros[numeros // 2]
        medio2 = lista_numeros[numeros // 2 - 1]
        return (medio1 + medio2) / 2


def main():
    cantidad = get_range()
    lista_numeros = generar_lista(cantidad)
    resultado = mediana(lista_numeros)
    print(f"La mediana de los numeros ingresados es de: \n {resultado}. ")

def reversed_word():
    while True:
        try:
            cadena = input("Ingresa la palabra que deseas invertir: ")
            if len(cadena) == 0:
                raise ValueError("Debes ingresar al menos una palabra.")
            print(cadena[::-1])
            break
        except ValueError as e:
            print(e)

'''palabra = input("Ingresa una palabra: ")
palabra = palabra[0].lower() + palabra[1:(len(palabra) - 1)].upper() + palabra[-1].lower()
print(palabra)'''

'''subs = "Vi"
palabra2 = input("Ingresa otra palabra: ")
palabra2 = palabra2.replace(palabra2[:2], subs)
print(palabra2)'''

s1 = "Había una vez, "
s2 = "un barquito chiquitito "
s3 = "que no podía, "
s4 = "que no podía navegar."

print(s1 + s2 +  s1 + s2 + s3 + s3 + s4)

print("Érase un hombre a una nariz pegado,\n Érase una nariz superlativa,\n Érase una alquitara medio viva,\n Érase un peje espada mal barbado;")

s = "me encantan las matemáticas"
print(s.upper())

s = "Mi pasión por el chocolate es superior a mis fuerzas"
print(len(s))

print(s.find("c"))
print(s.find("t"))
print(s[17:26])

nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
ciudad = input("Ingresa la ciudad dónde vives: ")
print("Su nombre es {} {}, tiene {} años y actualmente vive en {}.".format(nombre, apellido, edad, ciudad))