tasadolarhoy= 0.00
salariocol= 0.00
salarioenusd= 0.00

def cambio_peso_a_USD ():

    global tasadolarhoy
    global salariocol
    global salarioenusd
    tasadolarhoy= float(input("Digite el valor del dolar corresponiente a la tasa de hoy: "))
    salariocol= float(input("Digite su salario: "))
    salarioenusd = salariocol / tasadolarhoy
    print(f"Su salario convertido en dolares {salarioenusd}")