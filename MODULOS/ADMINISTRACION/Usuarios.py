#Usuarios
from MENU.Datos import guardar_datos, cargar_datos
import json

RUTA_CLIENTE = "MODULOS/ADMINISTRACION/Usuarios.json"
datos = cargar_datos(RUTA_CLIENTE)

def cargar_usuarios():
    try:
        return cargar_datos("MODULOS/ADMINISTRACION/Usuarios.json")
    except FileNotFoundError:
        return []
    except Exception as e:
        # Captura cualquier excepción y maneja el error aquí
        print("Ha ocurrido un error:", e)
    
    
def guardar_usuarios(usuarios):
    guardar_datos(usuarios, "MODULOS/ADMINISTRACION/Usuarios.json")
        

def agregar_usuario(nuevo_usuario):
    usuarios = dict(cargar_usuarios())
    usuarios["Usuarios"].append(nuevo_usuario)
    guardar_datos(usuarios, "MODULOS/ADMINISTRACION/Usuarios.json")

def obtener_usuario_por_identificacion(identificacion):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["Identificacion"] == int(identificacion):
            return usuario
    return None

def Actualizar_usuarios(datos):
    datos=dict(datos)
    Identificacion = int(input("Ingrese el numero de identificación del usuario que desea actualizar "))
    for i in range(len(datos["Usuarios"])):
        if datos["Usuarios"][i]["Identificacion"] == Identificacion:

            while True:
                print("(1) Actualizar el nombre: ")
                print("(2) Actualizar la dirección: ")
                print("(3) Actualizar el telefono: ")
                print("(4) Actializar la categoria: ")
                print("(5) Actualizar la identificación: ")
                print("(6) Actualizar los servicios utilizados: ")
                

                print("(7) salir ")
                opc=input("ingrese la opcion: ")
                


                if opc=="1":
                    datos["Usuarios"][i]["Nombre"]= input("ingrese el nombre nuevo: ")
                    print("Guardado exitosamente")
                    print("----------------------------------")


                elif opc== "2":
                    datos["Usuarios"][i]["Direccion"]=str(input("ingrese la direccion nueva: "))
                    print("Guardado exitosamente")
                    print("----------------------------------")

                elif opc=="3":
                    datos["Usuarios"][i]["Telefono"]=int(input("ingrese el telefono nuevo: "))
                    print("Guardado exitosamente")
                    print("----------------------------------")

                elif opc=="4":
                    datos["Usuarios"][i]["Categoria"]=input("ingrese la categoria nueva: ")
                    print("Guardado exitosamente")
                    print("----------------------------------")
                
                elif opc=="5":
                    datos["Usuarios"][i]["Identificacion"]=input("ingrese la nueva identificacion: ")
                    print("Guardado exitosamente")
                    print("----------------------------------")
                    
                elif opc=="6":
                    datos["Usuarios"][i]["Servicios_utilizados"]= str(input("ingrese los nuevos servicios utilizados: "))
                    print("Guardado exitosamente")
                    print("----------------------------------")

                elif opc=="7":
    
                    break
            break
    return datos

def agregar_usuario(nuevo_usuario):
    usuarios = cargar_usuarios()
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios, "MODULOS/ADMINISTRACION/Usuarios.json")
    
def eliminar_producto(nombre, archivo):
    datos = cargar_datos(archivo)
    if datos and nombre in datos["Productos"].values():
        productos_actualizados = {}
        eliminado = False

        for key, value in datos["Productos"].items():
            if value != nombre:
                productos_actualizados[key] = value
            else:
                eliminado = True

        if eliminado:
            datos["Productos"] = productos_actualizados
            guardar_datos(datos, archivo)
            return True
    
    return False

def agregar_informacion_administrador():
    nombre_usuario = {}
    nombre_usuario["nombre"] = input("Nombre: ")
    nombre_usuario["direccion"] = input("Dirección: ")
    nombre_usuario["telefono"]= input("Teléfono: ")
    nombre_usuario["categoria"] = input("Categoría: ")
    nombre_usuario["identificacion"] = input("Identificación: ")
    nombre_usuario["servicios_utilizados"] = list(input("Servicios utilizados (separados por comas): ").split(","))

    agregar_usuario(nombre_usuario)
    print("Información del usuario agregada exitosamente.")


def menu_usuarios():
    r = -1
    print("Bienvenido")
    print("Seleccione qué desea hacer: ")
    while r != 0:
        print("Escriba 1 para agregar un usuario.")
        print("Escriba 2 para actualizar la información de un usuario.")
        print("Escriba 3 para eliminar un usuario.")
        print("Escriba 4 para salir al menú principal de administrador.")
        r = int(input("-> "))
        if r == 1:
            agregar_informacion_administrador()
        elif r == 2:
            Actualizar_usuarios(datos)
        elif r == 3:
            eliminar_producto()
        elif r == 4:
            break
   