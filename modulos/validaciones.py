import operaciones_inventario
#funciónes para verficar si existe un producto antes de realizar las operaciones
#Utilizada por las demás funcionalidades pero no es un feature principal 

# verifica que el id no este utilizado previamente
def verificar_id(llave):
    return llave in operaciones_inventario.ids_utilizados

# primero verificamos el ID y luego el nombre
# ambas deben ser False para que permita agrear un producto
# si devuelve True el nombre o id están ocupados
def verificar_producto(id, nombre):
    
    if id in operaciones_inventario.inventario:
        return True
    
    # Verificar si nombre ya existe
    for producto in operaciones_inventario.inventario.values():
        if producto["nombre"].lower() == nombre.lower():
            return True
    
    return False



def verificar_categoria(cat):
    return cat in operaciones_inventario.categorias


