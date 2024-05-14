#Usuarios
from MENU.Datos import guardar_datos
import json

def cargar_usuarios():
    try:
        with open('MODULOS/ADMINISTRACION/Usuarios.json', 'r') as file:
           datos = json.load(file)
        return datos
    except FileNotFoundError:
        return []
    
def guardar_usuarios(usuarios):
    guardar_datos(usuarios, "MODULOS/ADMINISTRACION/Usuarios.json")
        

def agregar_usuario(nuevo_usuario):
    usuarios = cargar_usuarios()
    print(usuarios)
    usuarios.append(nuevo_usuario)
    guardar_datos(usuarios)

    
def obtener_usuario_por_identificacion(identificacion):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["Identificacion"] == int(identificacion):
            return usuario
    return None

def actualizar_usuario(identificacion_usuario, datos_actualizados):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["Identificacion"] == identificacion_usuario:
            usuario.update(datos_actualizados)
            guardar_usuarios(usuarios)
            return True
    return False

def eliminar_usuario(identificador_usuario):
    usuarios = cargar_usuarios()
    usuarios_actualizados = [usuario for usuario in usuarios if usuario["Identificacion"] != identificador_usuario]
    if len(usuarios_actualizados) != len(usuarios):
        guardar_usuarios(usuarios_actualizados)
        return True
    return False

def agregar_informacion_administrador():
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    categoria = input("Categoría: ")
    identificacion = input("Identificación: ")
    servicios_utilizados = input("Servicios utilizados (separados por comas): ").split(",")

    nuevo_usuario = {
        "Nombre": nombre,
        "Direccion": direccion,
        "Telefono": telefono,
        "Categoria": categoria,
        "Identificacion": int(identificacion),
        "Servicios utilizados": servicios_utilizados
    }

    agregar_usuario(nuevo_usuario)
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
            actualizar_usuario()
        elif r == 3:
            eliminar_usuario()
        elif r == 4:
            break
   