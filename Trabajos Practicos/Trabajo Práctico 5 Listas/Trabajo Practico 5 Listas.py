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

lista_siete = [3, 55, 32, 56, 104, 6, 18]
lista_cambiada = [lista_siete[-1]] + lista_siete[:-1]
print(lista_cambiada)
    

