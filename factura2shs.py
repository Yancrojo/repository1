Nproducto = [] #lista para guardar los nombres de los productos
Preciounitario= [] # lista para guardar el precio de los productos por unidad 
precioFinal=0 #variable para obtener el precio y total a pagar 
descuento=0  #variable para realizar descuento 
pfdescuento=0 #variable para obtener precio final con descuento 


while True: 
    try:
        # Si el número es mayor a 0 hace el break saliendo del ciclo, sino lanza un mensaje de error repitiendo el bucle hasta obtener el dato correcto
        CantidadProductos = int(input("Ingrese la cantidad de productos: "))
        if CantidadProductos > 0:
            break  
        else:
            print("ERROR: La cantidad debe ser mayor a 0. Intenta de nuevo.")
    except ValueError:
        print("ERROR: Debes ingresar un número válido. Intenta de nuevo.")

#bucle para ingresar la información de los productos 
for i in range(CantidadProductos):
    Nproducto.append(input("Ingrese nombre del producto: "))
    Preciounitario.append(int(input("Ingrese el precio del producto: ")))
    precioFinal = precioFinal + Preciounitario[i]

#bucle para mostrar la lista y precio de los productos 
for i in range(CantidadProductos):
    print(f"{Nproducto[i]} {Preciounitario[i]:.2f}")

#impresion para mostrar precio total
print(f"El precio total de sus productos comprados es {precioFinal:.2f}") 

#espacio para ingresar el descuento del día 
descdeldia = int(input("Ingrese el descuento del dia: "))
if 0 < descdeldia < 100: #validar que el descuento este entre 1 y 99 
    descuento = precioFinal * (descdeldia/100) #aplicar descuento del día 
    pfdescuento = precioFinal - descuento #calcula el valor del descuento, precio final 
    print(f"El descuento es del {descuento} y su valor a pagar es {pfdescuento:.2f}") #imprime el valor del descuento y el precio final
elif descdeldia == 0: #ingresa el porcentaje de descuento del día 

    print(f"El precio total de sus productos comprados es {precioFinal:.2f}") #imprime el precio final de la compra
else: 
    print(f"no tiene descuento {precioFinal:.2f}") #muestra el precio final 

# [] para  definir lista

