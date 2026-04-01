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