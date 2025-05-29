#pedir al usuario ingresar una nota númerica entre 0 y 100 
#verificar si los datos ingresados son correctos 
#validar si el estudiante aprobo o reprobo 

note= [] #lista para guardar las notas
Nnote =int(input("Ingresa la cantidad de notas: " )) #Variable para guardar cantidad de notas
datumnote= 0
Tnotas=0
average=0
count=0 

for i in range (Nnote):  
    #ingresar notas
    while True: 
        try: 
            datumnote = input("Ingrese una nota: ")
            if datumnote.isnumeric():  # Verificar si la entrada es numérica 
                datumnote=float (datumnote) #convertir la entrada a un número decimal
                note.append(datumnote)#agregar la nota ala lista 'note'
                if 0 < datumnote <= 40: #verificación de notas si es menor a 40
                    print("La nota fue reprobada: ")
                    break #salir del bucle 'while' para pedir la sigueinte nota
                elif 40 < datumnote <= 100: #verificación de noras si esta fue aprobada
                    print("La nota fue aprobada: ") 
                    break#salir del bucle interno'while' para pedir la siguiente nota
                else: 
                    print("Nota incorrecta: ") #la nota no esta en el rango esperado 
            else:
                print("El rango de las notas debe ser entre 0 y 100: ")#la nota no fue número
        except ValueError:
            print("Valor incorrecto: ")# error al intentar convertir la entrada a un número
    Tnotas= Tnotas + note[i]
    count= note
    average = (Tnotas) /  (Nnote)

result= input("Ingrese las notas separadas por ',': ")#pedir al usuario que ingrese las notas separadas por comas en la misma línea
taverage= result.split("***")#mosotrar las notas separadas por comas 
print(taverage) 

print(f"La suma de sus notas es {Tnotas} y su promedio es {average: .2f}   ")#suma de notas y calcular promedio 
if average > 40: 
            print("La nota es aprobada: ")
            
elif average <= 40: 
            print("No aprobo sus notas:  ")
cont=0 #inicar contador de notas para validar cuales se repiten 
punt=int(input("Elija una nota para validar las veces que se repite: "))#pedir al usuario una de las notas para validar cuantas veces se repite 
for i in range(Nnote): 
    print(punt)
    print(note)
    if punt == note[i]:
        cont= cont+1 
        

print("Las veces que esta se repite son: ", cont)

cont2=0 # inicializar un contador de notas mayores a un valor
valid=int(input("Ingrese un nota para validar cuales son mayores: "))#pedir al usuario un numero para validar cuales son mayores 

for i in range(Nnote): 
    if valid < note[i]:
        cont2= cont2+1 
        
print("La cantidad de notas mayores son: ", cont2) #imprimir la cantidad de notas mayores 
if cont2 == 0 :
    print("No hay notas mayores a la nota ingresada" , cont2) #decir si no hay notas mayores






    



    