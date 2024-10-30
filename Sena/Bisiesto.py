print('*'*30)
print('Bienvenido a la calculadora de Bisiestos')

año = int(input('Ingresa el año que quieres comprobar: '))

print('Comprobando...')

print(f'El año {año} es bisiesto.' if (año % 4 == 0 and año % 100 != 0) or (año % 4 == 0) else f'El año {año} no es bisisesto.')