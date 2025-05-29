
#------------------//---------------------------------------------------------------
#Add product to inventory 
surtimax=[]
for i in range (2):
        new_product=str(input(f"Ingrese nuevo producto #{i+1}: "))
        price= int(input(" Ingrese precio del producto: "))
        available= int(input (" Ingrese cantidad disponible: "))
        disp={"product":new_product, "price":price, "available":available}
        surtimax.append(disp)
print(surtimax)
#---------------------//------------------------------------------------------------
#Search for product in inventory #buscar producto
def Search_for_product(): 
    product=input( " Buscar producto: ")
    for value in surtimax:
        if value["product"]== product:
            print(value)
            break
    else:
        print(" El producto no esta en el inventario: ")
#--------------------------//-------------------------------------------------------------
#option to search for existing product in inventory and change sales price
#Update Price 
def update_price(): 
    valor=input("Ingrese el nombre del producto para actualizar: ")
    newprice=float(input(" Ingrese precio actualizado: "))
    for  value in surtimax:
            if value ["product"]== valor:
                value.update({"price": newprice})
                print(surtimax)
                break
#---------------------//----------------------------------------------------------------
#Remove product 
def remove_product():
    product=input("Producto que desea eliminar del inventario: " )
    for producto in (surtimax):
        if producto ["product"]==product:
            surtimax.remove(producto)
            break
        else: 
            continue
answer= """Selecciona una opción: 
        1. MOSTRAR INVENTARIO
        2. BUSCAR PRODUCTO
        3. ELEGIR PRODUCTO PARA CAMBIAR PRECIO
        4. ELIMINAR PRODUCTO
        5. SUMA TOTAL DE PRECIOS DE LA TIENDA 
        6. ABANDONAR 
"""
while True:
    number_option= input(answer)
    if number_option== "1":
        print(surtimax)
    elif number_option=="2":
        Search_for_product()
    elif number_option=="3":
        update_price()
    elif number_option=="4":
        remove_product()
    elif number_option=="5":
        prices= lambda surtimax: sum(product["price"]*product["available"] for product in surtimax)
        Tprices= prices(surtimax)
        
        print(f"{Tprices:.2f}")
    elif number_option=="6":
        print("OFF")
        break
    else:
        print("Error, Ingresa un número de 1 a 7:")