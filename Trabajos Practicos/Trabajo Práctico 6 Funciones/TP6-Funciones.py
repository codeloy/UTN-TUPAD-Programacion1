### TRABAJO PRACTICO N 6 FUNCIONES ###

#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla 
#el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa 
#principal. 

#Devuelve el prin del String
def imprimir_hola_mundo():
    print("Hola Mundo!")
#Llamada a la función
imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre) que reciba como 
#parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si 
#se llama con saludar_usuario("Marcos"), deberá de- volver: “Hola Marcos!”. 
#Llamar a esta función desde el programa principal solicitando el nombre al 
#usuario. 

#Función con parámetro que devuelve un "saludo"
def saludar_usuario(nombre):
    print(f"Hola {nombre}!")
#Llamada a la función con parámetro
saludar_usuario("Eloy")

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia)
#que reciba cuatro parámetros e imprima: “Soy [nombre] 
#apellido], tengo [edad] años y vivo en [residencia]”. Pe- dir los datos al 
#suario y llamar a esta función con los valores in- gresados.
 
#Función definida con 4 parámetros
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#Llamada a la función con sus 4 parámetros
informacion_personal("Eloy", "Arana", 45, "Valencia")