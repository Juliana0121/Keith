"""
# ---------------------- Módulo de Administración ----------------------

# Funciones para administrar usuarios
def cargar_usuarios():
    try:
        with open('modulos/administracion/Usuarios.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def guardar_usuarios(usuarios):
    with open("modulos/administracion/Usuarios.json", "w") as file:
        json.dump(usuarios, file, indent=4)

def agregar_usuario(nuevo_usuario):
    usuarios = cargar_usuarios()
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)

def obtener_usuario_por_identificador(identificador_usuario):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["Identificador"] == identificador_usuario:
            return usuario
    return None

def actualizar_usuario(identificador_usuario, datos_actualizados):
    usuarios = cargar_usuarios()
    for usuario in usuarios:
        if usuario["Identificador"] == identificador_usuario:
            usuario.update(datos_actualizados)
            guardar_usuarios(usuarios)
            return True
    return False

def eliminar_usuario(identificador_usuario):
    usuarios = cargar_usuarios()
    usuarios_actualizados = [usuario for usuario in usuarios if usuario["Identificador"] != identificador_usuario]
    if len(usuarios_actualizados) != len(usuarios):
        guardar_usuarios(usuarios_actualizados)
        return True
    return False

# ---------------------- Módulo de Reportes ----------------------

# Funciones para cargar y guardar datos de ventas y servicios
archivo_servicios = "modulos/reportes/servicios.json"
archivo_ventas = "modulos/reportes/ventas.json"
archivo_log = "modulos/reportes/log_errores.txt"

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

# Función para registrar errores en el archivo de registro
def registrar_error(error):
    with open(archivo_log, "a") as file:
        file.write(f"{datetime.datetime.now()}: {error}\n")

# Funciones para generar informes sobre servicios
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

# ---------------------- Módulo de Servicios y Productos ----------------------

# Funciones para cargar y guardar datos de servicios y productos
archivo_servicios_productos = "modulos/servicios_y_productos/servicios_productos.json"

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

        if producto in datos["Servicios"]:
            servicios_populares[producto] = servicios_populares.get(producto, 0) + venta.get("Cantidad", 0)
        
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

# ---------------------- Módulo de Ventas ----------------------

# Funciones para cargar y guardar datos de ventas
archivo_ventas = "modulos/ventas/ventas.json"

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


"""