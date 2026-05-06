###### TRABAJO PRÁCTICO INTEGRADOR MATEMÁTICA######

while True:

  print("Ingresa el número segun la operacíon deseada")
  print("1: Para A AND B")
  print("2: Para A OR B")
  print("3: Para (A AND B) OR NOT C")
  print("4: Para Salir")

  opcion_str = input("Elija del menu: ").strip()
    #comprobar si son numeros
  if not opcion_str.isdigit():
        print("Error: ingrese un número válido.")
        continue

  opcion = int(opcion_str)
    # Validacion de opciones de menu
  if opcion < 1 or opcion > 4:
      print("Error: Opción fuera de rango.")
      continue #Vuelve a mostrar el menu
  
  if opcion == 4:
     print("***Fin del programa***")
     break

  print("A B C | R")
  print("----------")
  for a in [0,1]:
    for b in [0,1]:
      for c in [0,1]:
        

        if opcion == 1:
          resultado = int(a and b)

        elif opcion == 2:
          resultado = int(a or b)

        elif opcion == 3:
          resultado = int((a and b) or not c)

        print (f"{a} {b} {c} {resultado}")



