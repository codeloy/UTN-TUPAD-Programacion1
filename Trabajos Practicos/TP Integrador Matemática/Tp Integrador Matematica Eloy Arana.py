# Trabajo Práctico Integrador - Generador de Tablas de Verdad
# Materia: Matemática y Programación
# Autor: Eloy Arana

# Bucle principal: se repite hasta que el usuario elija salir
while True:
  #Muestra en consola el menu principal
  print("Ingresa el número segun la operacíon deseada")
  print("1: Para A AND B")
  print("2: Para A OR B")
  print("3: Para (A AND B) OR NOT C")
  print("4: Para Salir")

  #El usuario ingresa el n del menu
  opcion_str = input("Elija del menu: ").strip()
  #comprueba que sean numeros, si no lo es vuelve a pedirlo
  if not opcion_str.isdigit():
        print("Error: ingrese un número válido.")
        continue
  #Convierte el dato ingresado a entero
  opcion = int(opcion_str)
    # Valida para aceptar solo los n del menu
  if opcion < 1 or opcion > 4:
      print("Error: Opción fuera de rango.")
      continue #Vuelve a mostrar el menu
  
  #Primera opción del menu
  if opcion == 1:
    #For anidado con dos valores(0, 1)
    #Crea la Tabla de verdad
    print("A  B | A AND B")
    print("--------------")
    for a in [0,1]:
      for b in [0,1]:
         #El resultado de la operacion(True, False)
         #Se castea a int() para obtener 1 o 0
         resultado = int(a and b)
         print(f"{a}  {b} |    {resultado}")

  #Segunda opción del menu
  elif opcion == 2:
    #For anidado con dos valores(0, 1)
    #Crea la Tabla de verdad
    print("A  B | A OR B")
    print("-------------")
    for a in [0,1]:
      for b in [0,1]:
        resultado = int(a or b)
        print(f"{a}  {b} |    {resultado}")

  #Tercera opción del menu
  elif opcion == 3:
    #For anidado con dos valores(0, 1)
    #Crea la Tabla de verdad    
    print("A  B  C | (A AND B) OR NOT C")
    print("----------------------------")
    #Este caso tiene tres for por tener tres variables
    #Con 3 variables hay 2**3 = 8 combinaciones posibles
    for a in [0,1]:
      for b in [0,1]:
        for c in [0,1]:
          resultado = int((a and b) or not c)
          print (f"{a}  {b}  {c} |    {resultado}")
  else:
     #Opción 4: el usuario eligió salir
     print("***Fin del programa***")
     break



