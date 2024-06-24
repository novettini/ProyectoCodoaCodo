import tkinter as tk
from tkinter import *
from tkinter.messagebox import *
import mariadb

root= Tk()
root.title("Dreamlify, tu app de sueño")
root.minsize(375, 500)
root.resizable(False,True)
root.configure(background="#58D68D")
root.iconbitmap("dreammify.jpeg")



try:
    conexion = mariadb.connect(
            user = "root",
            password = "",
            host = "127.0.0.1",
            port=3306,
            database="dreamlify"
    )
    cursor = conexion.cursor()
    print(f"Conectando correctamente a la base de datos: {conexion.database}")
except mariadb.Error as e:
    print(f"Error conectando a la base de datos: {e}")
      

def nueva_ventana():
    ventana_secundaria= Toplevel()
    ventana_secundaria.minsize(375, 500)
    ventana_secundaria.resizable(False,True)
    
    Label(ventana_secundaria, text="Dia").pack()
    e_dia= Entry(ventana_secundaria)
    e_dia.pack()
            
    Label(ventana_secundaria, text="Horas dormidas").pack()
    e_horas= Entry(ventana_secundaria)
    e_horas.pack()
            
    Label(ventana_secundaria, text="Interrupcion").pack()
    e_interrumpido= Entry(ventana_secundaria)
    e_interrumpido.pack()

    Label(ventana_secundaria, text="Ejercicio antes").pack()
    e_ejercicio= Entry(ventana_secundaria)
    e_ejercicio.pack()  
                
    Label(ventana_secundaria, text="Cafe antes").pack()
    e_cafe= Entry(ventana_secundaria)
    e_cafe.pack()     
    boton= Button(ventana_secundaria, text="cargar datos",command=lambda: agregar_dia())
    boton.pack()

             
    def agregar_dia():
            dia = e_dia.get()
            horas = e_horas.get()   
            interrumpido = e_interrumpido.get()
            ejercicio= e_ejercicio.get()
            cafe= e_cafe.get()
            try:
                cursor.execute("INSERT INTO datos_del_dia"
                            "(dia, horas_dormidas, suenio_interrumpido, cafe_tomado, ejercicio_antes) "
                                "VALUES (?,?,?,?,?)",
                                (dia,horas, interrumpido, ejercicio, cafe))
                conexion.commit()
                print("cargados a la bd")
            except mariadb.Error as error_registro:
                print(f"Error al registrar: {error_registro}")     





def ventana_borrar_datos():
    borrar_datos= Toplevel()
    borrar_datos.minsize(375, 500)
    borrar_datos.resizable(False,True)
    
    Label(borrar_datos, text="Dia a borrar").pack()
    e_dia= Entry(borrar_datos)
    e_dia.pack()
            
    boton= Button(borrar_datos, text="borrar datos",command=lambda: eliminar_datos())
    boton.pack()

             
    def eliminar_datos():
            dia = e_dia.get()
            try:
                cursor.execute(f"""DELETE FROM datos_del_dia WHERE dia= {dia}""")
                conexion.commit()
                print("borrado de la bd")
            except mariadb.Error as error_eliminando:
                print(f"Error al borrar: {error_eliminando}")     

            







def advertencia_borrado():
    askquestion(message=f"esta por borrar los datos del día{"dia"}", title="ADVERTENCIA")

def salir():
    askquestion(message=f"¿Desea cerrar el programa?", title="Dreamlify")

def añadir_dia():
    print("Bienvenido a Dreamlify, la aplicación que mejora tu descanso 😴😴")
    print(""" Opciones menú
          0 - Salir
          1 - Añadir día
          2 - Listar días
          3 - Buscar día
          4 - Borrar día
          5 - Modificar día
          """)
    Text=(""" 
            - Añadir día (1 - 31)
            - Ingresar horas dormidas. (float)
            - ¿Tu sueño fue interrumpido?
            - ¿Hiciste ejercicio antes de acostarte?
            - ¿Tomaste café antes de acostarte?
              """),
    

    # #MUESTRA UN ALERT
    # showinfo("Añadir día", Text)
    # #----------------

    # ventana_nueva= Label(root, background="red", text=f"Se almacenó {añadir_dia(dia)} correctamente")
    # ventana_nueva.pack()                     
                                           
    # dias[dia] = {
    #         'horas_dormidas': horas_dormidas,
    #         'sueño_interrumpido': suenio_interrumpido,
    #         'hacer_ejercicio': hacer_ejercicio,
    #         'tomar_cafe': tomar_cafe
    #         }

# PARA EL INICIO DE SESIÓN#
# entrada = Entry(root, width=80, bg="grey" )
# entrada.insert(0, "Ingrese su nombre de usuario")
# entrada.grid(row=0, column=0)
# entrada2 = Entry(root, width=80, bg="grey", show="*" )
# entrada2.insert(0, "Ingrese su nombre de usuario")
# entrada2.grid(row=1, column=0)

# # BOTON PARA ENVIAR LOS DATOS#
# def click_boton():
#     texto = Label(root, text=f"Se almacenó {entrada.get()} correctamente").grid(row=1, column=0)
# boton1 = Button (root, text="enviar", bg="red", width=80, pady=25, command=click_boton).grid(row=2, column=0)

# FIN DEL INICIO#


# x= IntVar()

# def actualiza(value):
#     opcion_set = Label(root, text=value)


titulo = Label(root, text="""Bienvenido a Dreamlify, 
               la aplicación que mejora tu descanso 😴😴
               seleccione una opcion:""")
titulo.pack()
opcion_1= Button(root, text="Añadir día",command=nueva_ventana).pack()
opcion_2= Button(root, text="Listar días").pack()
opcion_3= Button(root, text="Buscar día").pack()
opcion_4= Button(root, text="Borrar día", command=ventana_borrar_datos).pack()
opcion_5= Button(root, text="Modificar día").pack()
opcion_0= Button(root, text="Salir",command=lambda:(salir())).pack()




# PARA PODER CREAR UNO DEBAJO DEL OTRO
# opciones = [["añadir día", "1"],
#           ["Listar días" ,"2"],
#           ["Buscar día", "3"],
#           ["Borrar día", "4"],
#           ["Modificar día", "5"],
#             ["salir", "0"]]

# menu_inicio= StringVar()
# menu_inicio.set("Seleccione una opción")

# for opcion, valor in opciones:
#     Button(root, text=opcion, variable=menu_inicio, value=valor).pack(anchor=NW)
# boton_muestra = Button(root, text="Siguiente", command=lambda :actualiza(menu_inicio.get())).pack()
## FIN MOSTAR DEBAJO DEL OTRO



# boton_borrado = Button(root, text="borrado", command=advertencia_borrado()).pack()


root.mainloop()