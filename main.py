
import time
from modulos import menu, operaciones_inventario, validaciones

#función main para controlar el flujo del programa
def main():
    print("¡Bienvenido al Sistema de Gestión de Inventario ABP!")
    while True:
        menu.mostrar_menu()            
        opcion = menu.seleccionar_opcion()
        
        if opcion=="1":
            new_id = input("Ingrese un id: ")
            new_nombre = input("Ingrese nombre del producto: ")
            new_precio = input("Ingrese el precio: ")
            new_cantidad= input("Ingrese la cantidad en unidades: ")
            categoria= input(" Ingrese una de las sgts categorías:\n Abarrotes, Higiene, Bebidas, Lácteos, Bebidas, Limpieza): ")
            
            operaciones_inventario.agregar_producto(new_id, new_nombre, new_precio, new_cantidad, categoria)
            
        
        elif opcion=="2":
            id_eliminar = input("Ingrese un id a eliminar: ")
            nombre_eliminar = input("Ingrese nombre del producto a: ")
            operaciones_inventario.eliminar_producto(id_eliminar, nombre_eliminar)
            
        
        elif opcion=="3":
            id = input("Ingrese un id para seleccionar el producto ")
            new_nombre = input("Ingrese nuevo nombre del producto: ")
            new_precio = input("Ingrese el nuevo precio: ")
            new_cantidad= input("Ingrese la nueva cantidad en unidades: ")
            categoria= input(" Ingrese una de las sgts categorías:\n Abarrotes, Higiene, Bebidas, Lácteos, Bebidas, Limpieza): ")

            operaciones_inventario.modificar_producto(id,new_nombre,new_precio, new_cantidad, categoria )
            
        
        elif opcion=="4":
            nombre_buscar = input("Ingrese nombre del producto buscado: ")
            operaciones_inventario.buscar_producto(nombre_buscar)
            
        
        elif opcion=="5":
            operaciones_inventario.mostrar_inventario()
            
        
        elif opcion=="6":
            operaciones_inventario.calcular_valor_inventario()
            

        elif opcion=="7":
            print("¡Gracias por usar el sistema de gestión de inventario!")
            print("Saliendo del programa...")
            time.sleep(1)
            break   
        
        else:
            print("Opción no válida, intente nuevamente.")

# constructor
if __name__ == "__main__":
    main()