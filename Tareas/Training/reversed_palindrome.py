def invertir_palabra(palabra):
    """Función para invertir una palabra."""
    if len(palabra) == 0:
        raise ValueError("Por favor ingresa al menos una palabra.")
    return palabra[::-1]

def verificar_palindromo(palabra, palabra_invertida):
    """Función que verifica si una palabra es palíndroma."""
    if palabra == palabra_invertida:
        print(f"La palabra introducida fue '{palabra}', su versión al revés es '{palabra_invertida}', por lo tanto, esta palabra es palíndroma.")
    else:
        print(f"La palabra introducida fue '{palabra}', su versión al revés es '{palabra_invertida}', por lo tanto, esta palabra NO es palíndroma.")

def main():
    while True:
        try:
            print("\nBienvenido a la calculadora de palíndromos.")
            eleccion = input("¿Qué deseas hacer? 1 : Comprobar palabra. 2 : Salir: ")

            if eleccion == "1":
                palabra = input("Por favor ingresa la palabra que deseas comprobar: ").strip().lower() #El método strip() elimina los espacios en blanco (u otros caracteres innecesarios) al inicio y al final de una cadena de texto.
                if not palabra:
                    print("No ingresaste ninguna palabra. Inténtalo de nuevo.")
                    continue

                palabra_invertida = invertir_palabra(palabra)
                verificar_palindromo(palabra, palabra_invertida)

            elif eleccion == "2":
                print("Gracias por preferirnos, vuelve pronto.")
                break

            else:
                print("Selección inválida. Por favor ingresa 1 o 2.")

        except ValueError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Error inesperado: {e}")

main()