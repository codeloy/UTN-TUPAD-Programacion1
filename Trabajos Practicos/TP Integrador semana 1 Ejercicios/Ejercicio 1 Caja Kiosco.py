########TP integrador – Repetitivas- Condicionales y Secuenciales. ##########

#Ejercicio 1— “Caja del Kiosco”
#bjetivo: Simular una compra con validaciones y cálculo de total. 

#Ingresamos el nombre de cliente str
nombre_cliente = input("Cliente: ").strip()#saca los espacios

#Valida si son todos caracteres en el String
while nombre_cliente == "" or not nombre_cliente.isalpha():
    print("Error al introducir el cliente")
    nombre_cliente = input("Cliente: ")

#Cantidad de Productos 
cant_productos = input("Introduce la cantidad de productos: ").strip()

#Valida si son numeros positivos o cero
while not cant_productos.isdigit() or int(cant_productos) == 0:
    print("Error: Introduce un numero positivo")
    cant_productos = int(input("Vuelve a introducir la cantidad de productos: "))
#convertir la variable de str a int
productos = int(cant_productos)

#definicion de variables
total_sin_descuento = 0
total_con_descuento = 0
precio_total = 0
precio = 0
descuento = 0
 
 #Bucle que recorre la cantidad de productos
for i in range(1, productos + 1):
    precio_str = input(f"producto {i} con precio: ").strip()

    #Validacion de precio
    while not precio_str.isdigit() or int(precio_str) <= 0:
        print("Error: No introdujo un dato correcto")
        precio_str = input(f"producto {i} con precio: ")
    #convertir la variable de str a int
    precio = int(precio_str)
    
    #Validar que solo se ingrese 's' o 'n'
    descuento = input("Tiene descuento? S/N: ").strip().lower()
    while descuento != "s" and descuento != "n":
        print("Error: Solo introduzca 'S' o 'N'")
        descuento = input("Tiene descuento? S/N: ").strip().lower()
    
    total_sin_descuento += precio

    #Se aplica descuento si 's' es True
    if descuento == "s":
        precio_total = precio * 0.9
    else:
        precio_total = precio

    total_con_descuento += precio_total

#Calculo del descuento
ahorro = total_sin_descuento - total_con_descuento
#Calculo del promedio
promedio = total_con_descuento / productos

print(" ")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio: ${promedio:.2f}")
print("Gracias por su compra")