def calculo_de_area():
    lado = (input("Indique la medida de uno de los lados del terreno en metros (ejemplo: 6 metros): "))
    lado = int(lado.split("metros")[0])
    area = lado * lado
    print(f'El area del terreno seria de {area}')

def promedio():
    notas = input("Ingrese las notas a promediar separadas por una coma ',': ")
    nota = [float(n) for n in notas.split(',')]
    promedio_total = sum(nota)/len(nota)
    print(f'El promedio total es: {promedio_total}')

def iva():
    valor_producto = float(input("Ingrese el valor del producto a comprar: "))
    cantidad_producto = int(input("Ingrese la cantidad de producto que va a llevar: "))
    total_iva = cantidad_producto * valor_producto * 0.19
    precio_total = cantidad_producto * valor_producto + total_iva
    print(f'El iva para esta compra será de: {total_iva} COP y el costo total será de: {precio_total} COP')

def edad():
    año_nacimiento = int(input("Ingresa tu año de nacimiento: "))
    año_actual = 2024
    calculo_edad = año_actual - año_nacimiento
    print(f'De accuerdo a tu información tu edad es de {calculo_edad} años')
    
edad()