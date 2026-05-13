  
#1) Dado el diccionario precios_frutas  
#precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}  
#Añadir las siguientes frutas con sus respectivos precios:  
#● Naranja = 1200  
#● Manzana = 1500  
#● Pera = 2300  
#Lista ya dada con claves y valores
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450} 
#update actualiza el diccionario con los elementos nuevos
precios_frutas.update({"Naranja" : 1200, "Manzana" : 1500, "Pera" : 2300})
print("------Ejercicio 1------")
print(f"{precios_frutas}\n")

#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:  
#● Banana = 1330  
#● Manzana = 1700  
#● Melón = 2800
#Llama a la clave del dicc y modifica el valor
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print("------Ejercicio 2------")
print(f"{precios_frutas}\n")

#3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código 
#desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los 
#precios.
#Extrae las claves del dicc con keys()
lista_frutas = precios_frutas.keys()
lista_frutas = list(lista_frutas)
print("------Ejercicio 3------")  
print(f"{lista_frutas}\n")
  
#4) Escribí un programa que permita almacenar y consultar números telefónicos.  
#• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.  
#• Luego, pedí un nombre y mostrale el número asociado, si existe.
"""agenda = {}
for i in range(5):
    nombre = input("nombre: ")
    numero = input("Número de telefono: ")
    agenda[nombre] = numero
print(agenda)
for a in agenda:
    busqueda = input("Ingrese el nombre que busca: ")
    if busqueda in agenda:
        resultado = agenda.get(busqueda)
        print(f"El número de {busqueda} es: {resultado}")
        break
    else:
        print("Nombre no encontrado")
        break"""

#5) Solicita al usuario una frase e imprime:  
#• Las palabras únicas (usando un set).  
#• Un diccionario con la cantidad de veces que aparece cada palabra. 
"""frase = input("Ingresa una frase: ")
frase_cortada = frase.split(" ")
unicas = set(frase_cortada)
recuento = {}
for palabra  in frase_cortada:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print(f"Palabras Unicas: {unicas}")        
print(f"Recuendo: {recuento}")"""

#6) Permití ingresar los nombres de 3 alumnos, 
# y para cada uno una tupla de 3 notas. Luego, 
#mostrá el promedio de cada alumno.  

"""alumnos = {}
for i in range(3):
   nombre = input(f"nombre alumno{i+1}: ")
   nota1 = int(input("Primera nota: "))
   nota2 = int(input("Segunda nota: "))
   nota3 = int(input("Tercera nota: "))
   alumnos[nombre] = (nota1, nota2, nota3)


def promedio(notas_tupla):
    suma = sum(notas_tupla)
    return suma / 3

for nombre, notas in alumnos.items():
    promedio_final = promedio(notas)
    print(f"el promedio de {nombre} es: {promedio_final:.2f}")"""


#7) Se recibe el registro diario de asistencia a una capacitación en forma de lista. 
#En dicha lista pueden aparecer nombres repetidos, 
# ya que una misma persona pudo haber asistido en más de una jornada. 
#• Mostrá la lista original de asistencias.  
#• Generá un conjunto (set) a partir de la lista y 
# mostrar los empleados que asistieron al menos una vez (sin repetir nombres). 
#• Indicá cuántas veces asistió cada empleado a la capacitación. 

contador = {}
asistencias = ["Ana", "Luis", "Ana", "Maria", "Luis", "Pedro", "Ana"]
asistencia_unicas = set(asistencias)
print("------Ejercicio 7------")
#Recorre el set con for e imprime los valores
print(f"Los empleados fueron: ")
for nombre in asistencia_unicas:
    print(f"->{nombre}")
#Recorre el dicc y si encuentra repetido
#  suma 1 al valor de la clave
for nombre in asistencias:
    if nombre in contador:
        contador[nombre] += 1
    else:
        contador[nombre] = 1
#Con .items puedo iterar sobre la clave(empleado)
#y el valor(cantidad) del diccionario
for empleado, cantidad in contador.items():
    print(f"El empleado/a: {empleado} asistio:{cantidad} veces")
print("")

#8) Armá un diccionario donde las claves sean nombres de productos y los 
# valores su stock. Permití al usuario: 
# • Consultar el stock de un producto ingresado.  
# • Agregar unidades al stock si el producto ya existe.  
# • Agregar un nuevo producto si no existe.   

"""productos = {"leche" : 3, "harina" : 2, "fideos" : 7, "lentejas" : 1, "aceite" : 5}
print(f"La lista de productos es: {productos}")
consulta = input("Ingresa el producto: ").lower()
if consulta in productos:
    print(f"Con {productos.get(consulta)} unidades")
    add_unidades = int(input("Unidades a agregar: "))
    productos[consulta] += add_unidades
else:
    add_unidades = int(input(f"Unidades para {consulta}: "))
    productos[consulta] = add_unidades
print(f"Productos totales {productos}")"""

#9) Creá una agenda donde las claves sean tuplas de (día, hora)
#  y los valores sean eventos. 
#Ejemplo:  
# agenda = {
#           ("lunes", "10:00"): "Reunion",
#           ("martes", "15:00"): "Clases de ingles"
# }
#Permití consultar qué actividad hay en cierto día y hora. 

"""agenda = {}
cant_ingresos = int(input("número de ingresos a la agenda: "))

for i in range(cant_ingresos):
    dia = input("Ingresa día de la semana: ").lower()
    hora = input("Hora (HH:MM): ")
    evento = input("Ingrese el motivo: ")
    agenda[(dia), (hora)] = evento
print(agenda)
consulta_d = input("Dia a consultar: ").lower()
consulta_h = input("Hora a consultar: ")
if (consulta_d, consulta_h) in agenda:
    print(f"Actividad: {agenda[consulta_d, consulta_h]}")
else:
    print("No hay nada programado")"""

#10) Dado un diccionario que mapea nombres de países con sus capitales,
#  construí un nuevo diccionario donde:  
# • Las capitales sean las claves.  
# • Los países sean los valores.  

#Diccionario sin modificar
original = {
    "Argentina" : "Buenos Aires",
    "Chile" : "Santiago",
    "Uruguay" : "Montevideo"
    }
# Diccionario vacio para rellenar
invertido = {}
# Recorre el dicc obtiene la clave y 
# el valor, los invierte y los guarda
# en el dicc vacio
for clave, valor in original.items():
    invertido[valor] = clave
# Muestra los dos diccionarios
print(f"Diccionario Original: {original}")
print(f"Diccionario Invertido: {invertido}")
