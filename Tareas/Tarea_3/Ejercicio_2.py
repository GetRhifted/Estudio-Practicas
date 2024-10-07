# Necesitamos un programa capaz de calcular la edad de los usuarios y de igual forma que discrimine
# en función de si la persona es mayor o menor de edad.

# Menú de inicio.
print('*'* 30)
print('Bienvenido al calculador de edades')
print('*'* 30)
print('Por favor ingresa la siguiente información:')

# Solicitamos el año de nacimiento del usuario y de igual manera el año actual en que se hace la consulta.
año_nacimiento = int(input('Ingresa tu año de nacimiento: '))
año_actual = int(input('Ingresa el año actual: '))

# Ahora que tenemos los datos necesarios podemos proceder con la logíca matemática.
edad_usuario = año_actual - año_nacimiento

print('*'*30)
print('Calculando edad...')

# Introducimos la logíca de nuestro programa y presentamos los resultados.
if edad_usuario >= 18:
    print(f'Tu edad es de {edad_usuario} años, por lo tanto eres una persona mayor de edad.')
    print('Gracias por preferirinos.')
    print('*'*30)
else:
    print(f'Tu edad es de {edad_usuario} años, por lo tanto eres una persona menor de edad.')
    print('Gracias por preferirinos.')
    print('*'*30)