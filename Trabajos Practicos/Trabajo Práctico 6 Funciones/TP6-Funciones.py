### TRABAJO PRACTICO N 6 FUNCIONES ###

#1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla 
#el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa 
#principal. 

#Devuelve el prin del String
def imprimir_hola_mundo():
    print("Hola Mundo!")
#Llamada a la función
imprimir_hola_mundo()

#2. Crear una función llamada saludar_usuario(nombre)

#Función con parámetro que devuelve un "saludo"
def saludar_usuario(nombre):
    return f"Hola {nombre}!"
#Llamada a la función con parámetro
print(saludar_usuario("Eloy"))

#3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia)
 
#Función definida con 4 parámetros
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
#Llamada a la función con sus 4 parámetros
informacion_personal("Eloy", "Arana", 45, "Valencia")

#4. Crear dos funciones: calcular_area_circulo(radio) 

# Declarar variable Pi
PI = 3.1416
# Pide al usuario ingresar el radio
radio = int(input("Ingresa el radio: "))
# Definir la función
def calcular_area_circulo(radio):
    """ Calcula del area de un circulo dado un radio
    Argumento: radio(float)
    return: el resultado del cálculo(float)"""
    area = PI * radio**2
    return area
#Definir función
def calcular_perimetro_circulo(radio):
    """ Cálculo del Perímetro de un circulo dado un radio
    Argumento: radio(float)
    return: el resultado del cálculo(float)"""
    perimetro = 2 * PI * radio
    return perimetro
#Llamada de las dos funciones 
print(f"El Area: {calcular_area_circulo(radio):.2f}")
print(f"El Perimetro: {calcular_perimetro_circulo(radio):.2f}")

#5. Crear una función llamada segundos_a_horas(segundos)

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

#6. Crear una función llamada tabla_multiplicar(numero)

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

#7. Crear una función llamada operaciones_basicas(a, b)

#declarar función
def operaciones_basicas(a, b):
    """Cada operación se guarda en una variable
     Cada variable se guarda en la Tupla con el resultado """ 
    suma = a + b
    resta = a - b
    multi = a * b
    if b == 0:
        div = "No definido (div por 0)"
    else:
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

#8. Crear una función llamada calcular_imc(peso, altura)
 
#funcion con 2 parametros
def calcular_imc(peso, altura):
    """Calcúla el IMC dividiendo el peso 
     por la altura al cuadrado. Imprime el resultado """
    return peso / (altura**2) 

#Ingreso de datos
peso = float(input("Ingrese su Peso: "))
altura = float(input("Ingrese su Altura: "))

#Llamada de la función
imc = calcular_imc(peso, altura)
print(f"Su IMC(Indice de masa corporal) es: {imc:.2f}")

#9. Crear una función llamada celsius_a_fahrenheit(celsius)

#definir la función
def celsius_a_fahrenheit(celsius):
    """Formula F = (C x 1.8)+ 32
     El calculo de la formula la guarda en ft """
    ft = (celsius * 1.8) + 32
    return f"La conversión de {celsius} C a Fahrenheit es: {ft} F"

#Ingreso de datos
c = float(input("Ingrese los grados: "))
#Llamada de la función
print(celsius_a_fahrenheit(c))

#0. Crear una función llamada calcular_promedio(a, b, c) que reciba tres 
#números como parámetros y devuelva el promedio de ellos. Solicitar los 
#números al usuario y mostrar el resultado usando esta función. 

def calcular_promedio(a, b, c):
    """ Toma los 3 parametros, los suma
    y los divide por la cantidad(3)"""
    return (a + b + c) / 3
    
dato1 = int(input("Ingrese un número: "))
dato2 = int(input("Ingrese el segundo número: "))
dato3 = int(input("Ingrese el tercer número: "))

#Llamada de la función
promedio = calcular_promedio(dato1, dato2, dato3)
print(f"El promedio entre {dato1}, {dato2} y {dato3} es: {promedio} ")