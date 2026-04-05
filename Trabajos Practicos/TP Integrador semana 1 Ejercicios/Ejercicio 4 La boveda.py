#Ejercicio 4  — “Escape Room: La Bóveda”

#Definir variables
energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = ""
opcion = 0
intentos = 0
eleccion = 0

#valida el nombre del agente
while True:
        nom_agente = input("Ingrese el nombre de su agente: ").strip()
        if not nom_agente.isalpha():
            print("Error: el nombre solo debe contener letras")
            continue 
        break 
#while general(main)
while True:
    #Verificar condicion final en cada turno
    if cerraduras_abiertas == 3:
        print("VICTORIA")
        break
    if energia <= 0 or tiempo <=0:
        print("DERROTA")
        break
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        print("DERROTA")
        break

    # Mostrar estado actual antes del menu
    print(f"Energia: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}")

    #menu opciones
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar") 
    #Ingresar numero del menu
    opcion_str = input("Elija del menu: ").strip()
    #comprobar si son numeros
    if not opcion_str.isdigit():
        print("Error: ingrese un número válido.")
        continue
    
    opcion = int(opcion_str)
    # Validar que esté en los parametros(1-3)
    if opcion < 1 or opcion > 3:
        print("Error: Opción fuera de rango.")
        continue #Vuelve a mostrar el menu

    # Opcion 1: costos, verificar anti-spam y abrir si corresponde  
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        intentos += 1

        if intentos == 3:
             alarma = True
             print("La cerrarura está trabadea! ALARMA activada")

        elif energia < 40:
            while True:
                eleccion_str = input("Elija del 1 a 3: ").strip()
                    #comprobar si son numeros
                if not eleccion_str.isdigit():
                    print("Error: ingrese un número válido.")
                    continue
                eleccion = int(eleccion_str)
                # Comprobar que sea del 1 al 3
                if eleccion < 1 or eleccion > 3:
                    print("Error: Opción fuera de rango.")
                    continue #Vuelve a mostrar el menu
                break

            if eleccion == 3:
                alarma = True 
            else:
                cerraduras_abiertas += 1
        else:
            cerraduras_abiertas += 1 
                

    # Opcion 2: hackear panel. hackear acumulando codigo, abrir si codigo es suficiente  
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        intentos = 0

        for letra in range(1,5):
            codigo_parcial = codigo_parcial + "A"
            print(f"Paso {letra}: {codigo_parcial}") 
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1    

    #Opción 3 descansar, recuperar energia con limite y penaliza si hay alarma
    else:
        energia += 15
        tiempo -= 1
        intentos = 0
        if alarma == True:
             energia -= 10
        if energia > 100:
            energia = 100