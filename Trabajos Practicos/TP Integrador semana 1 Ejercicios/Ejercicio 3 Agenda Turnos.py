#✅ Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

# Turnos del lunes (4 cupos)
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
# Turnos del martes (3 cupos)
martes1 = ""
martes2 = ""
martes3 = ""
opcion = 0
dia = 0

# Pedir nombre del operador
operador = input("Ingrese el operador").strip()

# Validar que contenga solo letras (.isalpha())
while not operador.isalpha():
    print("Solo puede contener letras")
    operador = input("Ingrese el operador").strip()

# Mostrar opciones
# Validar que la opción sea numérica (.isdigit())
# Validar que esté en rango (1–5)

while True:
    print("1. Reservar turno")
    print("2. Cancelar turno")#Por nombre
    print("3. Ver agenda del dia")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion_str = input("Elija del menu: ").strip()
    #comprobar si son numeros
    if not opcion_str.isdigit():
        print("Error: ingrese un número válido.")
        continue

    opcion = int(opcion_str)
    # Validacion de opciones de menu
    if opcion < 1 or opcion > 5:
        print("Error: Opción fuera de rango.")
        continue #Vuelve a mostrar el menu


    if opcion == 1:
        
        while True:
            dia = input("Elija 1 para Lunes y 2 para Martes: ")
            if not dia.isdigit():
                print("Error: Introduce solo 1 o 2")
                dia = input("Vuelve a introducir el día: ")
                continue
            
            dia = int(dia)

            if dia != 1 and dia != 2:
                print("Error: Introduce solo 1 o 2")
                dia = input("Fuera de parametros: ")
                continue
            break
            
        #Validación del paciente
        while True:
            nom_paciente = input("Ingrese el nombre del paciente: ").strip()
            if not nom_paciente.isalpha():
                print("Error: el nombre solo debe contener letras")
                continue
            #verificar si se repite el paciente
            if dia == 1:
                c_repite = nom_paciente == lunes1 or nom_paciente == lunes2 or nom_paciente == lunes3 or nom_paciente == lunes4  
            else:
                c_repite = nom_paciente == martes1 or nom_paciente == martes2 or nom_paciente == martes3
            if c_repite:
                print("Error: El paciente ya tiene turno ese día")
                continue
            break

        # Buscar el primer turno libre ("")
        if dia == 1:
            if lunes1 == "":
                lunes1 = nom_paciente
            elif lunes2 == "":
                lunes2 = nom_paciente
            elif lunes3 == "":
                lunes3 = nom_paciente
            elif lunes4 == "":
                lunes4 = nom_paciente
            else:
                print("No hay turnos disponibles el Lunes")
        else:
            if martes1 == "":
                martes1 = nom_paciente
            elif martes2 == "":
                martes2 = nom_paciente
            elif martes3 == "":
                martes3 = nom_paciente
            else:
                print("No hay turnos disponibles el Martes")
    #Cancelar turno por nombre
    elif opcion == 2:
        
              #Elegir dia
              while True:
                dia = input("Elija 1 para Lunes y 2 para Martes: ").strip()
                if not dia.isdigit() or (int(dia) != 1 and int(dia) != 2):
                    print("Error: introduce solo 1 o 2")
                    continue
                dia = int(dia)
                break
                #Pedir nombre del paciente
              while True:
                nom_paciente = input("Ingrese el nombre del paciente: ").strip()
                if not nom_paciente.isalpha():
                    print("Error: el nombre solo debe contener letras")
                    continue
                #comprobar si tiene turno en lunes
                if dia == 1:
                    existe = nom_paciente == lunes1 or nom_paciente == lunes2 or nom_paciente == lunes3 or nom_paciente == lunes4
                    if not existe:
                        print("Error: El paciente no tiene turno ese día")
                        continue
                
                else:
                    existe= nom_paciente == martes1 or nom_paciente == martes2 or nom_paciente == martes3
                    if not existe:
                        print("Error: El paciente no tiene turno ese día")
                        continue
                #Comparar nombre con cada turno y si hay coincidencia lo borra
                if dia == 1:
                    if nom_paciente == lunes1:
                        lunes1 = ""
                    elif nom_paciente == lunes2:
                        lunes2 = ""
                    elif nom_paciente == lunes3:
                        lunes3 = ""
                    elif nom_paciente == lunes4:
                        lunes4 = ""
                else:
                    if nom_paciente == martes1:
                        martes1 = ""
                    elif nom_paciente == martes2:
                        martes2 = ""
                    elif nom_paciente == martes3:
                        martes3 = ""
                break
    elif opcion == 3:
        while True:
            dia = input("Elija 1 para Lunes y 2 para Martes: ").strip()
            if not dia.isdigit() or (int(dia) != 1 and int(dia) != 2):
                print("Error: introduce solo 1 o 2")
                continue
            dia = int(dia)
            break
        
        if dia == 1:
            print("Agenda Lunes")
            if lunes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {lunes1}")
            if lunes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {lunes2}")
            if lunes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {lunes3}")
            if lunes4 == "":
                print("Turno 4: (libre)")
            else:
                print(f"Turno 4: {lunes4}")

        else:
            print("Agenda Martes")
            if martes1 == "":
                print("Turno 1: (libre)")
            else:
                print(f"Turno 1: {martes1}")
            if martes2 == "":
                print("Turno 2: (libre)")
            else:
                print(f"Turno 2: {martes2}")
            if martes3 == "":
                print("Turno 3: (libre)")
            else:
                print(f"Turno 3: {martes3}")

# Si existe, cancelar y dejar el espacio vacío ("").
    if opcion == 4:
        l_ocupado = 0
        m_ocupado = 0

        #Comprobar si esta vacio y sumo 1 a contador
        if lunes1 != "":
            l_ocupado += 1
        if lunes2 != "":
            l_ocupado += 1
        if lunes3 != "":
            l_ocupado += 1
        if lunes4 != "":
            l_ocupado += 1

        if martes1 != "":
            m_ocupado += 1
        if martes2 != "":
            m_ocupado += 1
        if martes3 != "":
            m_ocupado += 1
        #comparo la cantidad de libres por diferencia
        l_libres = 4 - l_ocupado
        m_libres = 3 - m_ocupado
        if l_ocupado > m_ocupado:
            print("Lunes tiene más turnos")
        elif m_ocupado >l_ocupado:
            print("Martes tiene más turnos")
        else:
            print("Están igualados")
        #imprimir los turnos
        print(f"Lunes Ocupados: {l_ocupado}, Libres: {l_libres}")
        print(f"Martes Ocupados: {m_ocupado}, Libres: {m_libres}")

    else:
        print("El programa se cerró efectivamente")
        break