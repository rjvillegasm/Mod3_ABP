
from modulos import validaciones

# Estructuras de datos: 
# 
# diccionarios anidados

inventario = {
    "P001": {
        "nombre": "Arroz",
        "cantidad": 10,
        "precio": 2000,
        "categoria": "Abarrotes"
    },
    "P002": {
        "nombre": "Detergente",
        "cantidad": 25,
        "precio": 4000,
        "categoria": "Limpieza"
    },
    "P003": {
        "nombre": "Fideos",
        "cantidad": 15 ,
        "precio": 900,
        "categoria": "Abarrotes"
    },
    "P004": {
        "nombre": "Azucar",
        "cantidad": 8 ,
        "precio":1100  ,
        "categoria": "Abarrotes"
    },
    "P005": {
        "nombre": "Cloro",
        "cantidad": 5 ,
        "precio": 1200,
        "categoria": "Limpieza"
    },
    "P006": {
        "nombre": "Cocacola",
        "cantidad":6 ,
        "precio": 1500 ,
        "categoria": "Bebidas"
    },
    "P007": {
        "nombre": "Jabon glicerina",
        "cantidad": 4,
        "precio": 1700 ,
        "categoria": "Higiene"
    },
    "P008": {
        "nombre": "Leche en caja",
        "cantidad": 6,
        "precio": 1400,
        "categoria": "Lácteos"
    },
    "P009": {
        "nombre": "Champú",
        "cantidad":7 ,
        "precio": 2500,
        "categoria": "Higiene"
    },
    "P010": {
        "nombre": "Queso gauda sachet ",
        "cantidad": 8 ,
        "precio": 2400 ,
        "categoria": "Lácteos"
    }  
    
}
# conjuntos ids únicos
ids_utilizados= {"P001", "P002", "P003","P004", "P005",
"P006", "P007", "P008", "P009","P010" }

# caegorías tupla
categorias=("Abarrotes", "Higiene", "Bebidas", "Lácteos", "Bebidas", "Limpieza")

#función para agregar un producto
def agregar_producto(id, nombre, precio, cantidad, categoria):  
    if validaciones.verificar_producto(id, nombre):
        print("ID o nombre ya utilizados")
    else:
        if validaciones.verificar_categoria(categoria):
            new_producto={ "nombre": nombre,
                        "cantidad": cantidad ,
                        "precio": precio ,
                        "categoria": categoria,
                        }
            inventario[id]= new_producto
            ids_utilizados.add(id)  
        else:
            print("Categoría no existente, intente nuevamente.")
        

#función para eliminar un producto
def eliminar_producto(id, nombre):
    if validaciones.verificar_producto(id, nombre):
        producto_eliminado= inventario.pop(id,None)
        print(f"Se ha eliminado: {producto_eliminado}")
        ids_utilizados.remove(id)
    else:
        print("Producto ó ID incorrectos")
        
#función para modificar un producto existente
# el ID no puede ser modificado, en caso de error se debe borrar el producto y volver a ingresar
def modificar_producto(id,nombre, precio, cantidad,categoria):
    if validaciones.verificar_producto(id, nombre):
        if validaciones.verificar_categoria(categoria):         
            inventario[id]["nombre"]=nombre
            inventario[id]["precio"]=precio
            inventario[id]["cantidad"]=cantidad
            inventario[id]["categoria"]=categoria
            print(f"El producto modificado ha sido registrado como; nombre: {nombre}, precio: {precio}, cantidad: {cantidad}, categoría: {categoria} ")
        else:
            print("La categoría debe pertenecer a las pre-existentes")
    else:
        print("Producto ó ID incorrectos")
  
#función para buscar un producto
def buscar_producto(nombre):
    for codigo, producto in inventario.items():
        if nombre.lower()==producto["nombre"].lower():
            print("--------------")
            print(f"Código: {codigo}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Cantidad: {producto['cantidad']}")
            print(f"Precio: {producto['precio']}")
            print(f"Categoría: {producto['categoria']}")
            return
    print("Nombre del producto no encontrado")
        
    

#función para mostrar el inventario
def mostrar_inventario():
    print("\n")
    for codigo, producto in inventario.items():
        print(f"{codigo}: {producto}")

#función para obtener el valor del inventario
def calcular_valor_inventario():
    total=0
    for producto in inventario.values():
        total += producto["precio"]*producto["cantidad"]
    
    print(f" El valor del inventario es: {total} pesos")

