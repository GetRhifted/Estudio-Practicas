# Las tiendas “descuéntalo” le han solicitado su ayuda para crear
# un programa que permita calcular el IVA de n productos. Para
# esto, usted debe solicitar la cantidad del producto, el valor del
# producto y mostrar el valor a pagar incluyendo el IVA. Posterior
# al cálculo, se debe preguntar al usuario si desea registrar otro
# producto. El ciclo finaliza cuando el usuario responda que no
# desea registrar más productos.

# Establecemos la regla a seguir para que nuestro bucle while se mantenga activo.
decisión_usuario = "Si"
while decisión_usuario == "Si":
    print('*'*30)
    print('Bienvenido a Descuéntalo.')
    
    # Solicitamos la información al usuario.
    cantidad_productos = int(input('Ingrese la cantidad de productos que desea facturar: '))
    valor_producto = float(input('Ingrese por favor el valor del producto: '))

    # Realizamos nuestros calculos matemáticos.
    sub_total = cantidad_productos * valor_producto
    total_IVA = sub_total * 0.19
    total_con_IVA = sub_total + total_IVA

    # Mostramos los resultados.
    print(f'El valor total con IVA incluido para esta compra es de {total_con_IVA} COP.')

    # Preguntamos al usuario si desea continuar.
    decisión_usuario = input('¿Desea más facturar sus productos? Responda con un "Si" o un "No" de acuerdo a sus necesidades: ').capitalize()












