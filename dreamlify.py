# USUARIO = "admin"
# PASSWORD = "admin"

def bloquear_sesion():
    print("Sesion bloqueada")
    bloquear_sesion()

# Inicio de sesión
def iniciar_sesion():
    intento_inicio_sesion =3
    while intento_inicio_sesion > 0:
        usuario = input("Usuario: ")
        password = input("Contraseña: ")
        if usuario == "admin" and password == "admin":
            print("Bienvenido")
        else: 
            intento_inicio_sesion -= 1
            print("usuario y/o contraseña incorrecta/s")
            print(intento_inicio_sesion)
    if intento_inicio_sesion == 0:
        bloquear_sesion()
# Fin inicio
iniciar_sesion()

def enter_para_continuar():
    input("Presione enter para volver al menú...")
 
dias = {}

opcion_menu = 0


while opcion_menu != "0": # True o False
    print("Bienvenido a Dreamlify, la aplicación que mejora tu descanso 😴😴")
    print(""" Opciones menú
          0 - Salir
          1 - Añadir día
          2 - Listar días
          3 - Buscar día
          4 - Borrar día
          5 - Modificar día
          """)
    opcion_menu = input("Ingrese una opción: ")
    
    if opcion_menu == "1":
        print(""" 
            - Añadir día (1 - 31)
            - Ingresar horas dormidas. (float)
            - ¿Tu sueño fue interrumpido?
            - ¿Hiciste ejercicio antes de acostarte?
            - ¿Tomaste café antes de acostarte?
              """)
        
        dia = int(input("Ingrese el día que quiere añadir: "))
        
        if dia in dias:
            print("Ese día ya fue agregado.")
            enter_para_continuar()
        else:
            horas_dormidas = float(input("Ingrese las horas dormidas: "))
            suenio_interrumpido = int(input("¿Tu sueño fue interrumpido? (1 Sí, 2 No): "))
            hacer_ejercicio = int(input("¿Hiciste ejercicio antes? (1 Sí, 2 No): "))
            tomar_cafe = int(input("¿Tomaste café antes de acostarte? (1 Sí, 2 No): "))
        
            dias[dia] = {
            'horas_dormidas': horas_dormidas,
            'sueño_interrumpido': suenio_interrumpido,
            'hacer_ejercicio': hacer_ejercicio,
            'tomar_cafe': tomar_cafe
            }
        
            print(f"Día {dia} agregado correctamente.")
    
    elif opcion_menu == "2":
        print("Listando día...")
        for dia, datos in dias.items():
            print(f""" 🙍‍♂️🙍‍♀️ Datos del día: {dia} 🙍‍♂️🙍‍♀️
            Horas dormidas: {datos["horas_dormidas"]}
            Sueño interrumpido: {"Sí" if datos["sueño_interrumpido"] == 1 else "No" }
            Hiciste ejercicio: {"Sí" if datos["hacer_ejercicio"] == 1 else "No"}
            Tomaste café: {"Sí" if datos["tomar_cafe"] == 1 else "No"}
            """)
            print("-"*40)
        enter_para_continuar()
        
    elif opcion_menu == "3":
        print("Buscando día...")
        buscar_dia = int(input("Ingrese un día a buscar: "))
        if buscar_dia in dias.keys(): # esto es para filtrar
            datos = dias[buscar_dia]
            print(f""" 🙍‍♂️🙍‍♀️ Datos del día: {dia} 🙍‍♂️🙍‍♀️
            Horas dormidas: {datos["horas_dormidas"]}
            Sueño interrumpido: {"Sí" if datos["sueño_interrumpido"] == 1 else "No"}
            Hiciste ejercicio: {"Sí" if datos["hacer_ejercicio"] == 1 else "No"}
            Tomaste café: {"Sí" if datos["tomar_cafe"] == 1 else "No"}
            """)
            print("-"*40)  
        else:
            print("El día no existe.")
            
        enter_para_continuar()
    
    elif opcion_menu == "4":
        dia_a_eliminar = int(input("Ingrese el día que quiere borrar: "))
        if dia_a_eliminar in dias:
            del dias[dia_a_eliminar]
            print("Día eliminado")
            enter_para_continuar()
        else:
            print("Ese día no ha sido guardado.")
            enter_para_continuar()
        
    elif opcion_menu == "5":
        print("Mostrando día...")
        
        
    else:
        print("Opción incorrecta.")
        
    
    if opcion_menu == "0":
        print("Gracias por usar Dreamlify.")
        break