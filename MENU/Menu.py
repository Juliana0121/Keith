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

def historial_usuarios():
    print("----------------------------------------")
    print("Historial de usuarios ")
    print("----------------------------------------")
    print("1. Servicios utilizados por el usuario")
    print("2. Comunicación del cliente con la empresa")
    print("3. Volver al menú de administración de usuarios")
    print("----------------------------------------")

def menu_personalizar_servicios():
    print("----------------------------------------")
    print("Personalización de servicios ")
    print("----------------------------------------")
    print("1. Ver servicios utilizados por el cliente")
    print("2. Ver comunicaciones del cliente con la empresa")
    print("3. Volver al menú de administración de usuarios")
    print("----------------------------------------")

def menu_ventas():
    print("----------------------------------------")
    print("Ventas ")
    print("----------------------------------------")
    print("1. Registro de ventas ")
    print("2. Consultar ventas ")
    print("3. Volver al menú principal")
    print("----------------------------------------")

def menu_reportes():
    print("----------------------------------------")
    print("Reportes ")
    print("----------------------------------------")
    print("1. Generar reporte de ventas ")
    print("2. Generar reporte de servicios más populares ")
    print("3. Volver al menú principal")
    print("----------------------------------------")

def pedir_opcion():
    try:
        opc = int(input("Ingrese su opción: "))
        print("----------------------------------------")
        return opc
    except ValueError:
        print("Por favor, ingrese un número válido.")
        print("----------------------------------------")
        return -1
