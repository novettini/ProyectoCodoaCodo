### ACÁ IMPORTAMOS TODO LO NECESARIO PARA TRABAJAR, YA SEA JSON, COLORES O DEMÁS BIBLIOTECAS.###
from colorama import just_fix_windows_console
just_fix_windows_console()
from colorama import Fore, Back, Style


# print('back to normal now')
#APP DE SUEÑO: DREAMLIFY.
#EL USUARIO INGRESA DATOS SOBRE EL DÍA Y SU RUTINA DE SUEÑO.
#LA APP ALMACENA ESOS DATOS CON EL ID "DIA".
#EL USUARIO PUEDE ACCEDER A SUS DATOS DE SUEÑO DEL DÍA.
#LA APP LE DA CONSEJOS DE SUEÑO BASADOS EN LOS DATOS ALMACENADOS DEL DÍA.
#ANTES DE TERMINAR LA CARGA, LE PREGUNTA SI LOS DATOS SON CORRECTOS, Y SINO LE DA LA POSIBILIDAD DE CAMBIARLOS.
#EL USUARIO PUEDE ELIMINAR SUS DATOS DE SUEÑO DEL DÍA INCORRECTOS.


def bloquear_sesion():
    print(f"{Fore.RED}🚫Sesion bloqueada🚫")
    bloquear_sesion()

# Inicio de sesión
def iniciar_sesion():
    intento_inicio_sesion =3
    while intento_inicio_sesion > 0:
        usuario = input(f" {Fore.YELLOW}•{Style.RESET_ALL} {Style.BRIGHT}Usuario: {Style.RESET_ALL} ")
        password = input(f" {Fore.YELLOW}•{Style.RESET_ALL} {Style.BRIGHT}Contraseña: {Style.RESET_ALL} ")
        if usuario == "admin" and password == "admin":
            return
        else: 
            intento_inicio_sesion -= 1
            print(f"{Fore.RED}🚫 Usuario o contraseña incorrecta. 🚫{Style.RESET_ALL}")
            print(f"{Fore.RED} {'-' *40}")
    if intento_inicio_sesion == 0:
        bloquear_sesion()
# Fin inicio
iniciar_sesion()

def enter_para_continuar():
    input(f"Presione {Style.BRIGHT}enter{Style.RESET_ALL} para volver al menú...  ")

dias = {2: {'horas_dormidas': 2.0, 'sueño_interrumpido': 2, 'hacer_ejercicio': 2, 'tomar_cafe': 2},
        1: {'horas_dormidas': 7.0, 'sueño_interrumpido': 1, 'hacer_ejercicio': 1, 'tomar_cafe': 1},
        3: {'horas_dormidas': 8.0, 'sueño_interrumpido': 2, 'hacer_ejercicio': 2, 'tomar_cafe': 2},
        44: {'horas_dormidas': 12.0, 'sueño_interrumpido': 1, 'hacer_ejercicio': 1, 'tomar_cafe': 1}}
opcion_menu = 0

# DARLE LA OPCION AL USUARIO DE ELEGIR EL DATO POR EL ID "DIA" Y EN BASE A ESO MOSTRARLE LOS DEMAS DATOS CARGADOS.
# DIA VA DE  1 A 31// HORAS DORMIDAS (FLOAT 8.30)// SUEÑO INTERRUMPIDO INPUT(1 SI, 0 NO, OTRO NUMERO VOLVER A INGRESAR)//
# EJERCICIO ANTES INPUT(1 SI, 0 NO, OTRO NUMERO VOLVER A INGRESAR)//TOMAR CAFE  INPUT(1 SI, 0 NO, OTRO NUMERO VOLVER A INGRESAR)// PRINT DE TODOS LOS DATOS DEL DIA.
while opcion_menu != "0": # True o False
    print(Fore.WHITE + f"""
⭐️  Bienvenido a {Style.BRIGHT + Fore.BLUE}Dreamlify{Style.RESET_ALL}{Fore.WHITE}, la aplicación que mejora tu descanso 😴💤{Style.RESET_ALL}""")
    print(Style.RESET_ALL + Fore.BLUE + f"""
        ┌───────────────────────────────┐
        |    {Style.BRIGHT}Opciones menú:{Style.RESET_ALL}{Fore.BLUE}             |
        |   {Style.BRIGHT}1 -{Style.RESET_ALL} {Fore.WHITE}Añadir día{Style.RESET_ALL}{Fore.BLUE}              |
        |   {Style.BRIGHT}2 -{Style.RESET_ALL} {Fore.WHITE}Mostrar todos los días{Style.RESET_ALL}{Fore.BLUE}  |
        |   {Style.BRIGHT}3 -{Style.RESET_ALL} {Fore.WHITE}Buscar día{Style.RESET_ALL}{Fore.BLUE}              |
        |   {Style.BRIGHT}4 -{Style.RESET_ALL} {Fore.WHITE}Borrar día{Style.RESET_ALL}{Fore.BLUE}              |
        |   {Style.BRIGHT}5 -{Style.RESET_ALL} {Fore.WHITE}Modificar día{Style.RESET_ALL}{Fore.BLUE}           |
        |   {Style.BRIGHT}6 -{Style.RESET_ALL} {Fore.WHITE}Mostrar consejos{Style.RESET_ALL}{Fore.BLUE}        |
        |   {Style.BRIGHT}0 -{Style.RESET_ALL} {Fore.WHITE}Salir{Style.RESET_ALL}{Fore.BLUE}                   |
        └───────────────────────────────┘{Style.RESET_ALL}
""")
    opcion_menu = input(Fore.WHITE +"⭐️ Ingrese una opción: ")

    if opcion_menu == "1":
        print(Fore.BLUE + f"""
        ┌──────────────────────────────────────────────┐
        |   • {Fore.WHITE}Añadir día{Style.RESET_ALL}{Fore.BLUE}                               |
        |   • {Fore.WHITE}Ingresar horas dormidas{Style.RESET_ALL}{Fore.BLUE}                  |
        |   • {Fore.WHITE}¿Tu sueño fue interrumpido?{Style.RESET_ALL}{Fore.BLUE}              |
        |   • {Fore.WHITE}¿Hiciste ejercicio antes de acostarte?{Style.RESET_ALL}{Fore.BLUE}   |
        |   • {Fore.WHITE}¿Tomaste café antes de acostarte?{Style.RESET_ALL}{Fore.BLUE}        |
        └──────────────────────────────────────────────┘{Style.RESET_ALL}
              """)
        
        dia = int(input("⭐️ Ingrese el día que quiere añadir: "))

        if dia in dias:
            print(f"{Fore.RED}🚫 Ese día ya fue agregado.{Style.RESET_ALL}")
            enter_para_continuar()
        else:
            horas_dormidas = float(input(f"{Fore.YELLOW}•{Style.RESET_ALL} {Style.BRIGHT}Ingrese las horas dormidas:{Style.RESET_ALL} "))
            suenio_interrumpido = int(input(f"{Fore.YELLOW}•{Style.RESET_ALL} {Style.BRIGHT}¿Tu sueño fue interrumpido?{Style.RESET_ALL} (1 por Sí, o 2 por No): "))
            hacer_ejercicio = int(input(f"{Fore.YELLOW}•{Style.RESET_ALL} {Style.BRIGHT}¿Hiciste ejercicio antes?{Style.RESET_ALL} (1 por Sí, o 2 por No): "))
            tomar_cafe = int(input(f"{Fore.YELLOW}•{Style.RESET_ALL} {Style.BRIGHT}¿Tomaste café antes de acostarte?{Style.RESET_ALL} (1 por Sí, o 2 por No): "))

            dias[dia] = {
            'horas_dormidas': horas_dormidas,
            'sueño_interrumpido': suenio_interrumpido,
            'hacer_ejercicio': hacer_ejercicio,
            'tomar_cafe': tomar_cafe
            }
            print(f"""
                  {Fore.GREEN}Día {dia} agregado correctamente. ✅{Style.RESET_ALL}
                  """)
            enter_para_continuar()

    elif opcion_menu == "2":
        print("Mostrando todos los días...")
        #la funcion sorted() lo que hace es ordenar de menor a mayor, con esto, logramos que el orden de los días, al mostrarlos sea de menor a mayor, sin importar el orden en que fueron cargados
        for dia, datos in sorted(dias.items()):
            print(f"""
        {Fore.BLUE}┌───────────────────────────┐          
          {Fore.BLUE}{Style.BRIGHT} 🌛  Datos del día:{Style.RESET_ALL} {Style.BRIGHT}{dia}{Style.RESET_ALL} 🌜
          {Fore.YELLOW}⋆{Fore.BLUE} Horas dormidas:{Style.RESET_ALL} {datos["horas_dormidas"]}
          {Fore.YELLOW}⋆{Fore.BLUE} Sueño interrumpido:{Style.RESET_ALL} {"Sí" if datos["sueño_interrumpido"] == 1 else "No" }
          {Fore.YELLOW}⋆{Fore.BLUE} Hiciste ejercicio:{Style.RESET_ALL} {"Sí" if datos["hacer_ejercicio"] == 1 else "No"}
          {Fore.YELLOW}⋆{Fore.BLUE} Tomaste café:{Style.RESET_ALL} {"Sí" if datos["tomar_cafe"] == 1 else "No"}{Fore.BLUE}
        └───────────────────────────┘{Style.RESET_ALL}
            """)
            print(f"""{Fore.BLUE}˚★　⋆　✦　☾　☁︎　.　☾　. ⋆ ˚　.　☁︎　 . ✦ . ★ ⋆.˚{Style.RESET_ALL}
                  """)
        enter_para_continuar()

    elif opcion_menu == "3":
        buscar_dia = int(input(f"""
☁︎ {Fore.YELLOW}☾⋆{Style.RESET_ALL} Ingrese un día a buscar: """))
        if buscar_dia in dias.keys(): # esto es para filtrar
            datos = dias[buscar_dia]
            print(f""" 
        {Fore.BLUE}┌─────────────────────────┐
           {Style.BRIGHT + Fore.BLUE}Datos del día: {Style.RESET_ALL} {buscar_dia} ⭐️
        {Fore.BLUE} ─────────────────────────  
           {Fore.BLUE}Horas dormidas:{Style.RESET_ALL} {datos["horas_dormidas"]}
           {Fore.BLUE}Sueño interrumpido:{Style.RESET_ALL} {"Sí" if datos["sueño_interrumpido"] == 1 else "No"}
           {Fore.BLUE}Hiciste ejercicio:{Style.RESET_ALL} {"Sí" if datos["hacer_ejercicio"] == 1 else "No"}
           {Fore.BLUE}Tomaste café:{Style.RESET_ALL} {"Sí" if datos["tomar_cafe"] == 1 else "No"}
        {Fore.BLUE}└─────────────────────────┘{Style.RESET_ALL}
            """)
            print("Mostrando tips para este día...")
            print(" ")
            if datos["horas_dormidas"] <= 5:
                print(f"{Fore.BLUE}•{Style.RESET_ALL} Dormiste {Fore.RED}{datos["horas_dormidas"]}hs{Style.RESET_ALL}. ¿A eso llamas descansar? dormir poco afecta a tu salud. 📉")
            elif datos["horas_dormidas"] >= 6 and datos["horas_dormidas"] <= 7:
                print(f"{Fore.BLUE}•{Style.RESET_ALL} Dormiste {Fore.GREEN}{datos["horas_dormidas"]}hs{Style.RESET_ALL}, lo justo y necesario, un poquito más y quedás fresco como una lechuga. 📈")
            elif datos["horas_dormidas"] ==8:
                print(f"{Fore.BLUE}•{Style.RESET_ALL} ¡¡¡Dormiste {Fore.GREEN}{datos["horas_dormidas"]}hs{Style.RESET_ALL}, felicitaciones!!! 💫 ✅")
            else:
                print(f"{Fore.BLUE}•{Style.RESET_ALL} Dormiste {Fore.RED}{datos["horas_dormidas"]}hs{Style.RESET_ALL}, son demasiadas. 📉")

            if datos["tomar_cafe"] ==1:
                print(f"{Fore.BLUE}•{Style.RESET_ALL} Consumir café antes de dormir puede afectar tu descanso. ☕️❗️")

            if datos["hacer_ejercicio"] ==1:
                print(f"{Fore.BLUE}•{Style.RESET_ALL} Hacer ejercicio antes de dormir puede afectar tu descanso, es preferible elegir otro horario. ⚽️❗️")

            if datos["sueño_interrumpido"] ==1:
                print(f"{Fore.BLUE}•{Style.RESET_ALL} Tu sueño fue interrumpido, eso puede afectar tu descanso general. 🥱❗️")
            print(f"{Fore.BLUE}-{Style.RESET_ALL}"*40)  
            enter_para_continuar()
        else:
            print(f"{Fore.RED}🚫 Ese día no fue agregado.{Style.RESET_ALL}")
            enter_para_continuar()
            
    elif opcion_menu == "4":
        dia_a_eliminar = int(input(f"""
☁︎ {Fore.YELLOW}☾⋆{Style.RESET_ALL} Ingrese el día que quiere eliminar: """))
        if dia_a_eliminar in dias:
            del dias[dia_a_eliminar]
            print(f"{Fore.GREEN}Día eliminado ✅{Style.RESET_ALL}")
            enter_para_continuar()
        else:
            print(f"{Fore.RED}🚫 Ese día no ha sido guardado.{Style.RESET_ALL}")
            enter_para_continuar()

    elif opcion_menu == "5":
        dia_a_modificar = int(input(f"""
☁︎ {Fore.YELLOW}☾⋆{Style.RESET_ALL} Ingrese el día que desea modificar: """))
        if dia_a_modificar in dias:
            print("¿Qué desea modificar? ✏️")
            print(f"{Fore.BLUE}1.{Style.RESET_ALL} Horas dormidas")
            print(f"{Fore.BLUE}2.{Style.RESET_ALL} Sueño interrumpido")
            print(f"{Fore.BLUE}3.{Style.RESET_ALL} Ejercicio antes de dormir")
            print(f"{Fore.BLUE}4.{Style.RESET_ALL} Café antes de dormir")
            opcion_modificar = int(input("Ingrese la opción: "))

            #modificamos las horas dormidas
            if opcion_modificar == 1:
                horas_dormidas = float(input(f"{Fore.BLUE}•{Style.RESET_ALL} Ingrese las horas dormidas: "))
                dias[dia_a_modificar]["horas_dormidas"] = horas_dormidas

            #modificamos la interrupcion del sueño
            elif opcion_modificar == 2:
                sueño_interrumpido = int(input(f"{Fore.BLUE}•{Style.RESET_ALL} ¿Sueño interrumpido? (1.Sí 2.No): "))
                if sueño_interrumpido == 1:
                    dias[dia_a_modificar]["sueño_interrumpido"] = 1

            #modificamos el haber hecho ejercicio
            elif opcion_modificar == 3:
                hacer_ejercicio = int(input(f"{Fore.BLUE}•{Style.RESET_ALL} ¿Hiciste ejercicio? (1.Sí 2.No): "))
                if hacer_ejercicio == 1:
                    dias[dia_a_modificar]["hacer_ejercicio"] = 1

            #modificamos el tomar café
            elif opcion_modificar == 4:
                tomar_cafe = int(input(f"{Fore.BLUE}•{Style.RESET_ALL} ¿Tomaste café? 1. Sí 2. No: "))
                if tomar_cafe == 1:
                    dias[dia_a_modificar]["tomar_cafe"] = 1
            
        if dia_a_modificar not in dias:
            print(f"{Fore.RED}🚫 No guardaste datos de ese día.{Style.RESET_ALL}")
            enter_para_continuar()
            
        else:    
              enter_para_continuar()  
        
    elif opcion_menu == "6":

        print("""Mostrando tips...
              """)
        for dia, datos in dias.items():
            print(f"☁︎ {Fore.YELLOW}☾⋆{Fore.BLUE} {Style.BRIGHT + Fore.BLUE}Tips para el día:{Style.RESET_ALL} {dia}")
            if datos["horas_dormidas"] <= 5:
                print(f"{Fore.BLUE}•{Style.RESET_ALL} Dormiste {Fore.RED}{datos["horas_dormidas"]}hs{Style.RESET_ALL}. ¿A eso llamas descansar? dormir poco afecta a tu salud. 📉")
            elif datos["horas_dormidas"] >= 6 and datos["horas_dormidas"] <= 7:
                print(f"{Fore.BLUE}•{Style.RESET_ALL} Dormiste {Fore.GREEN}{datos["horas_dormidas"]}hs{Style.RESET_ALL}, lo justo y necesario, un poquito más y quedás fresco como una lechuga. 📈")
            elif datos["horas_dormidas"] == 8:
                print(f"{Fore.BLUE}•{Style.RESET_ALL} ¡¡¡Dormiste {Fore.GREEN}{datos["horas_dormidas"]}hs{Style.RESET_ALL}, felicitaciones!!! 💫 ✅")
            else:
                print(f"{Fore.BLUE}•{Style.RESET_ALL} Dormiste {Fore.RED}{datos["horas_dormidas"]}hs{Style.RESET_ALL}, son demasiadas. 📉")

            if datos["tomar_cafe"] ==1:
                print(f"{Fore.BLUE}•{Style.RESET_ALL} Consumir café antes de dormir puede afectar tu descanso. ☕️❗️")

            if datos["hacer_ejercicio"] ==1:
                print(f"{Fore.BLUE}•{Style.RESET_ALL} Hacer ejercicio antes de dormir puede afectar tu descanso, es preferible elegir otro horario. ⚽️❗️")

            if datos["sueño_interrumpido"] ==1:
                print(f"{Fore.BLUE}•{Style.RESET_ALL} Tu sueño fue interrumpido, eso puede afectar tu descanso general. 🥱❗️")

            print(f"{Fore.BLUE}-{Style.RESET_ALL}"*100)
        enter_para_continuar()

    else:
        print("💗  Gracias por usar Dreamlify. 💗")
        
        print(f"""
       {Fore.MAGENTA}✿ ⋆｡ ﾟ ☁︎｡⋆｡ ﾟ ☾ ﾟ ｡⋆{Style.RESET_ALL}
              """)
        enter_para_continuar()
        break        