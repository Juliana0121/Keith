import json
import datetime

# Funciones para cargar y guardar datos en archivos JSON
def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def guardar_datos(datos, archivo):
    with open(archivo, 'w') as file:
        json.dump(datos, file, indent=4)

# Funciones para el menú
def menu_principal():
    print("----------------------------------------")
    print("Bienvenido a Claro".center(40))
    print("----------------------------------------")
    print("1. Administración de usuarios ")
    print("2. Administración de servicios ")
    print("3. Ventas ")
    print("4. Reportes")
    print("5. Salir")
    print("----------------------------------------")

def menu_administracion_usuarios():
    print("----------------------------------------")
    print("Administración de usuarios ")
    print("----------------------------------------")
    print("1. Registro y administración de usuarios ")
    print("2. Historial de usuarios ")
    print("3. Personalización de servicios ")
    print("4. Volver al menú principal")
    print("----------------------------------------")

def menu_registro_administracion():
    print("----------------------------------------")
    print("Registro y administración de usuarios ")
    print("----------------------------------------")
    print("1. Registrar cliente ")
    print("2. Actualizar cliente ")
    print("3. Eliminar cliente ")
    print("4. Lista de clientes")
    print("5. Volver al menú de administración de usuarios")
    print("----------------------------------------")

def menu_usuarios():
    r=-1
    print("Bienvenido")
    print("Seleccione que desea hacer: ")
    while r!=0:
        print("Escriba 1 para agregar un usuario. ")
        print("Escriba 2 para actualizar la info de un usuario. ")
        print("Escriba 3 para eliminar un usuario. ")
        print("Escriba 4 para salir al menú principal de administrador. ")
        r=int(input("-> "))
        if r==1:
            agregar_informacion_administrador()
        elif r==2:
            actualizar_usuario()
        elif r==3:
            eliminar_usuario()
        elif r==4:
            break

# Funciones para usuarios
def cargar_usuarios():
    try:
        with open('MODULOS/ADMINISTRACION/Usuarios.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_usuarios(usuarios):
    with open("MODULOS/ADMINISTRACION/Usuarios.json", "w") as file:
        json.dump(usuarios, file, indent=4)

def generar_nuevo_identificador():
    usuarios = cargar_usuarios()
    if not usuarios:
        return 1
    ultimo_identificador = max(usuario["Identificador"] for usuario in usuarios)
    return ultimo_identificador + 1

def agregar_informacion_administrador():
    nuevo_identificador = generar_nuevo_identificador()
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    categoria = input("Categoría: ")
    servicios_utilizados = input("Servicios utilizados (separados por comas): ").split(",")

    nuevo_usuario = {
        "Identificador": nuevo_identificador,
        "Nombre": nombre,
        "Direccion": direccion,
        "Telefono": telefono,
        "Categoria": categoria,
        "Servicios utilizados": servicios_utilizados
    }

    usuarios = cargar_usuarios()
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)

    print("Información del usuario agregada exitosamente.")

# Función principal
def main():
    while True:
        menu_principal()
        opcion = pedir_opcion()
        if opcion == 1:
            while True:
                menu_administracion_usuarios()
                opcion = pedir_opcion()
                if opcion == 1:
                    while True:
                        menu_registro_administracion()
                        opcion = pedir_opcion()
                        if opcion == 1:
                            agregar_informacion_administrador()
                elif opcion == 2:
                    pass
                elif opcion == 3:
                    pass
                elif opcion == 4:
                    break
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            pass
        elif opcion == 5:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")

# Llamada a la función principal
if __name__ == "__main__":
    main()
