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

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el ra- dio 
#como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuel- va el perímetro del círculo. 
# Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados. 

# Declarar variable Pi
PI = 3.1416
# Pide al usuario ingresar el radio
radio = int(input("Ingresa el radio: "))
# Definir la función
def calcular_area(radio):
    """ Calcula del area de un circulo dado un radio
    Argumento: radio(float)
    return: el resultado del cálculo(float)"""
    area = PI * radio**2
    return area
#Definir función
def calcular_perimetro(radio):
    """ Cálculo del Perímetro de un circulo dado un radio
    Argumento: radio(float)
    return: el resultado del cálculo(float)"""
    perimetro = 2 * PI * radio
    return perimetro
#Llamada de las dos funciones 
print(f"El Area: {calcular_area(radio):.2f}")
print(f"El Perimetro: {calcular_perimetro(radio):.2f}")

#5. Crear una función llamada segundos_a_horas(segundos) que reciba una 
#cantidad de segundos como parámetro y devuelva la cantidad de horas 
#correspondientes. Solicitar al usuario los segundos y mostrar el resultado 
#usando esta función. 

#definir Función
def segundos_a_horas(segundos):
    """Calcula la cantidad de horas
    dividiendo el parametro(segundos) por 3600"""
    horas = segundos/3600
    return horas
#pide L usuario los segundos
segundos = int(input("Ingresa la cantidad de segundos a convertir: "))
#Llama a la función
print(f"Horas: {segundos_a_horas(segundos):.2f}")

#6. Crear una función llamada tabla_multiplicar(numero) que reciba un número 
#como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. 
# Pedir al usuario el número y llamar a la fun- ción.

#Declarar función
def tabla_multiplicar(numero):
    """Crea la tabla de multiplicar, multiplicando 
    el parametro de entrada(numero) por i y 
    lo guarda en num"""
    for i in range(1, 11):
        num = numero * i
        print(f"{numero}x{i} = {num}")
#pide el ingreso del numero(parametro)
numero = int(input("Tabla de multiplicar de: "))
#llamada de función
tabla_multiplicar(numero)

#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos 
#números como parámetros y devuelva una tupla con el resultado de sumarlos, 
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

#declarar función
def operaciones_basicas(a, b):
    """Cada operación se guarda en una variable
     Cada variable se guarda en la Tupla con el resultado """ 
    suma = a + b
    resta = a - b
    multi = a * b
    div = a / b
    return (suma, resta, multi, div)
#Ingresar los datos
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
#Desempaquetado de Tupla, asigna cada elemento de la tupla a una variable(en orden)
s, r, m, d = operaciones_basicas(num1, num2)

print(f"El Resultado de la suma es: {s} ")
print(f"El Resultado de la resta es: {r} ")
print(f"El Resultado de la multiplicación es: {m} ")
print(f"El Resultado de la división es: {d:.2f}")