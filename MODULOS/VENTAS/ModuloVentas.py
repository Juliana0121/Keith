#Modulo de ventas

import json
import datetime
import os


def cargar_datos(archivo):
    try:
        with open(archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def guardar_datos(datos, archivo):
    with open(archivo, 'w') as file:
        json.dump(datos, file, indent=4)

def crear_servicio(categoria, nombre, precio, descripcion, archivo):
    datos = cargar_datos(archivo) or {"Servicios": {}}
    datos["Servicios"].setdefault(categoria, {})
    datos["Servicios"][categoria][nombre] = {"precio": precio, "descripcion": descripcion}
    guardar_datos(datos, archivo)

def leer_servicios(archivo):
    datos = cargar_datos(archivo)
    return datos["Servicios"] if datos and "Servicios" in datos else {}

def actualizar_servicio(categoria, nombre, nuevo_precio, nueva_descripcion, archivo):
    datos = cargar_datos(archivo)
    if datos and categoria in datos["Servicios"] and nombre in datos["Servicios"][categoria]:
        datos["Servicios"][categoria][nombre]["precio"] = nuevo_precio
        datos["Servicios"][categoria][nombre]["descripcion"] = nueva_descripcion
        guardar_datos(datos, archivo)
        return True
    return False

def eliminar_servicio(categoria, nombre, archivo):
    datos = cargar_datos(archivo)
    if datos and categoria in datos["Servicios"] and nombre in datos["Servicios"][categoria]:
        del datos["Servicios"][categoria][nombre]
        guardar_datos(datos, archivo)
        return True
    return False


def crear_producto(nombre, precio, descripcion, archivo):
    datos = cargar_datos(archivo) or {"Productos": {}}
    datos["Productos"][nombre] = {"precio": precio, "descripcion": descripcion}
    guardar_datos(datos, archivo)

def leer_productos(archivo):
    datos = cargar_datos(archivo)
    return datos["Productos"] if datos and "Productos" in datos else {}

def actualizar_producto(nombre, nuevo_precio, nueva_descripcion, archivo):
    datos = cargar_datos(archivo)
    if datos and nombre in datos["Productos"]:
        datos["Productos"][nombre]["precio"] = nuevo_precio
        datos["Productos"][nombre]["descripcion"] = nueva_descripcion
        guardar_datos(datos, archivo)
        return True
    return False

def eliminar_producto(nombre, archivo):
    datos = cargar_datos(archivo)
    if datos and nombre in datos["Productos"]:
        del datos["Productos"][nombre]
        guardar_datos(datos, archivo)
        return True
    return False

def realizar_compra():
    return


def registrar_compra(tipo, nombre, cantidad):
    archivo_ventas = 'ModuloVentas.json'

    if os.path.exists(archivo_ventas):
        with open(archivo_ventas, 'r') as file:
            ventas = json.load(file)
    else:
        ventas = []

    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    compra = {
        "tipo": tipo,
        "nombre": nombre,
        "cantidad": cantidad,
        "fecha_hora": fecha_hora
    }

    ventas.append(compra)

    with open(archivo_ventas, 'w') as file:
        json.dump(ventas, file, indent=4)

    print("Compra registrada exitosamente.")

    