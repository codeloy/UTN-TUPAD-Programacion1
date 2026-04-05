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


#Ejercicio 2  — “Acceso al Campus y Menú Seguro” 
#Objetivo: Login con intentos + menú de acciones con validación estricta.

#definicion de variables
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
ingreso_aceptado = False

#Validacion del nombre de usuario
while intentos <3:
    print(f"Intento {intentos + 1}/3")
    #El usuario ingresa el Nombre de Usuario
    usuario = input("Nombre de Usuario: ").strip().lower()
    clave = input("Ingresa la clave: ").strip()
    #comprobar si usuario y clave son correctos
    if usuario ==  usuario_correcto and clave == clave_correcta:
        print("Acceso concedido.")
        ingreso_aceptado = True
        break
    else:
        print("Error: Credenciales inválidas.")
        #contador
        intentos += 1
        if intentos >= 3:
            print("Cuenta bloqueada.")
            break
# Sale del while 

if ingreso_aceptado:
#Mostrar menu
    while True:
        print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")

        opcion_str = input("Opción: ").strip()
        #comprobar si son numeros
        if not opcion_str.isdigit():
            print("Error: ingrese un número válido.")
            continue

        opcion = int(opcion_str)
        # Validacion de opciones de menu
        if opcion < 1 or opcion > 4:
            print("Error: Opción fuera de rango.")
            continue #Vuelve a mostrar el menu
        #1 Solo imprime mensaje
        if opcion == 1:
            print("Inscripto")

        #Cambio de clave
        elif opcion == 2:
            clave_nueva = input("Ingrese su nueva clave: ").strip()
            clave_nueva_2 = input("ingresarla nuevamente: ").strip()
            #Covalidar de largo e igualdad
            if len(clave_nueva) >= 6:
                if clave_nueva == clave_nueva_2:
                    clave_correcta = clave_nueva
                    print("Clave cambiada con exito")
                else:
                    print("Error: las claves no coinciden")
            else:
                print("Error: mínimo 6 caracteres")
        #3 solo imprime mensaje
        elif opcion == 3:
            print("Hoy sabes mas que ayer, no abandones!")
        else:
            break

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


#Ejercicio 5  — “Escape Room:"La Arena del Gladiador"
#definición de variables
danio = 0.0
vida_gladiador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
ataque_enemigo = 12
turno_gladiador = True

#Introducir y validar el nombre del gladiador
while True:
    nom_gladiador = input("Nombre del Gladiador: ").strip()
    if not nom_gladiador.isalpha():
        print("Error: Solo se permiten letras")
        continue 
    break

print("--- BIENVENIDO A LA ARENA ---")
print(f"Nombre del Gladiador: {nom_gladiador}")
print("=== INICIO DEL COMBATE ===")

#Ciclo de combate
while vida_gladiador > 0 and vida_enemigo > 0:

    #Mostrar vidas y pociones
    print(f"{nom_gladiador} (HP: {vida_gladiador}) vs Enemigo (HP:{vida_enemigo}) | Pociones: {pociones}")

    #menu opciones
    print("Ëlige acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz") #bucle for
    print("3. Curar") 

    #Ingresar numero del menu
    opcion_str = input("Elegir del menu: ").strip()
    #comprobar si son numeros
    if not opcion_str.isdigit():
        print("Error: ingrese un número válido.")
        continue
    
    opcion = int(opcion_str)
    # Validar que esté en los parametros(1-3)
    if opcion < 1 or opcion > 3:
        print("Error: Opción fuera de rango.")
        continue #Vuelve a mostrar el menu

    #Opcion 1) Ataque pesado
    if opcion == 1:
        #Golpe Crítico
        if vida_enemigo < 20:
            danio= ataque_pesado * 1.5
            vida_enemigo -= danio
            print(f"¡Atacaste al enemigo por {danio} puntos de daño!")
        else:
            danio = ataque_pesado
            vida_enemigo -= danio
            print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

    #Opción 2) Ráfaga Veloz
    elif opcion == 2:
        for i in range(1,4):
                vida_enemigo -= 5
                print(" > Golpe conectado por 5 de daño")

    #Opción 3 Curar
    elif opcion ==3:
        if pociones > 0:
            vida_gladiador += 30
            pociones -= 1
        else:
            print("¡No quedan pociones!" )
            turno_gladiador = False

    vida_gladiador -= ataque_enemigo
    print("¡El enemigo te atacó por 12 puntos de daño!")  

#Mensaje final segun resultado del combate       
if vida_gladiador >0 :
    print(f"¡VICTORIA! {nom_gladiador} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")