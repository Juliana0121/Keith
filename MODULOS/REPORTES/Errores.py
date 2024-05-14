import json
import os
import datetime

# Decir los nombres de los archivos json para guardar los servicios y las ventas
archivo_servicios = "servicios.json"
archivo_ventas = "ventas.json"
archivo_log = "log_errores.txt"

def cargar_servicios():
    if os.path.exists(archivo_servicios):
        with open(archivo_servicios, "r") as file:
            return json.load(file)
    else:
        return []

def cargar_ventas():
    if os.path.exists(archivo_ventas):
        with open(archivo_ventas, "r") as file:
            return json.load(file)
    else:
        return []

# Registra errores del archivo de registro
def registrar_error(error):
    with open(archivo_log, "a") as file:
        file.write(f"{datetime.datetime.now()}: {error}\n")

# Hace un  informe sobre la cantidad de productos o servicios ofrecidos por la empresa
def generar_informe_servicios():
    try:
        servicios = cargar_servicios()
        if servicios:
            print("Informe de Servicios:")
            for servicio in servicios:
                print(f"- {servicio['nombre']}: {servicio['cantidad']} unidades")
        else:
            print("No hay servicios registrados.")
    except Exception as e:
        print(f"Error al generar informe de servicios: {e}")
        registrar_error(f"Error al generar informe de servicios: {e}")

# Crea un informe sobre los servicios más populares
def generar_informe_servicios_populares():
    try:
        ventas = cargar_ventas()
        if ventas:
            servicios_vendidos = {}
            for venta in ventas:
                servicio = venta["servicio"]
                if servicio in servicios_vendidos:
                    servicios_vendidos[servicio] += 1
                else:
                    servicios_vendidos[servicio] = 1
            if servicios_vendidos:
                print("Servicios más populares:")
                for servicio, cantidad in sorted(servicios_vendidos.items(), key=lambda x: x[1], reverse=True):
                    print(f"- {servicio}: {cantidad} ventas")
            else:
                print("No hay ventas registradas.")
        else:
            print("No hay ventas registradas.")
    except Exception as e:
        print(f"Error al generar informe de servicios populares: {e}")
        registrar_error(f"Error al generar informe de servicios populares: {e}")

# CRea un informe sobre los usuarios que han tomado cada servicio
def generar_informe_usuarios_por_servicio():
    try:
        ventas = cargar_ventas()
        if ventas:
            usuarios_por_servicio = {}
            for venta in ventas:
                servicio = venta["servicio"]
                usuario = venta["usuario"]
                if servicio in usuarios_por_servicio:
                    if usuario in usuarios_por_servicio[servicio]:
                        usuarios_por_servicio[servicio][usuario] += 1
                    else:
                        usuarios_por_servicio[servicio][usuario] = 1
                else:
                    usuarios_por_servicio[servicio] = {usuario: 1}
            if usuarios_por_servicio:
                print("Usuarios por Servicio:")
                for servicio, usuarios in usuarios_por_servicio.items():
                    print(f"- {servicio}:")
                    for usuario, cantidad in usuarios.items():
                        print(f"  - {usuario}: {cantidad} compras")
            else:
                print("No hay ventas registradas.")
        else:
            print("No hay ventas registradas.")
    except Exception as e:
        print(f"Error al generar informe de usuarios por servicio: {e}")
        registrar_error(f"Error al generar informe de usuarios por servicio: {e}")

# Ejemploo
print("\nMenú de Reportes:")
print("1. Generar Informe de Servicios")
print("2. Generar Informe de Servicios Populares")
print("3. Generar Informe de Usuarios por Servicio")
print("4. Salir")
opcion = input("Seleccione una opción: ")

if opcion == "1":
    generar_informe_servicios()
elif opcion == "2":
    generar_informe_servicios_populares()
elif opcion == "3":
    generar_informe_usuarios_por_servicio()
elif opcion == "4":
    print("Salir")