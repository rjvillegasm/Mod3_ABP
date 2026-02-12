
import time
from modulos import menu, operaciones_inventario

#función main para controlar el flujo del programa
def main():
    print("¡Bienvenido al Sistema de Gestión de Inventario ABP!")
    while True:
        menu.mostrar_menu()            
        opcion = menu.seleccionar_opcion()
        
        if opcion=="1":
            operaciones_inventario.agregar_producto()
            pass
        
        elif opcion=="2":
            operaciones_inventario.eliminar_producto()
            pass
        
        elif opcion=="3":
            operaciones_inventario.modificar_producto()
            pass
        
        elif opcion=="4":
            operaciones_inventario.buscar_producto()
            pass
        
        elif opcion=="5":
            operaciones_inventario.mostrar_inventario()
            pass
        
        elif opcion=="6":
            operaciones_inventario.calcular_valor_inventario()
            pass

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