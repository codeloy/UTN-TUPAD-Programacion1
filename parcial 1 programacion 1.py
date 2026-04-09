#Parcial 1 - Programación 1 
#Sistema de Control de Inventario

#declarar variables
herramientas = []
existencias = []
opcion = 0
#1)preguntar al usuario la cantidad de herramientas a cargar
#2)Carga de Existencias: Ingresar la cantidad de unidades para cada herramienta 
#registrada previamente, respetando el orden de ingreso

while True:
    print("Menu principal")
    print("1. Carga Herramientas")
    print("2. Cantidad de Existencias")
    print("3. Visualización de Inventario")
    print("4. Consulta Stock")
    print("5. Reporte Agotados")
    print("6. Alta Nuevo Producto")
    print("7. Actialización de Stock")
    print("8. Salir")
    #Ingresar número del menu
    opcion_str = input("Elija del menu: ").strip()
    #comprobar si son numeros
    if not opcion_str.isdigit():
        print("Error: ingrese un número válido.")
        continue

    opcion = int(opcion_str)
    # Validacion de opciones de menu
    if opcion < 1 or opcion > 8:
        print("Error: Opción fuera de rango.")
        continue #Vuelve a mostrar el menu

    if opcion == 1:
        #Cuantas herramientas desea cargar?
        #Pedir que ingrese productos
        num_tools_str = input("Cantidad Herramientas: ").strip()
        #comprobar si son numeros
        if not num_tools_str.isdigit():
            print("Ingrese solo números.")
            continue
        num_tools = int(num_tools_str)
    
        #Itera la cantidad de herramientas ingresadas
        for i in range(num_tools):
            while True:
                tool = input("Ingrese las Herramientas: ").strip().capitalize()
                #Valida que tool no sea ""
                if tool == "":
                    print("Nombre vacio")
                    continue
                #Valida que sea una palabra
                if not tool.isalpha():
                    print("Nombre Incorrecto")
                    continue
                #valida que no se repitan las herramientas
                if tool in herramientas:
                    print("Herramienta repetida")
                    continue
                break #Si todo ok, Sale del while
            #Agrega el valor de tool a herramientas
            herramientas.append(tool)

    elif opcion == 2:
        existencias.clear()
        for h in herramientas:
            while True:
                #Muestra de que producto ingresar unidades
                cantidad_str = input(f"Ingrese unidades para {h}: ")
                #Valida si es número
                if not cantidad_str.isdigit():
                    print("Error: Ingrese números")
                    continue
                cantidad = int(cantidad_str)
                if cantidad < 0:
                    print("Error: Ingrese un número mayor o igual a 0")
                    continue
                break
            #Al pasar la validaciones agrega las unidades a la lista existencia
            existencias.append(cantidad)

    elif opcion == 3:
        