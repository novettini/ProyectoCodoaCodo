### ACÁ IMPORTAMOS TODO LO NECESARIO PARA TRABAJAR, YA SEA JSON, COLORES O DEMÁS BIBLIOTECAS.###
import json
from colorama import just_fix_windows_console
just_fix_windows_console()
from colorama import Fore, Back, Style

# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background' + Style.RESET_ALL)
# # print(Style.RESET_ALL)
# print('back to normal now')
#APP DE SUEÑO: DREAMLIFY.
#EL USUARIO INGRESA DATOS SOBRE EL DÍA Y SU RUTINA DE SUEÑO.
#LA APP ALMACENA ESOS DATOS CON EL ID "DIA".
#EL USUARIO PUEDE ACCEDER A SUS DATOS DE SUEÑO DEL DÍA.
#LA APP LE DA CONSEJOS DE SUEÑO BASADOS EN LOS DATOS ALMACENADOS DEL DÍA.
#ANTES DE TERMINAR LA CARGA, LE PREGUNTA SI LOS DATOS SON CORRECTOS, Y SINO LE DA LA POSIBILIDAD DE CAMBIARLOS.
#EL USUARIO PUEDE ELIMINAR SUS DATOS DE SUEÑO DEL DÍA INCORRECTOS.

dias_db= open("dia_db.json","r")
base_datos = json.load(dias_db)
dias_db.close()
print(base_datos)

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
 
dias = {2: {"mes":8 ,'horas_dormidas': 2.0, 'sueño_interrumpido': 2, 'hacer_ejercicio': 2, 'tomar_cafe': 2},
        2: {"mes":6 ,'horas_dormidas': 2.0, 'sueño_interrumpido': 2, 'hacer_ejercicio': 2, 'tomar_cafe': 2},
        1: {"mes": 7,'horas_dormidas': 1.0, 'sueño_interrumpido': 1, 'hacer_ejercicio': 1, 'tomar_cafe': 1},
        3: {"mes": 9, 'horas_dormidas': 2.0, 'sueño_interrumpido': 2, 'hacer_ejercicio': 2, 'tomar_cafe': 2},
        44: {"mes": 8,'horas_dormidas': 1.0, 'sueño_interrumpido': 1, 'hacer_ejercicio': 1, 'tomar_cafe': 1}}
opcion_menu = 0

# DARLE LA OPCION AL USUARIO DE ELEGIR EL DATO POR EL ID "DIA" Y EN BASE A ESO MOSTRARLE LOS DEMAS DATOS CARGADOS.
# DIA VA DE  1 A 31// HORAS DORMIDAS (FLOAT 8.30)// SUEÑO INTERRUMPIDO INPUT(1 SI, 0 NO, OTRO NUMERO VOLVER A INGRESAR)//
# EJERCICIO ANTES INPUT(1 SI, 0 NO, OTRO NUMERO VOLVER A INGRESAR)//TOMAR CAFE  INPUT(1 SI, 0 NO, OTRO NUMERO VOLVER A INGRESAR)// PRINT DE TODOS LOS DATOS DEL DIA.
while opcion_menu != "0": # True o False
    print("Bienvenido a Dreamlify, la aplicación que mejora tu descanso 😴😴")
    print(""" Opciones menú
          1 - Añadir día
          2 - Mostrar todos los días
          3 - Buscar día
          4 - Borrar día
          5 - Modificar día
          0 - Salir
        """)
    opcion_menu = input("Ingrese una opción: ")
    
    if opcion_menu == "1":
        print(""" 
            - Añadir día (1 - 31)
            - Ingresar mes: (0-12)  
            - Ingresar horas dormidas. (float)
            - ¿Tu sueño fue interrumpido?
            - ¿Hiciste ejercicio antes de acostarte?
            - ¿Tomaste café antes de acostarte?
              """)
        dia = int(input("Ingrese el día que quiere añadir: "))
        mes = int(input("Ingrese el mes que quiere añadir: "))
    
    # Verificar si el día y el mes ya existen en el diccionario
        if dia in dias and dias[dia]['mes'] == mes:
            print("Ese día ya fue agregado.")
        else:
            horas_dormidas = float(input("Ingrese las horas dormidas: "))
            suenio_interrumpido = int(input("¿Tu sueño fue interrumpido? (1 por Sí, o 2 por No): "))
            hacer_ejercicio = int(input("¿Hiciste ejercicio antes? (1 por Sí, o 2 por No): "))
            tomar_cafe = int(input("¿Tomaste café antes de acostarte? (1 por Sí, o 2 por No): "))
            
            dias[dia] = {
            "mes": mes,
            'horas_dormidas': horas_dormidas,
            'sueño_interrumpido': suenio_interrumpido,
            'hacer_ejercicio': hacer_ejercicio,
            'tomar_cafe': tomar_cafe
        }
            print(f"Día {dia} del mes {mes} agregado correctamente.")
    
    elif opcion_menu == "2":
        # mes_elegido= input("ingrese el mes a buscar (1-12)")
        print("Mostrando todos los días...")
        #la funcion sorted() lo que hace es ordenar de menor a mayor, con esto, logramos que el orden de los días, al mostrarlos sea de menor a mayor, sin importar el orden en que fueron cargados
        
        for dia, datos in sorted(dias.items()):
            print(f""" 🙍‍♂️🙍‍♀️ Datos del día: {dia}/{datos["mes"]} 🙍‍♂️🙍‍♀️
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
            buscar_mes= int(input("Ingrese el mes que quiere buscar: "))
            
            if buscar_mes in {datos["mes"]}:
            
                print(f""" 🙍‍♂️🙍‍♀️ Datos del dia: {buscar_dia}/{datos["mes"]} 🙍‍♂️🙍‍♀️
                Horas dormidas: {datos["horas_dormidas"]}
                Sueño interrumpido: {"Sí" if datos["sueño_interrumpido"] == 1 else "No"}
                Hiciste ejercicio: {"Sí" if datos["hacer_ejercicio"] == 1 else "No"}
                Tomaste café: {"Sí" if datos["tomar_cafe"] == 1 else "No"}
                """)
                print("-"*40)  
            else:
                print("El día no existe en el mes que ingresaste.")
        enter_para_continuar()
    
    elif opcion_menu == "4":
        dia_a_eliminar = int(input("Ingrese el día que quiere borrar: "))
        if dia_a_eliminar in dias:
            datos = dias[dia_a_eliminar]
            mes_a_eliminar = int(input("Ingrese el mes que quiere borrar: "))
            if mes_a_eliminar in {datos["mes"]}:
                del dias[dia_a_eliminar]
                print("Día eliminado")
                enter_para_continuar()
            else:
                print("Ese día no ha sido guardado.")
            enter_para_continuar()

        else:
            print("Ese día no ha sido guardado.")
            enter_para_continuar()
            
    elif opcion_menu == "5":
        dia_a_modificar = int(input("Ingrese el día que desea modificar: "))
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

        print("¿Querés moficar un día mas?")
        opcion_menu = input(f"""
                            1 para Sí.
                            2 para No. """)
        if opcion_menu == 1:
            dia_a_modificar
        else:    
            enter_para_continuar()  
        
    elif opcion_menu == "6":
    
        for dia, datos in dias.items():
            if (datos["tomar_cafe"] == 1):
                cafe_tomado +=1
            if (datos["tomar_cafe"] == 2):
                cafe_tomado -=1
        if cafe_tomado>1:
            print(f"""Has tomado café en {cafe_tomado} días.
                    El consumo elevado de café es perjudicial para la salud""")
        if cafe_tomado==0:
            print(f"""Has tomado café en {cafe_tomado} días.
                    estás bien, podria ser mejor, pero venis bien, dale bajá el consumo""")
        if cafe_tomado<1:
            print(f"""Has tomado café menos días antes de dormir.
                    Felicitaciones, segui sin consumir café""")        
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

    