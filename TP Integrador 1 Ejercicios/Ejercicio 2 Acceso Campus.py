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