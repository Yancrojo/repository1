nombre = input("Ingrese nombre:")
segundo_n = input("Digite su segundo nombre: ")
apellido = input("Digite su apellido: ")

def formatear_nombre(name, middleName, lastname):
    namef= name.capitalize()
    middleNamef = middleName.capitalize()
    lastnamef = lastname.capitalize()

    return (namef + " " + middleNamef + " " + lastnamef)


print(formatear_nombre(nombre, segundo_n, apellido ))



    # print(f"{nombre.capitalize()}{segundo_n.lower()}{apellido.lower()}")