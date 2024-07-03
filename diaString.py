### ACÁ IMPORTAMOS TODO LO NECESARIO PARA TRABAJAR, YA SEA JSON, COLORES O DEMÁS BIBLIOTECAS.###
from colorama import just_fix_windows_console
just_fix_windows_console()
from colorama import Fore, Back, Style
import datetime
 
# print('back to normal now')
#APP DE SUEÑO: DREAMLIFY.
#EL USUARIO INGRESA DATOS SOBRE EL DÍA Y SU RUTINA DE SUEÑO.
#LA APP ALMACENA ESOS DATOS CON EL ID "DIA".
#EL USUARIO PUEDE ACCEDER A SUS DATOS DE SUEÑO DEL DÍA.
#LA APP LE DA CONSEJOS DE SUEÑO BASADOS EN LOS DATOS ALMACENADOS DEL DÍA.
#ANTES DE TERMINAR LA CARGA, LE PREGUNTA SI LOS DATOS SON CORRECTOS, Y SINO LE DA LA POSIBILIDAD DE CAMBIARLOS.
#EL USUARIO PUEDE ELIMINAR SUS DATOS DE SUEÑO DEL DÍA INCORRECTOS.

cafe_tomado = 0
ejercicio_antes=0
horas_dormidas=0
suenio_sin_interrumpir=0


def bloquear_sesion():
    print("Sesion bloqueada")
    bloquear_sesion()

# Inicio de sesión
# def iniciar_sesion():
#     intento_inicio_sesion =3
#     while intento_inicio_sesion > 0:
#         usuario = input("Usuario: ")
#         password = input("Contraseña: ")
#         if usuario == "admin" and password == "admin":
#             print("Bienvenido")
#             return
#         else: 
#             intento_inicio_sesion -= 1
#             print("usuario y/o contraseña incorrecta/s")
#             print(intento_inicio_sesion)
#     if intento_inicio_sesion == 0:
#         bloquear_sesion()
# # Fin inicio
# iniciar_sesion()

def enter_para_continuar():
    input("Presione enter para volver al menú...")
 
dias = {"2-8": {'horas_dormidas': 2.0, 'sueño_interrumpido': 2, 'hacer_ejercicio': 2, 'tomar_cafe': 2},
        "2-12": {'horas_dormidas': 7.0, 'sueño_interrumpido': 1, 'hacer_ejercicio': 1, 'tomar_cafe': 1},
        "2-3": {'horas_dormidas': 8.0, 'sueño_interrumpido': 2, 'hacer_ejercicio': 2, 'tomar_cafe': 2},
        "4-4": {'horas_dormidas': 12.0, 'sueño_interrumpido': 1, 'hacer_ejercicio': 1, 'tomar_cafe': 1},
        "20-10": {'horas_dormidas': 12.0, 'sueño_interrumpido': 1, 'hacer_ejercicio': 1, 'tomar_cafe': 1}}
opcion_menu = 0

# convierte las fechas que cargamos, en formato fecha "d-m"
def convertir_fecha(fecha_str):
        return datetime.datetime.strptime(fecha_str, '%d-%m')

fechas_ordenadas = sorted(dias.keys(), key=convertir_fecha)

print(fechas_ordenadas)

# DARLE LA OPCION AL USUARIO DE ELEGIR EL DATO POR EL ID "DIA" Y EN BASE A ESO MOSTRARLE LOS DEMAS DATOS CARGADOS.
# DIA VA DE  1 A 31// HORAS DORMIDAS (FLOAT 8.30)// SUEÑO INTERRUMPIDO INPUT(1 SI, 0 NO, OTRO NUMERO VOLVER A INGRESAR)//
# EJERCICIO ANTES INPUT(1 SI, 0 NO, OTRO NUMERO VOLVER A INGRESAR)//TOMAR CAFE  INPUT(1 SI, 0 NO, OTRO NUMERO VOLVER A INGRESAR)// PRINT DE TODOS LOS DATOS DEL DIA.
while opcion_menu != "0": # True o False
    print(Fore.BLUE + Back.WHITE + "Bienvenido a Dreamlify, la aplicación que mejora tu descanso 😴😴")
    print(Style.RESET_ALL + Fore.BLUE + Back.RED + """
|     Opciones menú                                            |
|      1 - Añadir día                                          |
|      2 - Mostrar todos los días                              |
|      3 - Buscar día                                          |
|      4 - Borrar día                                          |
|      5 - Modificar día                                       |
|      6 - Mostrar consejos                                    |
|      0 - Salir                                               |
""")
    opcion_menu = input(Fore.BLUE + Back.WHITE +"Ingrese una opción: ")
    
    if opcion_menu == "1":
        print(""" 
            - Añadir día 
            - Ingresar horas dormidas.
            - ¿Tu sueño fue interrumpido?
            - ¿Hiciste ejercicio antes de acostarte?
            - ¿Tomaste café antes de acostarte?
              """)
        dia = (input("Ingrese el día que quiere añadir: "))
        
        if dia in dias:
            print("Ese día ya fue agregado.")
            enter_para_continuar()
        else:
            horas_dormidas = float(input("Ingrese las horas dormidas: "))
            suenio_interrumpido = int(input("¿Tu sueño fue interrumpido? (1 por Sí, o 2 por No): "))
            hacer_ejercicio = int(input("¿Hiciste ejercicio antes? (1 por Sí, o 2 por No): "))
            tomar_cafe = int(input("¿Tomaste café antes de acostarte? (1 por Sí, o 2 por No): "))
        
            dias[dia] = {
            'horas_dormidas': horas_dormidas,
            'sueño_interrumpido': suenio_interrumpido,
            'hacer_ejercicio': hacer_ejercicio,
            'tomar_cafe': tomar_cafe
            }
            print(f"Día {dia} agregado correctamente.")
    
    elif opcion_menu == "2":
        print("Mostrando todos los días...")
        #la funcion sorted() lo que hace es ordenar de menor a mayor, con esto, logramos que el orden de los días, al mostrarlos sea de menor a mayor, sin importar el orden en que fueron cargados
        for fecha in fechas_ordenadas:
            datos = dias[fecha]
            horas_dormidas = datos['horas_dormidas']
            sueño_interrumpido = datos['sueño_interrumpido']
            hacer_ejercicio = datos['hacer_ejercicio']
            tomar_cafe = datos['tomar_cafe']
            print(f"""
            🙍‍♂️🙍‍♀️ Datos del día: {fecha} 🙍‍♂️🙍‍♀️
            Horas dormidas: {horas_dormidas}
            Sueño interrumpido: {"Sí" if {sueño_interrumpido} == 1 else "No" }
            Hiciste ejercicio: {"Sí" if {hacer_ejercicio} == 1 else "No"}
            Tomaste café: {"Sí" if tomar_cafe == 1 else "No"}
            """)
            print("-"*40)
        enter_para_continuar()
        
    elif opcion_menu == "3":
        print("Buscando día...")
        buscar_dia = (input("Ingrese un día a buscar: (d-m) "))
        if buscar_dia in dias.keys(): # esto es para filtrar
            datos = dias[buscar_dia]
            print(f""" 
            🙍‍♂️🙍‍♀️ Datos del día: {buscar_dia} 🙍‍♂️🙍‍♀️
            Horas dormidas: {datos["horas_dormidas"]}
            Sueño interrumpido: {"Sí" if datos["sueño_interrumpido"] == 1 else "No"}
            Hiciste ejercicio: {"Sí" if datos["hacer_ejercicio"] == 1 else "No"}
            Tomaste café: {"Sí" if datos["tomar_cafe"] == 1 else "No"}
            """)
            print("Mostrando tips...")
            if datos["horas_dormidas"] <= 5:
                print("Descansaste menos de 5hs. ¿A eso llamas descansar? dormir poco afecta a tu salud.")
            elif datos["horas_dormidas"] >= 6 and datos["horas_dormidas"] < 8:
                print(f"Dormiste {datos["horas_dormidas"]}hs, lo justo y necesario, un poquito más y quedás fresco como una lechuga")
            elif datos["horas_dormidas"] ==8:
                print(f"¡¡¡Dormiste {datos["horas_dormidas"]}hs, felicitaciones!!!")
            else:
                print(f"Dormiste {datos["horas_dormidas"]}hs, son demasiadas")
                
            if datos["tomar_cafe"] ==1:
                print("Consumir café antes de dormir puede afectar tu descanso.")
            
            if datos["hacer_ejercicio"] ==1:
                print("Hacer ejercicio antes de dormir puede afectar tu descanso, es preferible elegir otro horario.")
                
            if datos["sueño_interrumpido"] ==1:
                print("Tu sueño fue interrumpido, eso puede afectar tu descanso general.")
            print("-"*40)  
            enter_para_continuar()
        else:
            print("Ese día no fue agregado.")
            enter_para_continuar()
    elif opcion_menu == "4":
        dia_a_eliminar = (input("Ingrese el día que quiere borrar: (d-m) "))
        if dia_a_eliminar in dias:
            del dias[dia_a_eliminar]
            print("Día eliminado")
            enter_para_continuar()
        else:
            print("Ese día no ha sido guardado.")
            enter_para_continuar()
        
    elif opcion_menu == "5":
        dia_a_modificar = (input("Ingrese el día que desea modificar: (d-m) "))
        if dia_a_modificar in dias:
            print("¿Qué desea modificar?")
            print("1. Horas dormidas")
            print("2. Sueño interrumpido")
            print("3. Hacer ejercicio")
            print("4. Tomar café")
            opcion_modificar = int(input("Ingrese la opción: "))
            
            #modificamos las horas dormidas
            if opcion_modificar == 1:
                horas_dormidas = float(input("Ingrese las horas dormidas: "))
                dias[dia_a_modificar]["horas_dormidas"] = horas_dormidas
            
            #modificamos la interrupcion del sueño
            elif opcion_modificar == 2:
                sueño_interrumpido = int(input("¿Sueño interrumpido? 1. Sí 2. No: "))
                if sueño_interrumpido == 1:
                    dias[dia_a_modificar]["sueño_interrumpido"] = 1
            
            #modificamos el haber hecho ejercicio
            elif opcion_modificar == 3:
                hacer_ejercicio = int(input("¿Hiciste ejercicio? 1. Sí 2. No: "))
                if hacer_ejercicio == 1:
                    dias[dia_a_modificar]["hacer_ejercicio"] = 1
            
            #modificamos el tomar café
            elif opcion_modificar == 4:
                tomar_cafe = int(input("¿Tomaste café? 1. Sí 2: "))
                if tomar_cafe == 1:
                    dias[dia_a_modificar]["tomar_cafe"] = 1
        if dia_a_modificar not in dias:
            print("No guardaste datos de ese día.")

        else:    
            enter_para_continuar()  
        
    elif opcion_menu == "6":
    
        print("Mostrando tips...")
        for dia, datos in dias.items():
            print(f" 🙍‍♂️🙍‍♀️ Tips para el día: {dia} 🙍‍♂️🙍‍♀️")
            if datos["horas_dormidas"] <= 5:
                print("Descansaste menos de 5hs. ¿A eso llamas descansar? dormir poco afecta a tu salud.")
            elif horas_dormidas >= 6 and horas_dormidas <= 7:
                print(f"Dormiste {datos["horas_dormidas"]}hs, lo justo y necesario, un poquito más y quedás fresco como una lechuga")
            else:
                print(f"Dormiste {datos["horas_dormidas"]}hs, son demasiadas")
                
            if datos["tomar_cafe"] ==1:
                print("Consumir café antes de dormir puede afectar tu descanso.")
            
            if datos["hacer_ejercicio"] ==1:
                print("Hacer ejercicio antes de dormir puede afectar tu descanso, es preferible elegir otro horario.")
                
            if datos["sueño_interrumpido"] ==1:
                print("Tu sueño fue interrumpido, eso puede afectar tu descanso general.")
                
            print("-"*40)
        enter_para_continuar()
    elif opcion_menu=="8":
        print (dias)

    else:
        print("Opción incorrecta.")
        enter_para_continuar()

    if opcion_menu == "0":
        print("Gracias por usar Dreamlify.")
        break        