from random import*

#1) Crear una lista con las notas de 10 estudiantes. 

promedio = 0
notas_estudiantes = [8, 6.5, 4, 9.8, 7.6, 4.3, 3, 6, 7.2, 10]
#Recorrer la lista y sumar elementos a promedio
for nota in notas_estudiantes:
    promedio += nota
#La suma en promedio se divide la cantidad
promedio = round(promedio / len(notas_estudiantes), 2)
#Valores minimos y maximos
nota_maxima = max(notas_estudiantes)
nota_minima = min(notas_estudiantes)
print(f"El promedio de la Lista: {notas_estudiantes} es: {promedio}")
print(f"Nota mas alta: {nota_maxima} | Nota mas baja: {nota_minima}")

#2) Pedir al usuario que cargue 5 productos en una lista. 

#Declarar lista vacía
productos = []
#Usuario ingresa los productos a la lista 
for i in range(1, 6):
    producto = input("Ingresar producto: ").strip().capitalize()
    #comprobar que sean letras
    while not producto.isalpha():
        print("Error: Valor no valido")
        producto = input("Ingresar producto: ").strip().capitalize()
    productos.append(producto)
    print(productos)
print(sorted(productos))

#Eliminar producto
print("Que producto de la lista desea eliminar?")
eliminar = input("Producto a eliminar: ").strip().capitalize()
#Validacion
while not eliminar.isalpha():
        print("Error: Valor no valido")
        eliminar = input("Ingresar producto a eliminar: ").strip().capitalize()
#Comprobar y si está, eliminarlo
if eliminar in productos:
    productos.remove(eliminar)
    print(f"Ha eliminado {eliminar}")
    print(f"Lista actualizada {productos} sin {eliminar}")
else:
     print("El producto que desea eliminar no se encuentra en la lista")

#3)Generar una lista con 15 números enteros al azar entre 1 y 100.  

lista_azar = []
#Agrega números random enteros a la lista
for num in range(1, 16):
    lista_azar.append(randint(0, 100))
#Declarar listas vacias
lista_pares = []
lista_impares = []
#Comprueba si es par o impar
for i in lista_azar:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)
print(f"La lista de números al azar es: {lista_azar}")
print(f"La lista de números pares es: {lista_pares} con una cantidad de {len(lista_pares)} elementos")
print(f"La lista de números impares es: {lista_impares} con una cantidad de {len(lista_impares)} elementos")

#4) Sacar valores repetidos: 

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

no_repetidos = []
#Si no esta repetido lo agrega a la nueva lista
for num in datos:
    if num not in no_repetidos:
       #Agrega num a la lista
       no_repetidos.append(num) 
print(no_repetidos)

#5)Lista con los nombres de 8 estudiantes presentes en clase. 
 
estudiantes = ["Juan", "Carla", "Ezequiel", "Laura", "Esteban",
                "Florencia", "Oscar", "Vanesa"]
print(f"Desea agregar un estudiante o borrar uno existente de estos:\n {estudiantes}")

agregar = input("Agregar un estudiante 'S/N' ").strip().lower()
#Si elige "s" introduce el nuevo estudiante
if agregar == "s":
    estudiante = input("Nombre del estudiante: ").title()
    estudiantes.append(estudiante)
#Elegir si borrar o no con S/N
eleccion = input("Borrar estudiante 'S/N' ").strip().lower()
if eleccion == "s":
    borrar = input("Nombre estudiante a borrar: ").strip().title()
    #Comprobar si el estudiante esta en la lista
    while borrar not in estudiantes:
        borrar = input("Vuelva a introducir el nombre: ").strip().title()
    estudiantes.remove(borrar)
    print(f"Estudiante {borrar} eliminado con éxito")
print(f"Lista actualizada {estudiantes}")

#6)Rotar todos los elementos una posición hacia la derecha 
 
lista_siete = [3, 55, 32, 56, 104, 6, 18]
#con Slicing se modifica la posición 
lista_cambiada = [lista_siete[-1]] + lista_siete[:-1]
print(lista_cambiada)
    
#9)matriz con las temperaturas mínimas y máximas de una semana. 

temp_semana = []
total_min = 0
total_max = 0
amplitud = 0
amplitud_max = 0
#Simula la carga de datos
for i in range(1, 8):
    temp_semana.append([randrange(1, 15, 1), randrange(15, 28, 1)])
print(temp_semana)
#Guarda valores min y max a dos variables
for i in range(len(temp_semana)):
    temp_min = temp_semana[i][0]   
    temp_max = temp_semana[i][1] 
    #Acumuladores para calcular promedios
    total_min += temp_min
    total_max += temp_max
    #Diferencias térmicas
    amplitud = temp_max - temp_min
    #Busqueda del valor mayor. Identifica el dia
    if amplitud > amplitud_max:
        amplitud_max = amplitud
        max_amplitud_total = i + 1

for i in range(len(temp_semana)):
    print(f"El día número: {i+1}, temperatura minima: {temp_semana[i][0]} temperatura maxima de: {temp_semana[i][1]}")

promedio_min = round(total_min/len(temp_semana), 2)
promedio_max = round(total_max/len(temp_semana), 2)

print(f"promedio temperaturas minimas {promedio_min}, promedio de las temperaturas altas {promedio_max}")
print(f"La mayor amplitud termica es: {amplitud_max}, en el dia número: {max_amplitud_total} de la semana")

#8) Crear una matriz con las notas de 5 estudiantes en 3 materias. 

#Definición de variables
matriz = []
total_uno = 0
total_dos = 0
total_tres = 0
#Simula la introducción de la matriz
for i in range(1, 6):
    matriz.append([round(random()*10, 2), round(random()*10, 2), round(random()*10, 2)])
print(matriz)   
#Acumular los valores de cada materia
for i in range(len(matriz)):
    nota_uno = matriz[i][0]   
    nota_dos = matriz[i][1] 
    nota_tres = matriz[i][2] 
    #suma los valores para calcular promedio
    total_uno += nota_uno
    total_dos += nota_dos
    total_tres += nota_tres

    promedio_estudiante = round((nota_uno + nota_dos + nota_tres)/3, 2)
    print(f"Nota promedio estudiante {i+1} es {promedio_estudiante}")

#Largo de la matriz para el calculo
cant_estudiantes = len(matriz)
#Promedio estudiante
promedio_uno = round(total_uno/cant_estudiantes, 2)
promedio_dos = round(total_dos/cant_estudiantes, 2)
promedio_tres = round(total_tres/cant_estudiantes, 2)
#Promedio por materia
print(f"Promedio Materia 1: {promedio_uno}")
print(f"Promedio Materia 2: {promedio_dos}")
print(f"Promedio Materia 3: {promedio_tres}")

#9) Juego de Ta-Te-Ti como una lista de listas (3x3). 
#definir variable y lista
ta_te_ti = []
contador = 0
print("***Juego Tateti***")
#Crea el tablero
for i in range(1, 4):
    ta_te_ti.append(["-", "-", "-"])
#muestra el tablero sin ""
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
print("¡Juego terminado! Gracias por jugar.")

#10) Registro de ventas de una tienda. 
#definir lista
caja_registradora = []

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

# 11) Busqueda de nombres en 10 estudiantes. 

#definir lista
estudiantes = ["Juan", "Elias", "Manuela", "Eliana", "Ezequiel", "Laura", "Ignacio", "Elodin", "Dena", "Arliden"]
estudiante = input("Estudiante a buscar: ").strip().title()
#Definie bandera
existe = False
#Recorrer para buscar
for i in range(len(estudiantes)):
    if estudiante == estudiantes[i]:
        #Si encuentra cambia la bandera
        existe = True
        print(f"El nombre se encuentra en la posición: {i}")
        break
if not existe:
    print("No encontrado")

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

# 13) Puntajes de un videojuego: 

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

#uso de metodos nativos(min, max, sorted)
#puntaje mayor y menor
mas_alto = max(puntajes)
mas_bajo = min(puntajes)
#Crear ranking
ranking = sorted(puntajes, reverse= True)
#Localizar indice con index()
pos_ranking = ranking.index(990) + 1

print(f"Puntaje más alto: {mas_alto} | Puntaje más bajo: {mas_bajo}")
print(f"Ranking de mayor a menor: {ranking}")
print(f"El puntaje 990 se encuentra en el puesto: {pos_ranking} del ranking")