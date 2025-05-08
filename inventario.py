
#Añanadir productos
inventory=[{"product":"computador", "precio":200.000, "disponibles":26},
{"product":"televisor", "precio":500.000, "disponibles":17 },
{"product":"monitor",  "precio":480.000, "disponibles":19},
{"product":"mouse", "precio":25.000, "disponibles":15}]  
# print(inventory)

# ------------------------------------//-------------------------------------
#Ingresar productos 
def new_product():
    new_product=str (input("Ingrese nuevo producto: "))
    precio= float(input("Ingrese el precio del producto: "))
    disponibles= int(input("Ingresa la cantidad disponible: "))
    inventory.append({"product":new_product, "precio":precio, "disponibles":disponibles})
    print(inventory)
    
# -------------------------------//------------------------------------------
#Buscar productos
def buscar_producto(): 
    product= input("Producto que deseas buscar: ")
    encontrado=True
    for i in (inventory):  
        if i ["product"] == product: 
            print (i)
            encontrado=True
            break
        else:
            encontrado=False
    if encontrado==False:
        print("Producto no existente. ")
# buscar_producto()

# ------------------------------------//-------------------------------------
#// formula para buscar producto dentro del inventario. 
def buscar_producto_para_actualizar():
    i=0 
    product= input("Producto que deseas buscar para cambiar precio: ")
    for producto in (inventory):  
        i = i-1
        if producto ["product"] == product: 
            i=i-1
            break
        else:
            continue
    return i

# ------------------------------------//-------------------------------------

#//Formaula para actualizar precios del inventario 
def actualizar_precio():  
    posicion_del_producto_actualizar= buscar_producto_para_actualizar()
    inventory[posicion_del_producto_actualizar]["precio"]= newprice= input("Ingrese nuevo precio: ")
    print(inventory)
# actualizar_precio()

# ------------------------------------//-------------------------------------

#eliminar productos del inventario 
def eliminar(): 
    i=0
    product= input("Producto que deseas eliminar: ")
    for producto in (inventory): #la i es para recorrer el código 
        i=i+1
        
        if producto ["product"] == product: 
            i=i-1
            del inventory[i]
            break
        else: 
            continue
    print(inventory)      

# ------------------------------------//-------------------------------------


respuesta="""selecciona lo que desear hacer:

1. Mostrar inventario
2. Buscar Producto
3. Actualizar Precio 
4. Agregar Producto al inventario
5. Eliminar Producto
6. Valor total productos 
7. Salir del menu
"""

while True: 
    numero_opcion =input(respuesta) 

    if  numero_opcion== "1":
        print(inventory)
    elif numero_opcion=="2": 
        buscar_producto()
    elif numero_opcion=="3":
        actualizar_precio()
    elif numero_opcion=="4":
        new_product()
    elif numero_opcion=="5":
        eliminar()
    elif numero_opcion=="6": 
        # funcion lambda para suma 
        precios= lambda inventory: sum(producto["precio"]*producto["disponibles"] for producto in inventory)
        Tprecios= precios(inventory)
        print(Tprecios)
    elif numero_opcion=="7": 
        print("salir")
        break


