##APP DE COMIDA//TURNOS
##EL USUARIO INGRESA Y PUEDE ELEGIR EN DISTINTOS MENÚS // EL USUARIO PUEDE ELEGIR PROFESIONES
##PUEDE AGREGARLOS A UN CARRITO DE COMPRA // PUEDE APUNTAR LA FECHA
##PUEDE FINALIZAR LA COMPRA // FINALIZA DE RESERVAR EL TURNO  

#definir variables
USUARIO_DB = "admin"
PASSWORD_DB = "admin"
# horas_dormidas = 0
# sueño_interrumpido = True
# ejercicio_antes = False
# tomar_cafe = False
# opcion_menu = str()






#
def iniciar_sesion():
    intento_inicio_sesion =3
    while intento_inicio_sesion > 0:
        usuario = input("Usuario: ")
        password = input("Contraseña: ")
        if usuario == "admin" and password == "admin":
            print("Bienvenido")
            return
        else: print("usuario y/o contraseña incorrecta/s")
        intento_inicio_sesion = -1
iniciar_sesion()    



# * Agregar datos:
# ● Listar datos:
# ● Buscar datos:
# ● Eliminar datos:
def horas_de_sueño():
    print(f"dormiste {horas_dormidas}hs")

def interrupcion_del_sueño():
    print("Mostrando dato ingresado...")

def ejercicio_antes_de_dormir ():
    print("Mostrando dato ingresado...")

def cafe_antes_de_dormir ():
    print("Mostrando dato ingresado...")





#  DE ESTA MANERA SE CARGAN TODOS
# Asignacion de variables
print("""Bienvenido a Dreamlify, la aplicación que mejora tu descanso 😴😴

    1 - Ingresar horas dormidas
    2 - ¿tu sueño fue interrumpido?
    3 - ¿Hiciste ejercicio antes de acostarte?
    4 - ¿Tomaste café antes de acostarte?
""")
# 

# Logica del programa, carga de datos
horas_dormidas = int(input("Ingrese las horas dormidas"))
sueño_interrumpido = int(input('Ingrese 1 sí su sueño fue interrumpido'))
ejercicio_antes = int(input('Ingrese 1 sí realizó ejercicio'))
tomar_cafe = int(input('Ingrese 1 sí tomó café'))
# print("eliminando datos...")


#mostrar datos
print("¿Qué dato estas buscando?")
opcion_menu = input("""
    1 - ¿Horas dormidas?
    2 - ¿Tu sueño fue interrumpido?
    3 - ¿Hiciste ejercicio antes de acostarte?
    4 - ¿Tomaste café antes de acostarte?
    5 - Eliminar datos ingresados
""")

if opcion_menu == "1":
    print("Sus Horas dormidas fueron: ", horas_dormidas, "hs")
elif opcion_menu == "2":
    if sueño_interrumpido ==1:
        sueño_interrumpido= "sí"
    else: sueño_interrumpido = "no"    
    print("¿Su sueño ", sueño_interrumpido, "fue interrumpido")
elif opcion_menu == "3":
    if ejercicio_antes ==1:
        ejercicio_antes= "sí"
    else: ejercicio_antes = "no"
    print("usted ", ejercicio_antes, " realizó ejercicio antes de dormir")
elif opcion_menu == "4":
    if tomar_cafe ==1:
        tomar_cafe= "sí"
    else: tomar_cafe = "no"
    print("Usted ", tomar_cafe, "tomó café")
else:
    print("hasta luego")
