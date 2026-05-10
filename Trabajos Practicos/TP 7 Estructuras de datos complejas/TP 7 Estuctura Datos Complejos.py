  
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
frase = input("Ingresa una frase: ")
frase_cortada = frase.split(" ")
unicas = set(frase_cortada)
recuento = {}
for palabra  in frase_cortada:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print(f"Palabras Unicas: {unicas}")        
print(f"Recuendo: {recuento}")

