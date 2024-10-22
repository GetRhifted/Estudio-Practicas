# El almacén "Viste con Estilo" requiere un programa que le permita calcular tallas en función a la estarura de los clientes.

# Menú de Bienvenida.
print('*'*30)
print('Bienvenido a Viste con Estilo')
print('*'*30)
print('Para una atención más precisa por favor ingresa la siguiente información:')

# Ahora solicitamos la estatura del cliente.
estatura_usuario = float(input('¿Cuál es tu estatura? '))

print('*'*30)
print('Calculando talla...')

# Aquí implementaremos la logíca del nuestro programa para la asignación de tallas y presentamos la información.
if estatura_usuario <= 1.50:
    print(f'Según tu estatura de {estatura_usuario}, tu talla ideal es S.')
    print('Gracias por preferirinos.')
    print('*'*30)

elif estatura_usuario > 1.50 and estatura_usuario < 1.70:
    print(f'Según tu estatura de {estatura_usuario}, tu talla ideal es M.')
    print('Gracias por preferirinos.')
    print('*'*30)

elif estatura_usuario >= 1.70 and estatura_usuario < 1.80:
    print(f'Según tu estatura de {estatura_usuario}, tu talla ideal es L.')
    print('Gracias por preferirinos.')
    print('*'*30)

else:
    print(f'Según tu estatura de {estatura_usuario}, tu talla ideal es XL.')
    print('Gracias por preferirinos.')
    print('*'*30)
