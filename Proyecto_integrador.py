
# PROYECTO INTEGRADOR
# SISTEMA DE CATALOGO DE TIENDA

# 1. Diccionario inicial de productos

catalogo = {
    "P01": {
        "nombre": "Cuaderno argollado",
        "precio": 6500,
        "stock": 20
    },
    "P02": {
        "nombre": "Caja de micropuntas",
        "precio": 18000,
        "stock": 12
    },
    "P03": {
        "nombre": "Resma de papel",
        "precio": 15000,
        "stock": 8
    }
}


# Funcion para leer numeros enteros positivos

def leer_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero > 0:
                return numero
            else:
                print("Error: ingrese un numero mayor que cero.")

        except ValueError:
            print("Error: debe ingresar un numero entero.")


# 2. Busqueda segura de productos

def buscar_producto():
    codigo = input("Ingrese el codigo del producto: ").strip().upper()

    producto = catalogo.get(codigo)

    if producto is not None:
        print("\n--- DATOS DEL PRODUCTO ---")
        print("Codigo:", codigo)
        print("Nombre:", producto.get("nombre"))
        print("Precio:", producto.get("precio"))
        print("Stock:", producto.get("stock"))
    else:
        print("\nAdvertencia: el producto no existe en el catalogo.")


# 3. Ingreso de existencias

def ingresar_existencias():
    codigo = input("Ingrese el codigo del producto: ").strip().upper()

    producto = catalogo.get(codigo)

    if producto is not None:
        cantidad = leer_entero("Ingrese la cantidad que desea agregar: ")

        producto["stock"] += cantidad

        print("\nExistencias actualizadas correctamente.")
        print("Nuevo stock:", producto["stock"])

    else:
        print("\nAdvertencia: no se encontro ese producto.")


# 4. Registro de productos nuevos

def registrar_producto():
    codigo = input("Ingrese el codigo del producto: ").strip().upper()

    if codigo == "":
        print("Error: el codigo no puede estar vacio.")
        return

    if codigo in catalogo:
        print("Este codigo ya existe en el catalogo.")
        confirmacion = input("¿Desea reemplazar el producto? (si/no): ").strip().lower()

        if confirmacion != "si":
            print("Operacion cancelada.")
            return

    nombre = input("Ingrese el nombre del producto: ").strip()

    if nombre == "":
        print("Error: el nombre no puede estar vacio.")
        return

    precio = leer_entero("Ingrese el precio unitario: ")
    stock = leer_entero("Ingrese la cantidad inicial: ")

    nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "stock": stock
    }

    catalogo.update({codigo: nuevo_producto})

    print("\nProducto registrado correctamente.")


# 5. Calculo del valor total del inventario

def calcular_valor_inventario():
    valor_total = 0

    for producto in catalogo.values():
        valor_producto = producto["precio"] * producto["stock"]
        valor_total += valor_producto

    print("\n--- VALOR DEL INVENTARIO ---")
    print("El valor total del inventario es: $", valor_total)


# 6. Mostrar todos los productos

def mostrar_catalogo():
    print("\n--- CATALOGO COMPLETO ---")

    if len(catalogo) == 0:
        print("No hay productos registrados.")
        return

    print("Codigos registrados:", list(catalogo.keys()))

    for codigo, producto in catalogo.items():
        print("----------------------------")
        print("Codigo:", codigo)
        print("Nombre:", producto["nombre"])
        print("Precio: $", producto["precio"])
        print("Stock:", producto["stock"])


# 7. Menu principal del programa

def menu():
    while True:
        print("\n================================")
        print("     SISTEMA DE CATALOGO")
        print("================================")
        print("1. Buscar producto")
        print("2. Ingresar existencias")
        print("3. Registrar producto")
        print("4. Calcular valor del inventario")
        print("5. Mostrar catalogo completo")
        print("6. Salir")
        print("================================")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            buscar_producto()

        elif opcion == "2":
            ingresar_existencias()

        elif opcion == "3":
            registrar_producto()

        elif opcion == "4":
            calcular_valor_inventario()

        elif opcion == "5":
            mostrar_catalogo()

        elif opcion == "6":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nOpcion no valida. Intente nuevamente.")


# Inicio del programa

menu()
