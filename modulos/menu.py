
#función que mustra el menu principal
def mostrar_menu():
    print("\n MENÚ PRINCIPAL")
    print("---------------")
    print("Opciones disponibles:")
    print("1. Agregar nuevo producto")
    print("2. Eliminar producto")
    print("3.Modificar producto")
    print("4. Buscar producto")
    print("5. Mostrar inventario completo")
    print("6. Calcular valor total del inventario")
    print("7. Salir")


def seleccionar_opcion():
    
    opcion = input("Selecciona una opción (1-7): ")
    return opcion    

