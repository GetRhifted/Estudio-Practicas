def añadir():
    inventario = {}  # Diccionario para almacenar productos y cantidades
    while True:
        try:
            nombre = input("Ingresa el nombre del producto a registrar: ").strip()
            if nombre == "":
                raise ValueError("El nombre del producto no puede estar vacío.")

            if nombre not in inventario:
                cantidad = int(input(f"Ingresa la cantidad de '{nombre}' a registrar: "))
                if cantidad <= 0:
                    raise ValueError("La cantidad debe ser mayor a 0.")
                inventario[nombre] = cantidad
                print(f"Producto '{nombre}' registrado con {cantidad} unidades.\n")
            else:
                print(f"El producto '{nombre}' ya está registrado con {inventario[nombre]} unidades.")
            
            continuar = input("¿Deseas registrar otro producto? (s/n): ").strip().lower()
            if continuar != "s":
                break

        except ValueError as e:
            print(f"Error: {e}\n")

    return inventario

def main():
    inventario = añadir()
    print("\nInventario final:")
    for producto, cantidad in inventario.items():
        print(f"- {producto}: {cantidad} unidades")

main()




