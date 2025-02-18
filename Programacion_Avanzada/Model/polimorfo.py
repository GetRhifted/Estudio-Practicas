from avioneta import Avioneta
from helicóptero import Helicóptero
from jet import Jet

# Creamos nuestros objetos:
avioneta = Avioneta("Mark1", 4, 100, 2400)
helicóptero = Helicóptero("Mark2", 5, 150, 3)
jet = Jet("Mark3", 200, 400, 900, 4)

# Hacemos uso de sus metodos:
avioneta.describir()
helicóptero.describir()
jet.describir()

# Preguntas y Respuestas:

# P: ¿Qué instrucciones se utilizaron para establecer la herencia entre las clases?
# R: a cada clase hija se le asigno la clase padre "Aeronave" entre parentesis para que pueda heredar sus métodos y atributos.

# P: ¿Qué función tiene la instrucción pass?
# R: Si bien se indicarón varios métodos, solo generamos una funcionalidad real en el método "Describir", la instrucción "pass" nos permite dejar una función vacia sin que esto
# interrumpa nuestro programa.

# P: Por cada clase se ha generado un archivo. ¿Cuáles son las instrucciones que se usaron para vincular los archivos entre sí y lograr la herencia entre hijos y padre?
# R: Se usaron las instrucciones "From" e "Import", donde la primera nos permite elegir el directorio o archivo que deseamos utilizar e "Import" nos permite seleccionar el
# elemento a traer para poder hacer uso de el en nuestro archivo actual, de esa forma pudimos vincular los datos de nuestras clases y ejecutar su logica sin problemas. 

# P: ¿Para que sirven las funciones setter y getter que se agregaron a las clases?
# R: Este tipo de funciones son las que nos permiten manipular y visualizar los datos que estan registrados en nuestras clases, mediante los "setter" podemos introducir la 
# información que deseemos y gracias al "getter" podemos visualizarla y saber cual es el valor asignado a cada atributo de nuestra clase.
 