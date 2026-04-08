from random import*

#1) Crear una lista con las notas de 10 estudiantes. 
#● Mostrar la lista completa. 
#● Calcular y mostrar el promedio. 
#● Indicar la nota más alta y la más baja.
"""promedio = 0
notas_estudiantes = [8, 6.5, 4, 9.8, 7.6, 4.3, 3]
for nota in notas_estudiantes:
    promedio += nota
promedio = round(promedio)/2
nota_maxima = max(notas_estudiantes)
nota_minima = min(notas_estudiantes)
print(f"El promedio de la Lista: {notas_estudiantes} es: {promedio}, la nota mas alta es: {nota_maxima} y la nota mas baja es: {nota_minima}") """

#2) Pedir al usuario que cargue 5 productos en una lista. 
#● Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted(). 
#● Preguntar al usuario qué producto desea eliminar y actualizar la lista. 

"""productos = []
for i in range(1, 6):
    producto = input("Ingresar producto: ").strip()
    while not producto.isalpha():
        print("Error: Valor no valido")
        producto = input("Ingresar producto: ").strip()
    productos.append(producto)
    print(productos)
print(sorted(productos))

print("Que producto de la lista desea eliminar?")
eliminar = input("Producto a eliminar: ")
while not eliminar.isalpha():
        print("Error: Valor no valido")
        eliminar = input("Ingresar producto a eliminar: ").strip()
if eliminar in productos:
    productos.remove(eliminar)
    print(f"Ha eliminado {eliminar}")
    print(f"Lista actualizada {productos} sin {eliminar}")
else:
     print("El producto que desea eliminar no se encuentra en la lista")"""

#3)Generar una lista con 15 números enteros al azar entre 1 y 100. 
#● Crear una lista con los pares y otra con los impares. 
#● Mostrar cuántos números tiene cada lista. 

"""lista_azar = []
for num in range(1, 16):
    lista_azar.append(randint(0, 100))

lista_pares = []
lista_impares = []

for i in lista_azar:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)
print(f"La lista de números al azar es: {lista_azar}")
print(f"La lista de números pares es: {lista_pares} con una cantidad de {len(lista_pares)} elementos")
print(f"La lista de números impares es: {lista_impares} con una cantidad de {len(lista_impares)} elementos")"""

#4) Dada una lista con valores repetidos: 
#● Crear una nueva lista sin elementos repetidos. 
#● Mostrar el resultado.
"""datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

no_repetidos = []
 
for num in datos:
    if num not in no_repetidos:
       no_repetidos.append(num) 
print(no_repetidos)"""

#5)Crear una lista con los nombres de 8 estudiantes presentes en clase. 
#● Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente. 
#● Mostrar la lista final actualizada. 

"""estudiantes = ["Juan", "Carla", "Ezequiel", "Laura", "Esteban",
                "Florencia", "Oscar", "Vanesa"]
print(f"Desea agregar un estudiante o borrar uno existente de estos:\n {estudiantes}")

agregar = input("Agregar un estudiante 'S/N' ").strip().lower()

if agregar == "s":
    estudiante = input("Nombre del estudiante: ").title()
    estudiantes.append(estudiante)

eleccion = input("Borrar estudiante 'S/N' ").strip().lower()
if eleccion == "s":
    borrar = input("Nombre estudiante a borrar: ").strip().title()
    while borrar not in estudiantes:
        borrar = input("Vuelva a introducir el nombre: ").strip().title()
    estudiantes.remove(borrar)
print(f"Estudiante {borrar} eliminado con éxito")
print(f"Lista actualizada {estudiantes}")"""

#6)Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha 
#(el último pasa a ser el primero). 

"""lista_siete = [3, 55, 32, 56, 104, 6, 18]
lista_cambiada = [lista_siete[-1]] + lista_siete[:-1]
print(lista_cambiada)"""
    

#9)Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de 
#una semana. 
#● Calcular el promedio de las mínimas y el de las máximas. 
#● Mostrar en qué día se registró la mayor amplitud térmica.
"""temp_semana = []
total_min = 0
total_max = 0
amplitud = 0
amplitud_max = 0

for i in range(1, 8):
    temp_semana.append([randrange(1, 15, 1), randrange(15, 28, 1)])
print(temp_semana)

for i in range(len(temp_semana)):
    temp_min = temp_semana[i][0] # i es el indice de iteración y 0 o 1 el  
    temp_max = temp_semana[i][1] # indice de la lista de 2 elementos

    total_min += temp_min
    total_max += temp_max

    amplitud = temp_max - temp_min

    if amplitud > amplitud_max:
        amplitud_max = amplitud
        max_amplitud_total = i + 1

for i in range(0, 7):
    print(f"El día número: {i+1}, temperatura minima: {temp_semana[i][0]} temperatura maxima de: {temp_semana[i][1]}")

promedio_min = round(total_min/7, 2)
promedio_max = round(total_max/7, 2)

print(f"promedio temperaturas minimas {promedio_min}, promedio de las temperaturas altas {promedio_max}")
print(f"La mayor amplitud termica es: {amplitud_max}, en el dia número: {max_amplitud_total} de la semana")"""

#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 
#● Mostrar el promedio de cada estudiante. 
#● Mostrar el promedio de cada materia. 
""""matriz = []
total_uno = 0
total_dos = 0
total_tres = 0

for i in range(1, 6):
    matriz.append([round(random()*10, 2), round(random()*10, 2), round(random()*10, 2)])
print(matriz)   

for i in range(len(matriz)):
    nota_uno = matriz[i][0]   
    nota_dos = matriz[i][1] 
    nota_tres = matriz[i][2] 

    total_uno += nota_uno
    total_dos += nota_dos
    total_tres += nota_tres

    promedio_estudiante = round((nota_uno + nota_dos + nota_tres)/3, 2)
    print(f"Nota promedio estudiante {i+1} es {promedio_estudiante}")

promedio_uno = round(total_uno/5, 2)
promedio_dos = round(total_dos/5, 2)
promedio_tres = round(total_tres/5, 2)

print(f"Promedio Materia 1: {promedio_uno}")
print(f"Promedio Materia 2: {promedio_dos}")
print(f"Promedio Materia 3: {promedio_tres}")"""

#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3). 
#● Inicializarlo con guiones "-" representando casillas vacías. 
#● Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O". 
#● Mostrar el tablero después de cada jugada.

#Ej mofificar valores Matriz
## Ejemplo: cambiar el número 6 por 60
#matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#matriz[1][2] = 60  # Modifica la segunda sublista (índice 1), tercer elemento (índice 2)
#print(matriz) # Resultado: [[1, 2, 3], [4, 5, 60], [7, 8, 9]]

"""ta_te_ti = []
contador = 0
print("***Juego Tateti***")
for i in range(1, 4):
    ta_te_ti.append(["-", "-", "-"])

for fila in ta_te_ti:
    print(" ".join(fila))

while contador < 9:
    #Valida que sea número
    f_usuario = input("Ingresar fila 1, 2, 3: ")
    if not f_usuario.isdigit():
        print("Solo puede ingresar números")
        continue
    #valida numero entre 1 y 3
    f_usuario = int(f_usuario)
    if f_usuario < 1 or f_usuario > 3:
        print("Fuera del tablero")
        continue

    #Valida que sea número
    c_usuario = input("Ingresar columna 1, 2, 3: ")
    if not c_usuario.isdigit():
        print("Solo puede ingresar números")
        continue
    #valida numero entre 1 y 3
    c_usuario = int(c_usuario)
    if c_usuario < 1 or c_usuario > 3:
        print("Fuera del tablero")
        continue

    #Se resta 1 para coincidir con el indice
    f_usuario -= 1 
    c_usuario -= 1 

    #Comprobar si la posición esta libre
    if ta_te_ti[f_usuario][c_usuario] != "-":
        print("Posición ocupada")
        continue

    marca_usuario = input("Ingresa X o O: ").strip().upper()
    #Validar que se ingrese X o O
    if marca_usuario != "X" and marca_usuario != "O" :
        print("Elección icorrecta, ingrese X o O")
        continue
    
    #Darle a la eleccion del jugador la posición de la Matriz
    ta_te_ti[f_usuario][c_usuario] = marca_usuario 
    contador += 1

    #Imprime el Tateti con la jugada
    for fila in ta_te_ti:
        print(" ".join(fila))
print("¡Juego terminado! Gracias por jugar.")"""

#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7. 
#● Mostrar el total vendido por cada producto. 
#● Mostrar el día con mayores ventas totales. 
#● Indicar cuál fue el producto más vendido en la semana.

"""caja_registradora = []

#Llenar la Matriz con productos
for v in range(1, 8):
    caja_registradora.append([round(random()*100, 2), round(random()*100, 2), round(random()*100, 2), round(random()*100, 2)])

for fila in caja_registradora:
    print(fila)

#Cada indice será la suma del total de cada producto
suma_productos = [0, 0, 0, 0]

#Iteracion que recorre cada indice de caja_registradora
for f in caja_registradora:
   #Recorre por cada vuelta los 4 productos de un indice de caja_registadora
   for i in range(len(f)):
       #Almacena cada producto en un indice(0, 1, 2, 3) y va sumando al agregar  
       suma_productos[i] += f[i] #f son los 4 productos i es cada uno de ellos(indices 0, 1, 2, 3)

#Sumo los 4 valores y los guardo en otra lista
ventas_x_dia = []
for x in caja_registradora:
    ventas_x_dia.append(sum(x))
    
#Dia con mayores ventas
mayor_venta = 0
dia_venta_mayor = 0 #variable para identificar el día
for i in range(len(ventas_x_dia)):
    if ventas_x_dia[i] > mayor_venta:
        mayor_venta = ventas_x_dia[i]
        dia_venta_mayor = i + 1
print(f"El día con mayores ventas es: {dia_venta_mayor} por un valor de: ${round(mayor_venta, 2)}")

print("Total vendido de cada producto")
for i in range(len(suma_productos)):
    print(f"Producto {i+1}: ${round(suma_productos[i], 2)}")

#El producto mas vendido de la semana
prod_mas_vendido = 0
num_prod_mas_vendido = 0 #variable para identificar el producto
for i in range(len(suma_productos)):
    if suma_productos[i] > prod_mas_vendido:
        prod_mas_vendido = suma_productos[i]
        num_prod_mas_vendido = i + 1

print(f"El número del producto mas vendido de la semana es: {num_prod_mas_vendido} con un valor: ${prod_mas_vendido}")
"""

# 11)Crear una lista con los nombres de 10 estudiantes. 
#● Solicitar al usuario que ingrese un nombre a buscar. 
#● Indicar si el nombre se encuentra en la lista. 
#●  Mostrar la posición en la que aparece. 
#● Si no se encuentra, informar que no está en la lista. 

"""estudiantes = ["Juan", "Elias", "Manuela", "Eliana", "Ezequiel", "Laura", "Ignacio", "Elodin", "Dena", "Arliden"]
estudiante = input("Estudiante a buscar: ").strip().title()
existe = False
for i in range(len(estudiantes)):
    if estudiante == estudiantes[i]:
        existe = True
        print(f"El nombre se encuentra en la posición: {i}")
        break
if not existe:
    print("No encontrado")"""

# 12) Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista. 
#● Mostrar la lista original. 
#● Mostrar la lista ordenada de menor a mayor. 
#● Mostrar la lista ordenada de mayor a menor. 
#● Investigar el uso de sorted() y del parámetro reverse. 

numeros_enteros = []
#Guardar los 8 valores en la lista
for i in range(8):
    numeros_enteros.append(int(input(f"Ingrese el número {i+1} de 8: ")))

print(f"Lista original: {numeros_enteros}")

print(f"Lista ordenada: {sorted(numeros_enteros)}")

print(f"Lista ordenada invertida: {sorted(numeros_enteros, reverse=True)}")