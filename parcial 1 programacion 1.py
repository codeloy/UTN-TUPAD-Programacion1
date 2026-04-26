#Parcial 1 - Programación 1 
#Sistema de Control de Inventario

#declarar variables
herramientas = []
existencias = []
opcion = 0

#Bucle principal
while True:
    print("***Menu principal***")
    print("1. Carga Herramientas")
    print("2. Carga de Existencias")
    print("3. Visualización de Inventario")
    print("4. Consulta Stock")
    print("5. Reporte Agotados")
    print("6. Alta Nuevo Producto")
    print("7. Actualización de Stock")
    print("8. Salir")
    
    #Ingresar número del menu
    opcion_str = input("Elija del menu: \n").strip()
    #comprobar si son numeros
    if not opcion_str.isdigit():
        print("Error: ingrese un número válido.\n")
        continue

    opcion = int(opcion_str)
    # Validacion de opciones de menu
    if opcion < 1 or opcion > 8:
        print("Error: Opción fuera de rango.")
        continue #Vuelve a mostrar el menu

    # Carga Herramientas
    if opcion == 1:

        while True:
                #Cuantas herramientas desea cargar?
                num_tools_str = input("Cantidad Herramientas que quiere Cargar: \n").strip()
                #comprobar si son numeros
                if not num_tools_str.isdigit():
                    print("Ingrese solo números.")
                    continue
                break
        num_tools = int(num_tools_str)
    
        #Itera la cantidad de herramientas ingresadas
        for i in range(num_tools):
            while True:
                tool = input("Ingrese las Herramientas: \n").strip().capitalize()
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
                break 
            #Agrega el valor de tool a herramientas
            herramientas.append(tool)

    #Carga de Existencias
    elif opcion == 2:
        existencias.clear()
        for h in herramientas:
            while True:
                #Muestra de que producto ingresar unidades
                cantidad_str = input(f"Ingrese unidades para {h}: \n")
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

    #Visualización de Inventario
    elif opcion == 3:
        #Avisa si no hay productos cargados
        if len(herramientas) == 0:
            print("No hay ninguna herramienta cargada")
        #Avisa si no hay unidades cargadas
        elif len(existencias) == 0:
            print("No hay ninguna cantidad cargada")
        #Ya comprobado, Muestra el stock: productos y unidades
        else:
            for i in range(len(herramientas)):
                print(f"{existencias[i]} unidades del producto: {herramientas[i]}\n")

    # Consulta Stock
    elif opcion == 4:
        #Avisa si no hay productos cargados
        if len(herramientas) == 0:
            print("No hay productos cargados")
        #Avisa si no hay unidades cargadas
        elif len(existencias) == 0:
            print("No hay unidades cargadas")
        #Si hay productos o unidades, permite la busqueda
        else:
            while True:
                    #Variable bandera
                    encontrado = False
                    search_prod = input("Ingrese la Herramienta: \n").strip().capitalize()
                    #Valida que el producto no sea ""
                    if search_prod == "":
                        print("Nombre vacio")
                        continue
                    #Valida que sea una palabra
                    if not search_prod.isalpha():
                        print("Nombre Incorrecto")
                        continue
                    #Recorre los indices y mantengo sincronizacion de listas
                    for i in range(len(herramientas)):
                        if herramientas[i] == search_prod:
                            #Cambia el valor 
                            encontrado = True
                            #Muestra el producto y las unidades
                            print(f"Producto buscado: {herramientas[i]}, con {existencias[i]} unidades\n")
                            break 
                    #El valor False confirma que no hay valores
                    if encontrado == False:
                        print("El producto no se encuentra en stock")
                        continue
                    break
            
    # Reporte Agotados        
    elif opcion == 5:
        #variable bandera
        hay_agotado = False
        #Recorre para buscar si hay 0 unidades
        for i in range(len(existencias)):
            if existencias[i] == 0:
                agotado = existencias[i]
                prod_agotado = herramientas[i]
                #Si hay alguno con 0 cambia la bandera
                hay_agotado = True
                print(f"Producto: {prod_agotado} con {agotado} unidades\n")
                #si la bandera no cambia, no hay 0
        if hay_agotado == False:
            print("No hay productos agotados\n")

    # Alta Nuevo Producto
    elif opcion == 6:

        add_producto = input("Ingrese el producto a agregar: \n").strip().capitalize()
        #Valida que tool no sea ""
        if add_producto == "":
            print("Nombre vacio, ha vuelto al menu")
        
        #valida que no se repitan las herramientas
        elif add_producto in herramientas:
            print("El producto ya existe, ha vuelto al menu")
        
        else:
            add_unidades_str = input(f"Ingrese unidades para {add_producto}: \n")
            #Valida si es número
            if not add_unidades_str.isdigit():
                print("Error: Solo debe ingresar números, ha vualto al menu")

            else:
                add_unidades = int(add_unidades_str)
                #Comprueba si es menor o igual a 0
                if add_unidades < 0:
                    print("Error: Ingrese un números positivos, ha vuelto al menu")
                else:    
                    #Si pasan las validaciones, se agregan a las listas
                    herramientas.append(add_producto)
                    existencias.append(add_unidades)

    # Actualización de Stock
    elif opcion == 7:
        while True:
            while True:
                sell_buy_str = input("Elija 1 para Vender y 2 para Comprar: \n")
                if not sell_buy_str.isdigit():
                    print("Error: Introduce solo 1 o 2")
                    continue
                
                sell_buy = int(sell_buy_str)

                if sell_buy != 1 and sell_buy != 2:
                    print("Error: Introduce solo 1 o 2")
                    continue
                break

            if sell_buy == 1:
                #Variable bandera
                encontrado = False

                ### Vender Producto ###
                vender_producto = input("Ingrese la Herramienta: \n").strip().capitalize()
                #Valida que el producto no sea ""
                if vender_producto == "":
                    print("Nombre vacio")
                    continue
                #Valida que sea una palabra
                if not vender_producto.isalpha():
                    print("El nombre solo debe contener letras")
                    continue

                #Recorre los indices de Herramientas
                for i in range(len(herramientas)):
                    if herramientas[i] == vender_producto: 
                        encontrado = True
                        #Muestra el producto y las unidades en stock
                        print(f"Producto buscado: {herramientas[i]}, con {existencias[i]} unidades\n")
                        break
                if encontrado == False:
                    print("El producto no existe")
                    continue 

                ### Venta de Unidades ###
                venta_unid_str = input(f"Ingrese unidades para {herramientas[i]}: \n")
                #Valida si es número
                if not venta_unid_str.isdigit():
                    print("Error: Ingrese números")
                    continue
                venta_unid = int(venta_unid_str)
                if venta_unid <= 0:
                    print("Error: Ingrese un número mayor a 0")
                    continue
        
                #Actualiza stock
                if venta_unid > existencias[i]:
                    print(f"No hay suficientes unidades a la venta")
                    continue
                else:
                    nuevo_stock = existencias[i] - venta_unid
                    existencias[i] = nuevo_stock
                break

            else:
                #Bandera para controlar
                encontrado = False

                ### Compra Producto ###
                comprar_producto = input("Herramienta a comprar: \n").strip().capitalize()
                #Valida que el producto no sea ""
                if comprar_producto == "":
                    print("Nombre vacio")
                    continue
                #Valida que sea una palabra
                if not comprar_producto.isalpha():
                    print("El nombre solo debe contener letras")
                    continue

                for i in range(len(herramientas)):
                    if herramientas[i] == comprar_producto:
                        #Cambia el valor 
                        encontrado = True
                        #Muestra el producto y las unidades en stock
                        print(f"Producto buscado: {herramientas[i]}, con {existencias[i]} unidades\n")
                        break
                if encontrado == False:
                    print("El producto no existe")
                    continue

                ### Comprar Unidades ###
                compra_unid_str = input(f"Ingrese unidades a comprar {herramientas[i]}: \n")

                #Valida si es número
                if not compra_unid_str.isdigit():
                    print("Error: Ingrese números")
                    continue
                compra_unid = int(compra_unid_str)
                if compra_unid <= 0:
                    print("Error: Ingrese un número mayor a 0")
                    continue 

                #Actualiza stock
                new_stock = existencias[i] + compra_unid
                existencias[i] = new_stock
            break

    # Opción 8 Salir
    else:
        print("Eligió salir.")
        print("El programa finalizó correctamente.") 
        break
