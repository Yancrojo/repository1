#Añanadir productos por su nombre, precio y cantidad disponible

inventory=[{"product":"computador","precio": 200.000,"disponibles": 26},
{"product":"televisor","precio": 500.000, "disponibles": 17 },
{"product":"monitor","precio": 480.000, "disponibles": 19},
{"product":"mouse","precio": 25.000, "disponibles": 15}]  
# print(inventory)

# ------------------------------------//-------------------------------------
#Agregar productos al inventario.
def new_product():
    new_product=str (input("  Ingrese nuevo producto: "))
    precio= float(input("  Ingrese el precio del producto: "))
    disponibles= int(input("  Ingresa la cantidad disponible: "))
    inventory.append({"  product":new_product, "precio":precio, "disponibles":disponibles})
    print(inventory)
    
# -------------------------------//------------------------------------------
#Buscar productos dentro de la lista para ver su disponibilidad, cantidad y precio 
def buscar_producto(): 
 
    while True:
            product= input(  "Producto que deseas buscar: ")
            if product.isalpha():
                    encontrado=False
                    for i in (inventory):  
                        if i.get("product") == product: 
                            print (i)
                            encontrado=True
                            break
                    if encontrado == False:
                        print( "Producto no existe" )
                        break
                    break
            else:
                print( "Ingrese una opción valida" )
    
      
            

# buscar_producto()

# ------------------------------------//-------------------------------------
#// formula para buscar producto dentro del inventario y actualizar precio de venta 
def buscar_producto_para_actualizar():
    # i=0 
    while True:
        try:
            product= input( "Producto que deseas buscar para cambiar precio: " )
            if product.isalpha():
                for i, producto in enumerate(inventory):  
                    # i = i-1
                    if producto["product"] == product: 
                        print(producto,product)
                        # i=i-1  
                        break   
                return i
            else:
                print( "Opción no valida, ingrese texto" )

        except ValueError:  
            print( "ERROR" )

#-----------------------------------------//----------------------------------------------------          
#actualiza precio de venta del producto que se elija 
def actualizar_precio():  
    posicion_del_producto_actualizar= buscar_producto_para_actualizar()
    while True:
        try: 
            
            newprice=input("Ingrese el nuevo precio: ")
            if newprice.isnumeric(): 
                inventory[posicion_del_producto_actualizar].update({"precio": newprice})
                print(inventory)
            else:
                print("ERROR. Ingrese nuevo precio")
            break    
        except ValueError:
            print("Vuelve a intetar")

        
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
#opciones de lo que requiere hacer en el sistema 
respuesta=  """ SELECCIONA UNA OPCIÓN:

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
        # funcion lambda para suma del total del inventario (cantidad en dinero)
        precios= lambda inventory: sum(producto["precio"]*producto["disponibles"] for producto in inventory)
        Tprecios= precios(inventory)
        print( Tprecios )
    elif numero_opcion=="7": 
        print("OFF")
        break
    else:
        print("Opción incorrecta, ingresa un número: ")