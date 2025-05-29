#add product
tecnology=[]
for i in range (5):
    # def add_product():
        add_product=str(input(f"Ingrese el producto {i+1}:  "))
        price=float(input("Ingrese su precio: "))
        available=int(input("Ingrese cantidad disponible: "))
        products={" product":add_product, "price":price, "available":available}
        tecnology.append(products)
print(tecnology)

def buscar_producto():
    while True:
            product=input("Busca el producto: ")
            if product.asalpha():
                    found=False
                    for i in (tecnology):
                        if i.get("product")==product:
                            print(i)
                            found=True
                            break
                        if found == False:
                            print("Producto no encontrado")
                            break
                        break
            else:
                print("Ingrese una opción valida: ")

def producto_para_actualizar():
            product=input("Producto que deseas cambiar precio: ")
            for producto in (tecnology):
                if producto ["product"]==product:
                    print(producto, product)
                    break
                else:
                    print("Opción no valida: ")
def actualizar_precio():
    producto_actualizar=actualizar_precio
    while True:
        try:
            newprice=input("Ingrese el nuevo precio: ")
            if newprice.isnumeric:
                tecnology[producto_actualizar].update({"precio",newprice})
                print(tecnology)
            else:
                print("Ingrese precio en número")
            break
        except ValueError:
            print("Vuelve a intentar: ")
def eliminar_producto():
    i=0
    product=("Producto para eliminar: ")
    for producto in (tecnology):
        i=i+1
        if producto["product: "]==product:
            i=i-1
            del tecnology[i]
            break
        else:
            continue
print(tecnology)

respuesta="""SELLECIONA UN NUMERO 
        1. AGREGAR UN PRODUCTO 
        2. BUSCAR UN PRODUCTO
        3.ACTUALIZAR PRECIO DEL PRODUCTO
        4.ELIMINAR PRODUCTO
        5.TOTAL PRECIO DE TODOS LOS PRODUCTOS
        6.SALIR
"""
while True:
    elegir_opcion=input(respuesta)
    if elegir_opcion=="1":
        add_product()
    elif elegir_opcion=="2":
        buscar_producto()
    elif elegir_opcion=="3":
        actualizar_precio()
    elif elegir_opcion=="4":
        eliminar_producto()
    elif elegir_opcion=="5":
        precios= lambda tecnology: sum(producto["precio"]*producto["disponibles"] for producto in tecnology)
        Tprecios= precios(tecnology)
        print(precios)
    elif elegir_opcion=="6":
        print("SALIR")
    else:
        print("Opción invalida: ingresa un número: ")

            

