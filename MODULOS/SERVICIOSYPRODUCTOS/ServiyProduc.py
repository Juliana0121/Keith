#Servicios y productos 
import json

def cargar_datos(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no existe.")
        return None
    except Exception as e:
        print(f"Error al cargar los datos del archivo '{nombre_archivo}': {e}")
        return None

def guardar_datos(datos, nombre_archivo):
    try:
        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos, archivo, indent=4)
        print(f"Los datos han sido guardados en '{nombre_archivo}' correctamente.")
    except Exception as e:
        print(f"Error al guardar los datos en el archivo '{nombre_archivo}': {e}")

def contar_ventas(datos):
    servicios_populares = {}
    productos_populares = {}

    ventas = datos.get("Ventas", [])
    for venta in ventas:
        producto = venta.get("Producto", "")

        # Cuenta las ventas de servicios
        if producto in datos["Servicios"]:
            servicios_populares[producto] = servicios_populares.get(producto, 0) + venta.get("Cantidad", 0)
        
        # Cuenta las ventas de los productos
        elif producto in datos["Productos"]:
            productos_populares[producto] = productos_populares.get(producto, 0) + venta.get("Cantidad", 0)

    return servicios_populares, productos_populares

def agregar_servicio(datos, categoria, nombre, precio):
    if categoria not in datos["Servicios"]:
        datos["Servicios"][categoria] = {}
    datos["Servicios"][categoria][nombre] = precio

def agregar_producto(datos, nombre, detalles):
    datos["Productos"][nombre] = detalles

def actualizar_servicio(datos, categoria, nombre, nuevo_precio):
    if categoria in datos["Servicios"] and nombre in datos["Servicios"][categoria]:
        datos["Servicios"][categoria][nombre] = nuevo_precio
    else:
        print(f"No se encontró el servicio '{nombre}' en la categoría '{categoria}'.")

def actualizar_producto(datos, nombre, nuevos_detalles):
    if nombre in datos["Productos"]:
        datos["Productos"][nombre].update(nuevos_detalles)
    else:
        print(f"No se encontró el producto '{nombre}'.")

# Actializa y CRUD
def actualizar_datos(nombre_archivo):
    datos = cargar_datos(nombre_archivo)
    if datos is None:
        return
    
    # Cuenta las ventas y actualiza los servicios y productos populares
    servicios_populares, productos_populares = contar_ventas(datos)
    datos["Servicios Populares"] = servicios_populares
    datos["Productos Populares"] = productos_populares
    
    
def cargar_servicios():
    try:
        with open("servicios.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_servicios(servicios):
    with open("servicios.json", "w") as file:
        json.dump(servicios, file, indent=4)

def agregar_servicio(nuevo_servicio):
    servicios = cargar_servicios()
    servicios.append(nuevo_servicio)
    guardar_servicios(servicios)

def obtener_servicio_por_identificador(identificador_servicio):
    servicios = cargar_servicios()
    for servicio in servicios:
        if servicio["Identificador"] == identificador_servicio:
            return servicio
    return None

def actualizar_servicio(identificador_servicio, datos_actualizados):
    servicios = cargar_servicios()
    for servicio in servicios:
        if servicio["Identificador"] == identificador_servicio:
            servicio.update(datos_actualizados)
            guardar_servicios(servicios)
            return True
    return False

def eliminar_servicio(identificador_servicio):
    servicios = cargar_servicios()
    for servicio in servicios:
        if servicio["Identificador"] == identificador_servicio:
            servicios.remove(servicio)
            guardar_servicios(servicios)
            return True
    return False 

def ver_catalogo():
    try:
        with open('MODULOS/SERVICIOSYPRODUCTOS/S&P.json', 'r') as file:
            catalogo = json.load(file)
            
            catalogo 
            print("Catálogo de Servicios y Productos:")
            for categoria, productos_servicios in catalogo.items():
                print(f"\n{categoria}:")
                for nombre, detalles in productos_servicios.items():
                    print(f"- {nombre}:")
                    for atributo, valor in detalles.items():
                        print(f"  - {atributo}: {valor}")
    except FileNotFoundError:
        print("El archivo 'S&P.json' no se encontró.")
    except Exception as e:
        print(f"Error al cargar el catálogo: {e}")
    return




    