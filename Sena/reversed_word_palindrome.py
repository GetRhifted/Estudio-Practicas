def reversed_word(word):
    palabra_invertida = ""
    for letra in word[::-1]:
        palabra_invertida += letra
    print(f'Tu palabra "{word}" en forma invertida queda: "{palabra_invertida}".')

palabra = input('Ingresa la palabra que deseas invertir: ').lower()

reversed_word(word = palabra)